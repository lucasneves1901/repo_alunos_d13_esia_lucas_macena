# Atividade 6: Um CLAUDE.md que o colega segue e confere

Disciplina: D1.3 Prompting Técnico, Especificação e Contexto · Encontro: 14/11/2026, 14h · Professor: Victor Hugo Wanderley Freire

## Objetivo

Escrever as instruções persistentes de um projeto, revisá-las com um colega e mostrar, com um caso antes e depois, o que a revisão mudou.

## Vínculo com a aula

- conceitos documento, seleção, leitura, revisão e regressão, slides 3 a 17;
- demonstração dos slides 21 e 22: a mesma tarefa com um CLAUDE.md vago e com um verificável;
- prática acompanhada do slide 23: o modelo preenchido com uma regra, um limite e uma conferência.

## Ponto de partida

- modelos `modelos/CLAUDE-modelo.md`, `modelos/historico.md` e `modelos/verificacao.md`;
- orientação de versões em `apoio/versionamento.md`;
- o que você escreve: CLAUDE.md v1 e v2, histórico e um caso conferido.

## Entrada

Um recorte compartilhável do seu projeto, sem segredo nem dado de cliente, ou o caso Fila Clara.

## Saída esperada

Na pasta `entregas/seu-nome/aula-6/`:

- `v1/CLAUDE.md` e `v2/CLAUDE.md`;
- `historico.md`, com a linha da v2;
- `verificacao.md`, com 1 caso conferido com v1 e com v2;
- `registro.md`.

## Critério de pronto

- [ ] o v1 tem a fonte da regra, 1 limite e 1 forma de conferir;
- [ ] o colega tentou seguir o v1 no Claude Code e anotou 1 instrução que não conseguiu seguir ou conferir;
- [ ] o v2 muda essa instrução, e o histórico diz o motivo;
- [ ] 1 caso conhecido tem o resultado com v1 e com v2;
- [ ] o CLAUDE.md não tem informação temporária, como prazo da semana ou tarefa do dia.

## Tempo estimado

91 minutos em aula: 25 de prática acompanhada, 8 para entrar na sala, 52 em dupla e 6 para o registro. Na sala, são 12 minutos para o v1, 16 para o teste do colega, 16 para o v2 e 8 para salvar.

## Passos

1. Com o professor, preencha o modelo com uma regra, um limite e uma conferência.
2. Numa pasta nova, `projeto-b6`, salve o v1 como `CLAUDE.md` e copie só os arquivos que ele cita.
3. O colega abre o Claude Code nessa pasta, envia o pedido de partida abaixo e anota o que não conseguiu seguir. Troquem os papéis.
4. Escreva o v2, registre o motivo no histórico e confira 1 caso com v1 e com v2.
5. Preencha o registro e salve as execuções. A v3 e os outros dois casos ficam para a AV3.

Pedido de partida:

```text
Siga as instruções deste projeto. Proponha três casos de teste para a regra de prioridade, com entrada e resultado esperado. Diga quais arquivos leu e como conferiu cada caso. Não altere arquivos.
```

## Plano B

- sem projeto compartilhável: use o caso Fila Clara e o pedido de partida como está;
- sem acesso ao Claude Code: o colega lê o v1 e marca quais instruções conseguiria conferir, como "inspeção manual";
- dúvida se o CLAUDE.md foi carregado: confira com `/memory` e anote o que apareceu.

## Extensão opcional

- liste o que conferir ao levar o documento para outra ferramenta, como `AGENTS.md`. Não vale ponto extra.

## Pré-requisitos

- atividade 3: critério de aceite que outra pessoa confere;
- atividade 5: separar informação duradoura de informação da tarefa.

## Entrega

O registro vale para a AV1, com a rubrica de [avaliacao.md](../../avaliacao.md). Prazo: 23h59 do dia do encontro, horário de Brasília.
