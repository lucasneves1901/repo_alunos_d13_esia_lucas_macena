# Guardar versões sem complicar

A AV3 pede três estados recuperáveis: v1 inicial, v2 depois da primeira revisão e v3 depois da segunda. Cada mudança tem motivo, revisor e nova conferência. Renomear arquivo sem mudar conteúdo não conta.

## Com pastas: disponível para todos

Crie `v1/`, `v2/` e `v3/` dentro da sua pasta de entrega. Guarde em cada uma os arquivos daquele momento. No `historico.md`, registre o que mudou e quais casos você conferiu de novo.

## Com Git: opcional

Use uma pasta nova, só da atividade, fora de qualquer repositório de trabalho. O professor mostra os comandos:

```text
git init
git add CLAUDE.md historico.md
git commit -m "Registra versao inicial"
git diff
git log --oneline
```

`git diff` mostra o que mudou desde a última versão guardada. Não é preciso publicar nem criar conta.

## O que é um pull request

É um pedido de revisão de uma mudança num repositório compartilhado. O autor explica a mudança e como conferiu; o colega comenta; o autor ajusta; o responsável integra. Na aula, a mesma conversa acontece por arquivo e devolutiva.

## Conferir depois de mudar

Repita três casos: um normal, um de fronteira e um de exclusão. Guarde o resultado antes e depois. Se o pedido e o modelo mudaram juntos, registre esse limite.
