# Atividade 1: especificação revisada

Disciplina: D1.3 Prompting Técnico, Especificação e Contexto · Individual · Peso 40% · Prazo: 11/11/2026, 23h59 · Professor: Victor Hugo Wanderley Freire

O prazo terminou. Este enunciado detalha o pedido da antiga AV2, sem exigência nova. Quem entregou não refaz nem reorganiza: a correção olha o conteúdo, não o nome dos arquivos.

## Objetivo

Revisar a especificação v1 da aula 3 a partir da devolutiva do colega, escrever a v2 com duas partes de trabalho e mostrar como conferir cada critério.

## Vínculo com a aula

- aula 3, conceitos necessidade, origem, especificação e casos, slides 3 a 14;
- aula 3, demonstração dos slides 21 e 22: a mesma tarefa com especificação vaga e com especificação completa;
- [prática da aula 3](../exercicios/aula-3/README.md): a v1 e a execução pelo colega, que é a sua devolutiva;
- seção "Partes do trabalho" do modelo de especificação, mostrada no anúncio desta atividade. A aula 4 aprofunda a divisão em partes.

## Ponto de partida

- `especificacao-v1.md` e `resposta-colega.md` da sua pasta `entregas/seu-nome/aula-3/`;
- regras em `caso/regras.md` e decisões em `caso/decisoes-confirmadas.md`, para quem usou o caso Fila Clara;
- modelos de [especificação](../modelos/especificacao.md) e de [histórico](../modelos/historico.md);
- o que você escreve: a v2, o histórico e a conferência dos critérios.

## Entrada

A sua especificação v1 e a devolutiva do colega: os critérios que ele marcou como "não passou" ou não conseguiu conferir.

## Saída esperada

Na pasta `entregas/seu-nome/atividade-1/`:

| Arquivo | Conteúdo |
|---|---|
| `especificacao-v1.md` | a v1 da aula 3, sem alteração |
| `especificacao-v2.md` | a v2 no modelo, com todas as seções, inclusive "Partes do trabalho" |
| `historico.md` | as linhas v1 e v2 do modelo e, abaixo da tabela, uma sugestão da IA aceita e uma rejeitada, com motivo |
| `evidencias.md` | a devolutiva do colega e o resultado da conferência de cada critério da v2 |

A v2 e o histórico somam até duas páginas. A v1 e as evidências são anexos.

## Critério de pronto

- [ ] a v2 tem objetivo, entradas, limites, formato de saída e critérios de aceite;
- [ ] cada critério diz a entrada, o resultado esperado e como conferir, e permite marcar passou ou não passou;
- [ ] um dos critérios é um caso de fronteira;
- [ ] a v2 tem 2 partes, cada uma com entrada, saída e critério próprio, e a coluna "Depende de" preenchida;
- [ ] o histórico liga 1 mudança da v2 a um ponto da devolutiva e à conferência feita depois;
- [ ] o histórico aponta 1 sugestão da IA aceita e 1 rejeitada ou desnecessária, com motivo, ou diz o que você conferiu antes de aceitar todas;
- [ ] a v2 e o histórico cabem em 2 páginas.

## Tempo estimado

2h de estudo autônomo, a carga prevista no plano de ensino. A divisão por passo é planejada e não foi cronometrada.

## Passos

1. Releia a v1 e a devolutiva. Marque cada critério que falhou ou que o colega não conseguiu conferir (20min).
2. Reescreva a especificação como v2 no modelo. Mude o que a devolutiva apontou (40min).
3. Preencha "Partes do trabalho" com 2 partes: entrada, saída e critério de cada uma, e de qual parte a segunda depende (25min).
4. Confira cada critério da v2 contra as regras, no Claude Code ou por inspeção manual. Anote o resultado em `evidencias.md` (25min).
5. Registre no histórico o que mudou, o motivo e o que você conferiu depois (10min).

O Claude Code pode revisar a v2. Ele aponta problemas; você decide o que aceitar e registra o motivo. Pedido de revisão, opcional:

```text
Leia especificacao-v2.md e caso/regras.md. Aponte critérios que outra pessoa não conseguiria conferir e regras que a especificação contradiz. Separe problema confirmado de sugestão. Não altere arquivos.
```

## Plano B

- sem acesso ao Claude Code: confira os critérios à mão contra as regras e marque "inspeção manual" em `evidencias.md`;
- sem v1 ou sem devolutiva, por falta na aula 3: use o rascunho C de [apoio/contingencia.md](../apoio/contingencia.md) como v1 e a crítica pelos critérios como devolutiva, marcadas como "simulação";
- entrega perdida por motivo justo e comprovado: siga a seção "Ausência, parceiro e dificuldade de acesso" da [avaliação](../avaliacao.md).

## Extensão opcional

- descreva a saída esperada em JSON e indique uma verificação de formato e outra de conteúdo. Não vale ponto extra.

## Pré-requisitos

- prática da aula 3: especificação v1 executada por um colega;
- modelo de especificação lido, com as seções que ele pede.

## Critérios da nota

Cada critério recebe nível 0, 1 ou 2. O [cálculo](../avaliacao.md) transforma os níveis em nota de 0 a 10.

| Critério | Peso |
|---|---:|
| Objetivo, entradas, limites e formato estão claros | 25% |
| Critérios distinguem acerto/erro e incluem um caso de fronteira | 35% |
| Duas partes podem ser conferidas e a dependência está explícita | 20% |
| Histórico liga uma mudança à devolutiva e a uma nova verificação | 20% |

## Entrega

Envie a pasta `atividade-1/` pelo canal de entrega da disciplina indicado pelo professor.
