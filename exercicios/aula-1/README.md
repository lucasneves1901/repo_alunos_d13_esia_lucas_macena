# Atividade 1: Um pedido que o colega consegue usar

Disciplina: D1.3 Prompting Técnico, Especificação e Contexto · Encontro: 06/11/2026, 19h · Professor: Victor Hugo Wanderley Freire

## Objetivo

Escrever um pedido que o colega executa no Claude Code sem explicação oral e revisar o pedido a partir do que faltou.

## Vínculo com a aula

- conceitos tarefa, contexto, formato e critério, slides 3 a 14;
- demonstração dos slides 21 e 22: o mesmo pedido, primeiro vago e depois explícito;
- prática acompanhada do slide 23: a primeira tentativa, feita com o professor.

## Ponto de partida

- modelo `modelos/pedido.md`, com cinco campos: tarefa, informações, limites, formato e conferência;
- caso Fila Clara em `caso/regras.md` e `caso/demandas.md`;
- o que você escreve: pedido v1, pedido v2 e registro.

## Entrada

Um pedido seu, de trabalho, sem dado de cliente, segredo ou credencial. Quem não tiver um pedido assim usa a demanda B de `caso/demandas.md`.

## Saída esperada

Na pasta `entregas/seu-nome/aula-1/`:

- `pedido-v1.md` e `pedido-v2.md`;
- `resposta-v2.md`, com a resposta do Claude Code ao pedido v2;
- `registro.md`, copiado desta pasta e preenchido.

## Critério de pronto

- [ ] o pedido v2 tem os cinco campos do modelo preenchidos;
- [ ] o colega executou o v1 e você anotou pelo menos uma lacuna que ele encontrou;
- [ ] o v2 resolve essa lacuna, e a mudança aparece quando se comparam os dois arquivos;
- [ ] você conferiu um critério do v2 na resposta e anotou o trecho que comprova;
- [ ] o registro tem as quatro seções preenchidas.

## Tempo estimado

81 minutos em aula: 25 de prática acompanhada, 8 para entrar na sala, 42 em dupla e 6 para o registro.

## Passos

1. Com o professor, preencha o modelo para a demanda B e faça uma tentativa com o pedido de partida abaixo.
2. Na sala, salve seu pedido v1. Passe ao colega só o texto e os arquivos que o pedido cita.
3. O colega executa no Claude Code sem perguntar nada e diz o que precisou supor. Troquem os papéis.
4. Escreva o v2 com o que faltou. Execute o v2 e confira um critério.
5. Preencha o registro.

Pedido de partida:

```text
Leia caso/regras.md. Explique R2 para uma pessoa nova no suporte, em até 80 palavras. Inclua os estados ativos e um exemplo que exclua fechado, preservando a ordem. Não acrescente prazo de atendimento. Não altere arquivos.
```

## Plano B

- sem acesso ao Claude Code: acompanhe a execução do colega na tela compartilhada e marque "execução observada" no registro;
- sem colega na sala: o professor forma um trio ou indica um revisor;
- sem nenhuma execução possível: use as respostas de `apoio/contingencia.md` e marque "simulação".

## Extensão opcional

- adapte o v2 para uma pessoa que entra hoje no time, sem mudar os critérios. Não vale ponto extra.

## Pré-requisitos

- abrir uma pasta no terminal e iniciar o Claude Code com `claude`, como mostra `guia-claude-code.md`;
- salvar um arquivo `.md` no editor.

## Entrega

O registro vale para a AV1, com a rubrica de [avaliacao.md](../../avaliacao.md). Prazo: 23h59 do dia do encontro, horário de Brasília.
