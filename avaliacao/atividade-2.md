# Atividade 2: conjunto final de artefatos

Disciplina: D1.3 Prompting Técnico, Especificação e Contexto · Individual · Peso 60% · Prazo: 30/11/2026, 23h59 · Professor: Victor Hugo Wanderley Freire

## Objetivo

Reunir, revisar e conferir os artefatos das aulas 2 a 6 numa pasta versionada que outra pessoa consegue ler e conferir.

## Vínculo com a aula

| Item | Aula | Onde apareceu |
|---|---|---|
| Técnica escolhida | 2 | slides 3 a 11 e [prática da aula 2](../exercicios/aula-2/README.md) |
| Especificação | 3 | slides 3 a 14, [prática da aula 3](../exercicios/aula-3/README.md) e [Atividade 1](atividade-1.md) |
| Decomposição | 4 | slides 3 a 14, demonstração dos slides 21 e 22 e [prática da aula 4](../exercicios/aula-4/README.md) |
| Decisão de contexto | 5 | slides 3 a 14, demonstração dos slides 21 e 22 e [prática da aula 5](../exercicios/aula-5/README.md) |
| CLAUDE.md, versões e regressão | 6 | slides 3 a 17, demonstração dos slides 21 e 22, [prática da aula 6](../exercicios/aula-6/README.md) e [versionamento](../apoio/versionamento.md) |

## Ponto de partida

- suas pastas `entregas/seu-nome/aula-2/` a `aula-6/` e `atividade-1/`;
- modelos de [especificação](../modelos/especificacao.md), [decomposição](../modelos/decomposicao.md), [contexto](../modelos/contexto.md), [CLAUDE.md](../modelos/CLAUDE-modelo.md), [histórico](../modelos/historico.md) e [verificação](../modelos/verificacao.md);
- um recorte compartilhável de projeto real, sem segredo nem dado de cliente, ou o caso Fila Clara;
- o que você escreve: a revisão de cada artefato, a v3 e a nova conferência de três casos.

## Entrada

Os arquivos que você guardou nas práticas e na Atividade 1. A Atividade 2 não pede produto novo nem aplicação implementada.

## Saída esperada

Na pasta `entregas/seu-nome/atividade-2/`:

| Item | Arquivo | O que contém |
|---|---|---|
| 1 | `especificacao.md` | a v2 da Atividade 1, ou uma nova se você mudou de tarefa, com a técnica escolhida e o motivo |
| 2 | `decomposicao.md` | 2 a 4 partes com entrada, saída, responsável e conferência |
| 3 | `contexto.md` | o que entrou, o que saiu e em que ordem, com a evidência de 2 condições ou mais |
| 4 | `CLAUDE.md` | as instruções persistentes do projeto |
| 5 | `historico.md`, `v1/`, `v2/` e `v3/` | três versões recuperáveis e o motivo de cada revisão |
| 6 | `verificacao.md` | três casos conhecidos conferidos de novo |

Os itens 1 a 4 somam até quatro páginas de texto principal; histórico e evidências curtas ficam fora da conta. Arquivos Markdown bastam, sem apresentação. A regressão é uma conferência de três casos, sem framework de avaliação.

## Critério de pronto

- [ ] `especificacao.md` tem critérios de caso normal, de fronteira e de exclusão, cada um com a forma de conferir;
- [ ] `especificacao.md` nomeia a técnica (pedido direto, exemplos ou revisão), o resultado que motivou a escolha e 1 situação em que ela não ajuda;
- [ ] `decomposicao.md` tem de 2 a 4 partes, e a saída de uma parte aparece como entrada de outra;
- [ ] cada parte tem entrada, saída, critério, dependência e quem confere;
- [ ] `contexto.md` compara 2 condições ou mais na mesma tarefa, com qualidade, tempo e consumo, ou N/D com motivo;
- [ ] `CLAUDE.md` tem a fonte das regras, 1 forma de conferir e 1 limite, sem prazo nem tarefa do dia;
- [ ] `historico.md` tem as linhas v1, v2 e v3, cada uma com o que mudou, o motivo, quem revisou e o que foi conferido depois;
- [ ] `v2/` e `v3/` mudam o conteúdo da versão anterior, porque renomear arquivo não conta;
- [ ] `verificacao.md` tem os casos normal, fronteira e exclusão, com o resultado antes e depois da mudança;
- [ ] `verificacao.md` informa pedido, saída, modelo, data, origem do resultado, contribuição da IA e limite;
- [ ] nenhuma medida ausente aparece como número.

## Tempo estimado

2h de finalização, a carga de estudo autônomo prevista no plano de ensino. A divisão por passo é planejada e não foi cronometrada.

## Passos

1. Reúna na pasta da entrega os arquivos das práticas e da Atividade 1 (20min).
2. Corrija as lacunas que as devolutivas apontaram na especificação, na decomposição e no contexto (30min).
3. Escreva a v3 e confira de novo três casos: normal, fronteira e exclusão (30min).
4. Escreva a técnica escolhida em `especificacao.md` e a decisão de contexto em `contexto.md` (25min).
5. Organize a pasta, marque a lista do critério de pronto e envie (15min).

O caminho mais curto versiona o `CLAUDE.md`: a v1 e a v2 vêm da prática da aula 6, e a v3 sai aqui. Versionar a especificação também vale: v1 da aula 3, v2 da Atividade 1 e v3 aqui. Cada revisão tem um motivo registrado, que vem do colega, do professor ou de um caso conferido.

## Plano B

- sem Claude Code depois de 14/11: use as execuções guardadas até a aula 6, confira por inspeção manual e marque essa origem em `verificacao.md`;
- sem projeto compartilhável: use o caso Fila Clara e os arquivos das práticas;
- sem medida de tempo ou de consumo: escreva N/D e o motivo.

## Extensão opcional

- guarde as versões com Git, numa pasta só da atividade, e anexe a saída de `git log --oneline`;
- liste o que conferir ao levar o `CLAUDE.md` para outra ferramenta, como `AGENTS.md`.

Nenhuma extensão vale ponto extra.

## Pré-requisitos

- práticas das aulas 2 a 6, com os arquivos guardados;
- Atividade 1, que fornece a especificação v2.

## Critérios da nota

Cada critério recebe nível 0, 1 ou 2. O [cálculo](../avaliacao.md) transforma os níveis em nota de 0 a 10.

| Critério | Peso |
|---|---:|
| Especificação e critérios permitem conferir; partes se conectam | 25% |
| Técnica é escolhida por necessidade, com limite reconhecido | 15% |
| Decisão de contexto usa efeito observado e esforço/consumo | 20% |
| Instruções persistentes são úteis, específicas e conferíveis | 20% |
| Duas revisões e nova conferência mostram o que mudou | 20% |

## Entrega

Envie a pasta `atividade-2/` em .zip na tarefa “Atividade 2: conjunto final de artefatos” do Moodle da disciplina, até 30/11/2026, 23h59.
