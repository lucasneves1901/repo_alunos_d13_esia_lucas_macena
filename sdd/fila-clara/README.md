# Fila Clara: repositório do exercício de SDD

Projeto fictício em Python, só com a biblioteca padrão. Ele lista os chamados ativos visíveis para um departamento pelas regras R1, R2 e R3 de `docs/regras.md`. Os dados estão em `dados/chamados.json`.

## Rodar

```text
python -m fila_clara listar --departamento Oficina
python -m unittest
```

O primeiro comando mostra `T1 | alta`, `T4 | baixa` e `T6 | alta`. O segundo roda os 4 testes de `tests/`.

## O exercício

Você leva a demanda de `docs/demanda.md` do pedido ao código com o Spec Kit. As fases são constituição, especificação, esclarecimento, plano, tarefas e implementação. O passo a passo está no encontro de prática da D1.3.

Copie esta pasta para fora do kit antes de abrir o Claude Code. Dentro do kit, a sessão também carrega o `CLAUDE.md` do kit, que não pertence a este projeto. O passo precisa de Python 3, que roda os scripts do Spec Kit e os testes.

As pastas `.specify/` e `.claude/skills/` vêm do Spec Kit v1.4.0, do GitHub, instalado com `specify init --integration claude --script py`. A licença MIT do Spec Kit está em `LICENSE-spec-kit`.
