# Atividade 3: Uma especificação que o colega executa sem perguntar

Disciplina: D1.3 Prompting Técnico, Especificação e Contexto · Encontro: 07/11/2026, 14h · Professor: Victor Hugo Wanderley Freire

## Objetivo

Transformar uma demanda vaga numa especificação curta, com três critérios de aceite, que o colega executa e confere sem conversa.

## Vínculo com a aula

- conceitos necessidade, origem, especificação e casos, slides 3 a 14;
- demonstração dos slides 21 e 22: a tabela da Oficina com especificação vaga e depois completa;
- prática acompanhada do slide 23: critérios de inclusão, exclusão e fronteira escritos com a turma.

## Ponto de partida

- demandas A e B em `caso/demandas.md` e regras em `caso/regras.md`;
- modelo `modelos/especificacao.md`;
- decisões do responsável em `caso/decisoes-confirmadas.md`, que você abre só no passo 3;
- o que você escreve: especificação v1, lista do que a IA acrescentou e registro.

## Entrada

A demanda A ou a demanda B de `caso/demandas.md`.

## Saída esperada

Na pasta `entregas/seu-nome/aula-3/`:

- `especificacao-v1.md`, com objetivo, entradas, limites, saída e três critérios;
- `resposta-colega.md`, com a resposta que o colega obteve ao executar a sua especificação;
- `registro.md`, com o que a IA acrescentou e o critério reescrito.

## Critério de pronto

- [ ] a especificação tem um critério de caso normal, um de fronteira e um de exclusão;
- [ ] cada critério cita a regra R1, R2 ou R3, ou a decisão, que o sustenta;
- [ ] o registro lista pelo menos 1 acréscimo da IA, ou diz quais regras você conferiu sem achar acréscimo;
- [ ] o colega executou a especificação e marcou cada critério como passou ou não passou;
- [ ] você reescreveu 1 critério que o colega não conseguiu conferir.

## Tempo estimado

91 minutos em aula: 25 de prática acompanhada, 8 para entrar na sala, 52 em dupla e 6 para o registro.

## Passos

1. Com o professor, escreva os três critérios da demanda B.
2. Rodada 1: peça ao Claude Code uma história e três critérios para a demanda escolhida, com o pedido de partida abaixo.
3. Só depois abra `caso/decisoes-confirmadas.md` e marque o que a IA acrescentou.
4. Preencha o modelo como v1. A seção "Partes do trabalho" é opcional em aula.
5. Rodada 2: troque a especificação com o colega. Ele executa só o que está escrito e marca cada critério. Troquem os papéis. Depois, reescreva o critério que falhou.

Pedido de partida:

```text
Leia caso/regras.md e a demanda escolhida de caso/demandas.md. Proponha uma história de usuário e três critérios observáveis. Separe fatos confirmados, sugestões suas e dúvidas. Não acrescente regra como se estivesse aprovada. Não altere arquivos.
```

## Plano B

- sem acesso ao Claude Code: o colega confere a especificação à mão contra `caso/regras.md` e marca "inspeção manual";
- sem colega na sala: o professor forma um trio ou indica um revisor;
- sem nenhuma execução possível: analise o rascunho C de `apoio/contingencia.md` e marque "simulação".

## Extensão opcional

- escreva a saída em JSON e indique uma verificação de formato e outra de conteúdo. Não vale ponto extra.

## Pré-requisitos

- atividade 1: pedido com os cinco campos.

## Entrega

A prática não tem nota nem prazo. Guarde os arquivos e o registro: as duas atividades avaliativas de [avaliacao.md](../../avaliacao.md) partem deles.
