"""
Assistente de energia — módulo do Citizen Assist AI
Contribuição da disciplina Soluções em Energias Renováveis e Sustentáveis.

Responde perguntas sobre o gasto do chuveiro elétrico e como economizar, usando:
  - a ficha FC-08 (fichas/FC-08_energia_banho.md) como fonte do texto;
  - calculadora_energia.py para os números (o MESMO módulo do notebook 03_calculos.ipynb).

Por que regras e não um LLM aqui? Os números precisam ser exatamente os da análise.
Este módulo é determinístico. No assistente completo (GS de Prompt), o agente pode chamar
`responder()` como ferramenta e só reescrever o texto, sem mudar os valores.

Privacidade: o módulo só usa minutos de banho e número de pessoas. Ele detecta e mascara
CPF, telefone, e-mail e números longos antes de qualquer processamento, e não guarda histórico.

Uso pelo teclado:  python assistente_energia.py
"""

from __future__ import annotations

import re
import unicodedata

import calculadora_energia as ce

DATA_VERIFICACAO = "13/11/2026"
LIMITE_CARACTERES = 500
MINUTOS_A = 5  # meta da alternativa A (premissa P05)

# Ajuste 7 (testes com usuários): rodapé mais curto, com os dois avisos no início da linha.
RODAPE = (
    "\n\nATENÇÃO: os valores são estimativas, não são garantidos.\n"
    "ATENÇÃO: este assistente NÃO é um canal oficial. Confirme com a sua distribuidora de energia.\n"
    f"Fonte: ficha FC-08, verificada em {DATA_VERIFICACAO}."
)

MENU = (
    "Assistente de energia. Escolha um número ou escreva sua pergunta:\n"
    "1 - Quanto o meu banho gasta?\n"
    "2 - Como economizar no banho\n"
    "3 - Aquecedor solar vale a pena?\n"
    "4 - Tarifa Social (desconto na conta de luz)\n"
    "5 - Meio ambiente\n"
    "6 - Fontes e limitações\n"
    "0 - Sair"
)

# Ajuste 3 (testes com usuários): números por extenso de 1 a 69 ("doze", "vinte e cinco").
UNIDADES = {"um": 1, "uma": 1, "dois": 2, "duas": 2, "tres": 3, "quatro": 4, "cinco": 5,
            "seis": 6, "sete": 7, "oito": 8, "nove": 9}
DE_DEZ_A_DEZENOVE = {"dez": 10, "onze": 11, "doze": 12, "treze": 13, "catorze": 14, "quatorze": 14,
                     "quinze": 15, "dezesseis": 16, "dezessete": 17, "dezoito": 18, "dezenove": 19}
DEZENAS = {"vinte": 20, "trinta": 30, "quarenta": 40, "cinquenta": 50, "sessenta": 60}
NUMEROS_POR_EXTENSO = {**UNIDADES, **DE_DEZ_A_DEZENOVE, **DEZENAS}

_PREMISSAS = None


def _premissas():
    global _PREMISSAS
    if _PREMISSAS is None:
        _PREMISSAS = ce.carregar_premissas()
    return _PREMISSAS


# ------------------------------------------------------------------ utilidades
def normalizar(texto: str) -> str:
    """Minúsculas e sem acentos, para comparar palavras-chave."""
    sem_acento = unicodedata.normalize("NFD", texto)
    sem_acento = "".join(c for c in sem_acento if unicodedata.category(c) != "Mn")
    return sem_acento.lower()


def brl(valor: float) -> str:
    return f"{valor:,.0f}".replace(",", ".")


def anos(valor: float) -> str:
    return f"{valor:.1f}".replace(".", ",")


