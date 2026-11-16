"""
Calculadora de energia do banho — Citizen Assist AI
Contribuição da disciplina Soluções em Energias Renováveis e Sustentáveis.

Este módulo é usado em dois lugares, para garantir que os números sejam os mesmos:
  1. no notebook 03_calculos.ipynb (análise completa);
  2. no assistente (etapa 5), que responde ao usuário com estas mesmas funções.

Todos os valores vêm de dados/premissas.csv (ver 02_dados_e_fontes.md).
Os resultados são ESTIMATIVAS, não valores garantidos.
"""

from __future__ import annotations

import csv
from pathlib import Path

PASTA = Path(__file__).resolve().parent
ARQUIVO_PREMISSAS = PASTA / "dados" / "premissas.csv"

MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

# Estação de cada mês (1 = janeiro), para variar a fração solar com o sol disponível
ESTACAO_DO_MES = {
    12: "verão", 1: "verão", 2: "verão",
    3: "outono", 4: "outono", 5: "outono",
    6: "inverno", 7: "inverno", 8: "inverno",
    9: "primavera", 10: "primavera", 11: "primavera",
}
ID_IRRADIACAO_ESTACAO = {"verão": "P24", "outono": "P25", "inverno": "P26", "primavera": "P27"}

# Alternativa A: posição verão de outubro a março (6 meses quentes, premissa P08)
MESES_POSICAO_VERAO = {10, 11, 12, 1, 2, 3}

FRACAO_SOLAR_MAXIMA = 0.95  # o sistema nunca cobre 100%: sempre há dias nublados


