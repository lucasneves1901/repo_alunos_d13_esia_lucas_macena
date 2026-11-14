"""Uso: python -m fila_clara listar --departamento Oficina"""
import argparse
import json
from pathlib import Path

from .regras import ativos, prioridade, visiveis

DADOS = Path(__file__).resolve().parent.parent / "dados" / "chamados.json"


def carregar(caminho=DADOS):
    return json.loads(Path(caminho).read_text(encoding="utf-8"))


def listar(chamados, departamento):
    return [f"{c['id']} | {prioridade(c['impacto'], c['urgencia'])}"
            for c in ativos(visiveis(chamados, departamento))]


def main(argv=None):
    parser = argparse.ArgumentParser(prog="fila_clara")
    comandos = parser.add_subparsers(dest="comando", required=True)
    lista = comandos.add_parser("listar", help="chamados ativos visíveis para um departamento")
    lista.add_argument("--departamento", required=True)
    lista.add_argument("--dados", default=DADOS)
    args = parser.parse_args(argv)
    for linha in listar(carregar(args.dados), args.departamento):
        print(linha)
