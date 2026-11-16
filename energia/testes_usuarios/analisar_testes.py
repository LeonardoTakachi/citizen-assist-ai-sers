"""
Resume os testes com usuários e gera resultados_testes.md.
Rodar dentro da pasta testes_usuarios/:   python analisar_testes.py

Lê ficha_registro.csv (tarefas) e questionario.csv (compreensão e notas 1-5).
Linhas sem tempo ou sem nota são ignoradas, então dá para rodar com os testes pela metade.
"""

import csv
from pathlib import Path
from statistics import mean

PASTA = Path(__file__).resolve().parent
TAREFAS = {"T1": "Gasto do banho", "T2": "Aquecedor solar (aluguel)", "T3": "Desconto na conta"}
COMPREENSAO = {"C1": "Atitude sem custo", "C2": "Valores são estimativas", "C3": "Para quem o solar faz sentido",
               "C4": "Não é canal oficial"}
AFIRMACOES = {"Q1": "Fácil de usar", "Q2": "Entendi sem ajuda", "Q3": "Dicas úteis",
              "Q4": "Confio nos números", "Q5": "Indicaria"}


def ler(nome):
    with open(PASTA / nome, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def certo(valor: str) -> bool | None:
    v = (valor or "").strip().lower()
    if v in ("certo", "c", "sim", "s", "1", "acertou"):
        return True
    if v in ("errado", "e", "nao", "não", "n", "0", "errou"):
        return False
    return None


def fmt(x, casas=1):
    return f"{x:.{casas}f}".replace(".", ",")


def main():
    ficha = ler("ficha_registro.csv")
    quest = ler("questionario.csv")
    linhas = ["# Resultados dos testes com usuários", ""]

    participantes = sorted({l["participante"] for l in ficha if l["tempo_s"].strip()})
    linhas += [f"Participantes com dados: **{len(participantes)}** ({', '.join(participantes) or 'nenhum'}). "
               "Nenhum dado pessoal foi registrado.", ""]

    # --- tarefas
    linhas += ["## Tarefas", "", "| Tarefa | Tempo médio | Concluiu sozinho | Com ajuda | Não concluiu | Usou menu |",
               "|---|---|---|---|---|---|"]
    for t, nome in TAREFAS.items():
        dados = [l for l in ficha if l["tarefa"] == t and l["tempo_s"].strip()]
        if not dados:
            linhas.append(f"| {t} {nome} | — | — | — | — | — |")
            continue
        tempos = [float(l["tempo_s"].replace(",", ".")) for l in dados]
        conta = lambda v: sum(1 for l in dados if l["concluiu"].strip().lower().replace("ã", "a") == v)
        menu = sum(1 for l in dados if "menu" in l["usou_menu_ou_texto"].lower())
        n = len(dados)
        linhas.append(f"| {t} {nome} | {fmt(mean(tempos), 0)} s | {conta('sim')}/{n} | {conta('com ajuda')}/{n} "
                      f"| {conta('nao')}/{n} | {menu}/{n} |")

    # --- compreensão
    linhas += ["", "## Compreensão", "", "| Pergunta | Acertos |", "|---|---|"]
    for c, nome in COMPREENSAO.items():
        respostas = [certo(l[c]) for l in quest if certo(l[c]) is not None]
        linhas.append(f"| {c} {nome} | {sum(respostas)}/{len(respostas)} |" if respostas else f"| {c} {nome} | — |")

    # --- notas
    linhas += ["", "## Notas (1 a 5)", "", "| Afirmação | Média | Menor | Maior |", "|---|---|---|---|"]
    todas = []
    for q, nome in AFIRMACOES.items():
        notas = [float(l[q]) for l in quest if l[q].strip()]
        todas += notas
        linhas.append(f"| {q} {nome} | {fmt(mean(notas))} | {min(notas):g} | {max(notas):g} |"
                      if notas else f"| {q} {nome} | — | — | — |")
    if todas:
        linhas += ["", f"**Média geral: {fmt(mean(todas))} de 5.**"]

    # --- comentários
    linhas += ["", "## Comentários e travadas", ""]
    for l in ficha:
        texto = "; ".join(x for x in (l["travadas"].strip(), l["comentario"].strip()) if x)
        if texto:
            linhas.append(f"- {l['participante']}, {l['tarefa']}: {texto}")
    for l in quest:
        for campo, rotulo in (("o_que_ficou_confuso", "confuso"), ("o_que_faltou", "faltou")):
            if l[campo].strip():
                linhas.append(f"- {l['participante']} ({rotulo}): {l[campo].strip()}")

    linhas += ["", "Ajustes feitos a partir destes resultados: ver `registro_ajustes.md`."]
    (PASTA / "resultados_testes.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print("\n".join(linhas))


if __name__ == "__main__":
    main()
