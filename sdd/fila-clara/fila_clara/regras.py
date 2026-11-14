"""Regras R1, R2 e R3 de docs/regras.md."""

ESTADOS_ATIVOS = ("aberto", "em_andamento")


def prioridade(impacto, urgencia):
    soma = impacto + urgencia
    if soma >= 5:
        return "alta"
    if soma >= 3:
        return "media"
    return "baixa"


def ativos(chamados):
    return [c for c in chamados if c["estado"] in ESTADOS_ATIVOS]


def visiveis(chamados, departamento):
    return [c for c in chamados if c["departamento"] == departamento]