# ------------------------------------------------------------------ privacidade
PADROES_DADOS = [
    ("e-mail", re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")),
    ("CPF", re.compile(r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b")),
    ("telefone", re.compile(r"(\(?\b\d{2}\)?\s?)?\b9?\d{4}-?\d{4}\b")),
    ("número de documento", re.compile(r"\b\d{7,}\b")),
]


def proteger_dados(texto: str) -> tuple[str, list[str]]:
    """Troca dados pessoais por [removido] ANTES de qualquer processamento."""
    encontrados = []
    for nome, padrao in PADROES_DADOS:
        if padrao.search(texto):
            encontrados.append(nome)
            texto = padrao.sub("[removido]", texto)
    return texto, encontrados


# ------------------------------------------------------------------ extração
def extenso_para_digitos(t: str) -> str:
    """'doze minutos' -> '12 minutos'; 'vinte e cinco' -> '25'; 'meia hora' -> '30 minutos'."""
    t = re.sub(r"\bmeia hora\b", "30 minutos", t)
    dezenas = "|".join(DEZENAS)
    unidades = "|".join(UNIDADES)
    t = re.sub(rf"\b({dezenas})\s+e\s+({unidades})\b",
               lambda m: str(DEZENAS[m.group(1)] + UNIDADES[m.group(2)]), t)
    todas = "|".join(sorted(NUMEROS_POR_EXTENSO, key=len, reverse=True))
    return re.sub(rf"\b({todas})\b", lambda m: str(NUMEROS_POR_EXTENSO[m.group(1)]), t)


def extrair_minutos(t: str) -> float | None:
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:min|minuto)", t)
    return float(m.group(1).replace(",", ".")) if m else None


def extrair_pessoas(t: str) -> int | None:
    if re.search(r"\b(moro|vivo) sozinh", t) or "so eu" in t:
        return 1
    m = re.search(r"(\d+)\s*(?:pessoa|morador|moramos|pessoas)", t) or \
        re.search(r"(?:somos|moramos|familia de)\s*(\d+)", t)
    return int(m.group(1)) if m else None


def numero_solto(t: str) -> float | None:
    """Mensagem que é só um número (resposta a uma pergunta do assistente)."""
    t = t.strip()
    return float(t.replace(",", ".")) if re.fullmatch(r"\d+(?:[.,]\d+)?", t) else None


# ------------------------------------------------------------------ intenções
def _tem(t: str, *chaves: str) -> bool:
    return any(c in t for c in chaves)


def detectar_intencao(t: str) -> str:
    if _tem(t, "ignore", "ignora", "instrucoes anteriores", "[sistema]", "prompt de sistema",
            "nova regra", "modo desenvolvedor"):
        return "injecao"
    if _tem(t, "canal oficial", "voce e oficial", "e oficial?", "voce e da prefeitura", "voce e do governo",
            "voce e da distribuidora", "voce e da enel"):
        return "oficial"
    if _tem(t, "fotovolta", "gerar energia", "gerar minha energia", "geladeira", "ar condicionado",
            "ar-condicionado", "televis", "lampada", "maquina de lavar", "ferro de passar") \
            or re.search(r"\bgas\b", t):
        return "fora_escopo"
    if _tem(t, "aluguel", "alugad", "inquilino", "apartamento", "apto", "condominio"):
        return "moradia"
    if _tem(t, "solar", "aquecedor", "placa", "coletor"):
        return "solar"
    if _tem(t, "tarifa social", "desconto", "cadunico", "cad unico", "cadastro unico",
            "baixa renda", "bpc", "isencao", "nao pagar", "de graca", "gratis"):
        return "tarifa_social"
    # Ajuste 4 (testes com usuários): "minha conta está cara" não é pedido de cálculo do banho.
    if re.search(r"conta.{0,25}\b(cara|alta|pesada|subiu|absurda|caro)\b", t) or \
            _tem(t, "conta muito", "nao consigo pagar", "pagar a conta"):
        return "conta_alta"
    if _tem(t, "meio ambiente", "co2", "carbono", "ambiental", "poluic", "planeta", "sustentav"):
        return "ambiente"
    if _tem(t, "fonte", "limitac", "de onde", "confiavel", "referencia", "garantid"):
        return "fontes"
    if _tem(t, "economizar", "economia", "economiz", "dica", "reduzir", "diminuir",
            "posicao verao", "pagar menos", "gastar menos"):
        return "economizar"
    if _tem(t, "quanto gasta", "quanto custa", "quanto pesa", "gasto", "consumo", "conta de luz",
            "chuveiro", "banho", "kwh", "energia", "luz"):
        return "calcular"
    if re.search(r"\b(oi|ola|bom dia|boa tarde|boa noite|menu|ajuda|opcoes)\b", t):
        return "menu"
    return "nao_entendi"


OPCOES_MENU = {"1": "calcular", "2": "economizar", "3": "solar", "4": "tarifa_social",
               "5": "ambiente", "6": "fontes", "0": "sair"}


# ------------------------------------------------------------------ respostas
def texto_calculo(minutos: float, pessoas: int) -> str:
    """
    Ajustes 5 e 6 (testes com usuários): um valor em reais por linha, economia do banho curto
    em destaque, kWh só como explicação e aquecedor solar fora do resultado principal.
    """
    e = ce.estimar_para_usuario(minutos, pessoas, _premissas())
    p = "pessoa" if pessoas == 1 else "pessoas"
    linhas = [
        f"Sua casa: {pessoas} {p}, banho de {minutos:g} minutos.",
        "",
        f"GASTO HOJE: cerca de R$ {brl(e['reais_mes_atual'])} por mês só com o banho.",
        f"VOCÊ PODE ECONOMIZAR: cerca de R$ {brl(e['a_economia_reais_mes'])} por mês, sem gastar nada.",
    ]
    if minutos <= MINUTOS_A:
        linhas += ["Seu banho já é curto. Parabéns!",
                   "Como: deixe a chave do chuveiro na posição verão nos meses quentes."]
    else:
        linhas.append(f"Como: banho de até {MINUTOS_A} minutos e chave na posição verão nos meses quentes.")
    linhas += [
        "",
        f"(O banho gasta cerca de {e['kwh_mes_atual']} kWh por mês. kWh é a medida de energia "
        "que aparece na conta de luz. O valor em dinheiro é o R$.)",
        "Quer saber se um aquecedor solar vale a pena para a sua casa? Digite 3.",
    ]
    return "\n".join(linhas)


def texto_solar_personalizado(minutos: float, pessoas: int) -> str:
    e = ce.estimar_para_usuario(minutos, pessoas, _premissas())
    pb_min, pb_max = e["b_payback_anos"]
    inv_min, inv_max = e["b_investimento"]
    linhas = [
        f"PARA A SUA CASA ({pessoas} pessoas, banho de {minutos:g} minutos):",
        f"- O aquecedor solar economizaria cerca de R$ {brl(e['b_economia_reais_mes'])} por mês.",
        f"- Ele custa de R$ {brl(inv_min)} a R$ {brl(inv_max)} e se paga em {anos(pb_min)} a {anos(pb_max)} anos.",
    ]
    if pb_max > 15:
        linhas.append("- No seu caso ele pode demorar mais que a vida útil para se pagar.")
    return "\n".join(linhas)


TEXTOS = {
    "economizar": (
        "Duas atitudes que não custam nada:\n"
        "1. Banho de até 5 minutos.\n"
        "2. Chave do chuveiro na posição verão nos meses quentes (outubro a março). "
        "Ela gasta de 30% a 40% menos que a posição inverno.\n"
        "Para 3 pessoas, isso economiza cerca de 59% do gasto com o banho: perto de R$ 49 por mês. "
        "E ainda poupa cerca de 21 mil litros de água por ano.\n"
        "Quer o cálculo para a sua casa? Diga quantos minutos dura o banho e quantas pessoas moram com você."
    ),
    # Ajuste 8 (testes com usuários): resposta curta e condições PRIMEIRO; detalhes depois.
    "solar": (
        "RESPOSTA CURTA: o aquecedor solar só vale a pena se você tem CASA PRÓPRIA, "
        "telhado sem sombra e dinheiro ou crédito para investir.\n"
        "Se você mora de aluguel ou em apartamento, o melhor é o banho curto (opção 2).\n"
        "\n"
        "Detalhes:\n"
        "- Ele esquenta a água com a luz do sol. O chuveiro elétrico fica só de apoio.\n"
        "- Economiza cerca de R$ 59 por mês para 3 pessoas.\n"
        "- Custa de R$ 2.300 a R$ 4.300, instalado. Se paga em 3 a 6 anos.\n"
        "- Para quem já toma banho curto, demora mais: de 8 a 15 anos.\n"
        "Antes de comprar, peça orçamento a instaladores."
    ),
    "moradia": (
        "RESPOSTA CURTA: para quem mora de aluguel ou em apartamento, o aquecedor solar é difícil. "
        "O melhor é mudar o hábito, que não custa nada.\n"
        "\n"
        "Por quê: precisa da autorização do dono ou do condomínio, e o aparelho fica no imóvel.\n"
        "O que fazer:\n"
        "1. Banho de até 5 minutos.\n"
        "2. Chave do chuveiro na posição verão nos meses quentes.\n"
        "Isso economiza cerca de 59% do gasto com o banho."
    ),
    # Ajuste 9 (testes com usuários): uma frase primeiro, siglas explicadas, sem "CDE".
    "tarifa_social": (
        "RESPOSTA CURTA: se sua família está no CadÚnico e tem renda baixa, você pode ter direito à "
        "TARIFA SOCIAL. Com ela, a energia é grátis até 80 kWh por mês.\n"
        "ONDE PROCURAR: na sua distribuidora de energia (a empresa da conta de luz). "
        "Se ainda não está no CadÚnico, procure o CRAS da sua cidade.\n"
        "\n"
        "Detalhes:\n"
        "- CadÚnico é o cadastro do governo para programas sociais.\n"
        "- Tem direito quem ganha até meio salário mínimo por pessoa da casa, "
        "ou tem alguém que recebe o BPC (benefício para idosos e pessoas com deficiência).\n"
        "- Quem ganha até 1 salário mínimo por pessoa tem um desconto menor.\n"
        "- O que passar de 80 kWh é cobrado. Por isso, banho curto continua ajudando.\n"
        "Não informe CPF, NIS ou renda aqui. Este assistente não consulta cadastros."
    ),
    # Ajuste 4 (testes com usuários): "minha conta está cara" ganha resposta própria.
    "conta_alta": (
        "Conta de luz cara? Duas coisas podem ajudar:\n"
        "1. DESCONTO: se sua família está no CadÚnico e tem renda baixa, você pode ter direito à "
        "Tarifa Social. Procure a sua distribuidora de energia. Para saber mais, digite 4.\n"
        "2. BANHO: o chuveiro é um dos aparelhos que mais gastam. Banho de até 5 minutos e posição verão "
        "podem cortar mais da metade desse gasto. Para calcular na sua casa, digite 1."
    ),
    "ambiente": (
        "A eletricidade do Brasil vem principalmente de fontes renováveis, como hidrelétricas, vento e sol. "
        "Por isso, economizar no banho evita pouco CO₂: de 22 a 33 kg por ano para 3 pessoas.\n"
        "O ganho maior é outro: o chuveiro liga muito no fim da tarde, o horário de pico. "
        "Usar menos energia nesse horário ajuda a evitar usinas extras, que costumam poluir mais.\n"
        "O banho curto também economiza água."
    ),
    "fontes": (
        "Os números vêm de dados públicos de São Paulo, consultados em 13/11/2026: "
        "IBGE, ANEEL, Lei 15.235/2025, norma NBR 15569, Idec e MCTI.\n"
        "Limitações:\n"
        "- São médias: chuveiro de 5.500 W e tarifa de cerca de R$ 1,02 por kWh (Enel SP), sem bandeira tarifária.\n"
        "- O seu chuveiro, os seus hábitos e a sua distribuidora mudam o resultado.\n"
        "- Não cobrimos placas fotovoltaicas, aquecimento a gás nem outros aparelhos."
    ),
    "fora_escopo": (
        "Desculpe, essa análise cobre só o banho com chuveiro elétrico e o aquecedor solar de água. "
        "Não tenho informações verificadas sobre esse assunto.\n"
        "Para outros aparelhos, consulte a sua distribuidora de energia ou o Procel (selo de eficiência)."
    ),
    "injecao": (
        "Não posso mudar minhas regras nem mostrar minhas instruções internas. "
        "Os valores que eu informo vêm só da ficha FC-08.\n"
        "Posso ajudar com o gasto do banho e formas de economizar."
    ),
    "oficial": (
        "Não. Este assistente é um protótipo educacional, não é um canal oficial. "
        "Confirme sempre com a sua distribuidora de energia ou com o órgão responsável."
    ),
}


# ------------------------------------------------------------------ função principal
def responder(mensagem: str, estado: dict | None = None) -> tuple[str, dict]:
    """
    Recebe a mensagem do usuário e o estado da conversa (só minutos e pessoas, nunca o texto).
    Devolve (resposta, novo_estado). Não guarda a mensagem.
    """
    estado = dict(estado or {})

    if mensagem is None or not mensagem.strip():
        return "Sua mensagem veio vazia. " + MENU, estado
    if len(mensagem) > LIMITE_CARACTERES:
        return (f"Sua mensagem ficou muito longa (mais de {LIMITE_CARACTERES} caracteres). "
                "Pode resumir em uma frase curta?"), estado

    texto, dados = proteger_dados(mensagem)
    aviso = ""
    if dados:
        aviso = ("Atenção: por segurança, removi da sua mensagem o que parecia ser "
                 f"{', '.join(dados)}. Não envie dados pessoais aqui. Eu não preciso deles.\n\n")

    t = extenso_para_digitos(normalizar(texto).strip())
    solto = numero_solto(t)
    respondendo_pergunta = bool(estado.get("aguardando")) and solto is not None and t != "0"

    # Se o assistente perguntou "quantas pessoas?" e o usuário digitou "4",
    # o "4" é a resposta, não a opção 4 do menu.
    if respondendo_pergunta:
        intencao = "nao_entendi"
    else:
        intencao = OPCOES_MENU.get(t) or ("sair" if t == "sair" else detectar_intencao(t))
    if intencao == "sair":
        return "Até logo! Lembre-se: banho curto economiza energia e água.", {}

    minutos = extrair_minutos(t)
    pessoas = extrair_pessoas(t)

    # Resposta a uma pergunta pendente ("Quantos minutos?" -> "10")
    if respondendo_pergunta:
        if estado["aguardando"] == "minutos":
            minutos = solto
        else:
            pessoas = int(solto)
        intencao = "calcular"
    if minutos is not None or pessoas is not None:
        if intencao in ("nao_entendi", "menu", "economizar"):
            intencao = "calcular"

    if intencao == "calcular":
        minutos = minutos if minutos is not None else estado.get("minutos")
        pessoas = pessoas if pessoas is not None else estado.get("pessoas")
        if minutos is not None and not (1 <= minutos <= 60):
            return aviso + "O tempo de banho precisa estar entre 1 e 60 minutos. Quantos minutos dura o banho?", \
                {"aguardando": "minutos", "pessoas": pessoas}
        if pessoas is not None and not (1 <= pessoas <= 15):
            return aviso + "O número de pessoas precisa estar entre 1 e 15. Quantas pessoas moram na casa?", \
                {"aguardando": "pessoas", "minutos": minutos}
        if minutos is None:
            return aviso + "Para calcular, quantos minutos dura cada banho, em média?", \
                {"aguardando": "minutos", "pessoas": pessoas}
        if pessoas is None:
            return aviso + "E quantas pessoas tomam banho na casa?", \
                {"aguardando": "pessoas", "minutos": minutos}
        # Guarda só minutos e pessoas (não são dados pessoais) para a opção 3 personalizar o cálculo.
        return aviso + texto_calculo(minutos, pessoas) + RODAPE, {"minutos": minutos, "pessoas": pessoas}

    casa = {k: estado[k] for k in ("minutos", "pessoas") if estado.get(k) is not None and not estado.get("aguardando")}
    if intencao == "solar" and len(casa) == 2:
        return (aviso + TEXTOS["solar"] + "\n\n" + texto_solar_personalizado(casa["minutos"], casa["pessoas"])
                + RODAPE), casa

    if intencao in TEXTOS:
        rodape = "" if intencao in ("injecao", "oficial") else RODAPE
        return aviso + TEXTOS[intencao] + rodape, casa

    if intencao == "menu":
        return aviso + MENU, casa

    return aviso + ("Desculpe, não entendi. Pode escrever de outro jeito?\n"
                    "Exemplo: \"Banho de 10 minutos, somos 4 pessoas\".\n\n" + MENU), {}


# ------------------------------------------------------------------ uso pelo terminal
def main():
    print(MENU)
    estado: dict = {}
    while True:
        try:
            msg = input("\nVocê: ")
        except (EOFError, KeyboardInterrupt):
            print("\nAté logo!")
            break
        resposta, estado = responder(msg, estado)
        print("\nAssistente:\n" + resposta)
        if normalizar(msg).strip() in ("0", "sair"):
            break


if __name__ == "__main__":
    main()