# ---------------------------------------------------------------- premissas
def carregar_premissas(caminho: Path = ARQUIVO_PREMISSAS) -> dict[str, dict]:
    """Lê o CSV de premissas. Valores numéricos viram float; faixas ('15 a 25') ficam como texto."""
    premissas = {}
    with open(caminho, encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            try:
                linha["valor"] = float(linha["valor"])
            except ValueError:
                pass
            premissas[linha["id"]] = linha
    return premissas


def v(premissas: dict, id_: str) -> float:
    """Valor numérico de uma premissa."""
    return premissas[id_]["valor"]


# ---------------------------------------------------------------- física básica
def energia_banho_kwh(potencia_w: float, minutos: float) -> float:
    """Energia (kWh) = Potência (kW) × Tempo (h)."""
    return (potencia_w / 1000) * (minutos / 60)


def energia_mensal_kwh(potencia_w: float, minutos: float, pessoas: float,
                       banhos_por_dia: float = 1, dias: float = 30) -> float:
    return energia_banho_kwh(potencia_w, minutos) * pessoas * banhos_por_dia * dias


def litros_aquecidos(energia_kwh: float, calor_especifico: float, delta_t: float) -> float:
    """Conferência física: Q = m·c·ΔT  ->  m = Q / (c·ΔT). 1 kg de água ≈ 1 litro."""
    energia_j = energia_kwh * 3.6e6
    return energia_j / (calor_especifico * delta_t)


def fracao_solar_do_mes(premissas: dict, mes: int) -> float:
    """Fração solar anual (P14) ajustada pelo sol de cada estação (P24-P27 / P20)."""
    anual = v(premissas, "P14") / 100
    estacao = ESTACAO_DO_MES[mes]
    proporcao = v(premissas, ID_IRRADIACAO_ESTACAO[estacao]) / v(premissas, "P20")
    return min(anual * proporcao, FRACAO_SOLAR_MAXIMA)


# ---------------------------------------------------------------- cenários
def cenarios_mensais(premissas: dict, pessoas: float | None = None,
                     minutos_base: float | None = None,
                     minutos_a: float | None = None) -> list[dict]:
    """kWh de cada mês para Base, Alternativa A e Alternativa B."""
    pessoas = pessoas if pessoas is not None else v(premissas, "P02")
    minutos_base = minutos_base if minutos_base is not None else v(premissas, "P04")
    minutos_a = minutos_a if minutos_a is not None else v(premissas, "P05")
    banhos = v(premissas, "P03")
    dias = v(premissas, "P09")
    pot_inverno = v(premissas, "P06")
    pot_verao = pot_inverno * (1 - v(premissas, "P07") / 100)

    linhas = []
    for mes in range(1, 13):
        base = energia_mensal_kwh(pot_inverno, minutos_base, pessoas, banhos, dias)
        pot_a = pot_verao if mes in MESES_POSICAO_VERAO else pot_inverno
        alt_a = energia_mensal_kwh(pot_a, minutos_a, pessoas, banhos, dias)
        f = fracao_solar_do_mes(premissas, mes)
        alt_b = base * (1 - f)  # o chuveiro elétrico só completa o que o sol não cobre
        alt_ab = alt_a * (1 - f)  # A + B: banho curto com aquecedor solar
        linhas.append({
            "mes": MESES[mes - 1],
            "estacao": ESTACAO_DO_MES[mes],
            "base_kwh": base,
            "a_kwh": alt_a,
            "b_kwh": alt_b,
            "ab_kwh": alt_ab,
            "fracao_solar_b": f,
        })
    return linhas


def resumo_anual(premissas: dict, tarifa: float | None = None, **kwargs) -> dict:
    """Totais de 12 meses: kWh, R$, kg de CO2, economia e payback da alternativa B."""
    tarifa = tarifa if tarifa is not None else v(premissas, "P11")
    fator_kg_por_kwh = v(premissas, "P19")  # t/MWh = kg/kWh
    meses = cenarios_mensais(premissas, **kwargs)

    resumo = {}
    for chave, nome in [("base", "Base"), ("a", "A - hábito"), ("b", "B - aquecedor solar"),
                        ("ab", "A+B - combinado")]:
        kwh = sum(m[f"{chave}_kwh"] for m in meses)
        resumo[chave] = {
            "cenario": nome,
            "kwh_ano": kwh,
            "reais_ano": kwh * tarifa,
            "kg_co2_ano": kwh * fator_kg_por_kwh,
        }
    for chave in ("a", "b", "ab"):
        r = resumo[chave]
        r["economia_kwh"] = resumo["base"]["kwh_ano"] - r["kwh_ano"]
        r["economia_reais"] = r["economia_kwh"] * tarifa
        r["economia_pct"] = 100 * r["economia_kwh"] / resumo["base"]["kwh_ano"]
        r["co2_evitado_kg"] = r["economia_kwh"] * fator_kg_por_kwh

    resumo["a"]["investimento_min"] = resumo["a"]["investimento_max"] = 0.0
    resumo["b"]["investimento_min"] = v(premissas, "P15")
    resumo["b"]["investimento_max"] = v(premissas, "P16")
    resumo["b"]["payback_min_anos"] = payback_anos(resumo["b"]["investimento_min"], resumo["b"]["economia_reais"])
    resumo["b"]["payback_max_anos"] = payback_anos(resumo["b"]["investimento_max"], resumo["b"]["economia_reais"])

    # A+B: o investimento é o mesmo de B. O payback "incremental" responde à pergunta:
    # "se a família JÁ mudou o hábito (A), ainda vale a pena comprar o aquecedor?"
    ab = resumo["ab"]
    ab["investimento_min"], ab["investimento_max"] = resumo["b"]["investimento_min"], resumo["b"]["investimento_max"]
    ganho_extra = (resumo["a"]["kwh_ano"] - ab["kwh_ano"]) * tarifa
    ab["economia_extra_sobre_a_reais"] = ganho_extra
    ab["payback_incremental_min_anos"] = payback_anos(ab["investimento_min"], ganho_extra)
    ab["payback_incremental_max_anos"] = payback_anos(ab["investimento_max"], ganho_extra)
    return resumo


def payback_anos(investimento: float, economia_anual: float) -> float:
    """Payback simples (sem juros e sem reajuste de tarifa)."""
    return float("inf") if economia_anual <= 0 else investimento / economia_anual


def custo_energia_tarifa_social(consumo_kwh_mes: float, tarifa: float, faixa_gratis: float = 80) -> float:
    """Lei 15.235/2025: até 80 kWh/mês a energia é gratuita; paga-se o excedente (só a parte de energia)."""
    return max(consumo_kwh_mes - faixa_gratis, 0) * tarifa


# ---------------------------------------------------------------- uso pelo assistente
def estimar_para_usuario(minutos: float, pessoas: int, premissas: dict | None = None) -> dict:
    """
    Estimativa para a pergunta do usuário. Recebe só minutos de banho e número de pessoas
    (nenhum dado pessoal). Devolve valores arredondados, prontos para a resposta do assistente.
    """
    premissas = premissas or carregar_premissas()
    if not (1 <= minutos <= 60):
        raise ValueError("minutos deve estar entre 1 e 60")
    if not (1 <= pessoas <= 15):
        raise ValueError("pessoas deve estar entre 1 e 15")

    minutos_a = min(minutos, v(premissas, "P05"))  # se já toma banho curto, não "piora"
    r = resumo_anual(premissas, pessoas=pessoas, minutos_base=minutos, minutos_a=minutos_a)
    return {
        "kwh_mes_atual": round(r["base"]["kwh_ano"] / 12),
        "reais_mes_atual": round(r["base"]["reais_ano"] / 12),
        "a_minutos": minutos_a,
        "a_economia_reais_mes": round(r["a"]["economia_reais"] / 12),
        "a_economia_pct": round(r["a"]["economia_pct"]),
        "b_economia_reais_mes": round(r["b"]["economia_reais"] / 12),
        "b_economia_pct": round(r["b"]["economia_pct"]),
        "b_investimento": (round(r["b"]["investimento_min"]), round(r["b"]["investimento_max"])),
        "b_payback_anos": (round(r["b"]["payback_min_anos"], 1), round(r["b"]["payback_max_anos"], 1)),
        "tarifa": v(premissas, "P11"),
        "potencia_w": v(premissas, "P06"),
    }


if __name__ == "__main__":
    pr = carregar_premissas()
    for k, r in resumo_anual(pr).items():
        print(k, {c: (round(x, 1) if isinstance(x, float) else x) for c, x in r.items()})
    print(estimar_para_usuario(10, 3, pr))
