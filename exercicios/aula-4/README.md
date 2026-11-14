# Atividade 4: Dividir a demanda D e testar o corte

Disciplina: D1.3 Prompting Técnico, Especificação e Contexto · Encontro: 13/11/2026, 19h · Professor: Victor Hugo Wanderley Freire

## Objetivo

Dividir a demanda D em 2 a 4 unidades com entrada, saída e critério próprios e testar o corte executando 2 unidades do outro grupo.

## Vínculo com a aula

- conceitos resultado, unidades, dependências e verificação, slides 3 a 14;
- demonstração dos slides 21 e 22: U1 passa a regra para U2, que gera três casos de teste; primeiro com a passagem incompleta, depois corrigida;
- prática acompanhada do slide 23: U1 e U2 escritas no modelo, com o professor.

## Ponto de partida

- demanda D em `caso/demandas.md` e regras em `caso/regras.md`;
- modelo `modelos/decomposicao.md`;
- decisão do responsável em `caso/decisoes-confirmadas.md`, seção D, que o grupo abre só no passo 2;
- o que o grupo escreve: a decomposição. O que você executa: duas unidades do outro grupo.

## Entrada

A demanda D: "A supervisão da manutenção quer acompanhar os chamados de prioridade alta de todos os departamentos."

## Saída esperada

Na pasta `entregas/seu-nome/aula-4/`:

- `decomposicao.md`, a do seu grupo, com 2 a 4 unidades;
- `u1-saida.md` e `u2-saida.md`, com o que você produziu ao executar as duas unidades recebidas, ou a lacuna que impediu;
- `registro.md`.

## Critério de pronto

- [ ] cada unidade da decomposição tem entrada, saída, critério e dependência preenchidos;
- [ ] a decomposição marca a dúvida que pede decisão do responsável;
- [ ] as 2 unidades recebidas foram executadas e cada saída está salva em arquivo;
- [ ] se a segunda unidade depende da primeira, ela recebeu o arquivo `u1-saida.md`;
- [ ] o registro aponta 1 lacuna da passagem, ou o critério que mostrou que a passagem bastou.

## Tempo estimado

91 minutos em aula: 25 de prática acompanhada, 8 para entrar na sala, 52 em grupo e 6 para o registro. Na sala, são 14 minutos para dividir, 26 para executar e 12 para devolver.

## Passos

1. Com o professor, escreva U1 e U2 no modelo. Pergunta de apoio: qual arquivo sai de U1 e entra em U2?
2. Na sala, o grupo divide a demanda D em 2 a 4 unidades e marca a dúvida que exige decisão. Só então abre a seção D de `caso/decisoes-confirmadas.md`.
3. Envie a decomposição ao grupo seguinte: 1 para 2, 2 para 3, até 7 para 1. Receba a do grupo anterior, sem explicação oral.
4. Para cada uma das 2 unidades recebidas, abra uma conversa no Claude Code, cole o texto da unidade e envie o pedido de partida abaixo. Salve cada saída.
5. Devolva ao grupo autor 1 lacuna com evidência. Preencha o registro.

Pedido de partida:

```text
Execute apenas a unidade que forneci, com suas entradas e critérios. Não amplie o escopo. Se faltar uma dependência, liste a lacuna. Produza o artefato solicitado e indique como cada critério pode ser conferido. Não altere outros arquivos.
```

## Plano B

- o grupo não terminou a divisão no minuto 14: use as duas unidades de apoio, U1 escreve a regra da supervisão e U2 propõe três casos de teste para ela;
- a unidade recebida está incompleta: execute o que der e registre a lacuna, que é o resultado esperado do teste do corte;
- sem acesso ao Claude Code: faça a unidade à mão a partir de `caso/regras.md` e marque "inspeção manual".

## Extensão opcional

- compare uma divisão em 2 unidades e outra em 4 e diga onde o ganho de conferência compensa a coordenação. Não vale ponto extra.

## Pré-requisitos

- atividade 3: especificação com critérios de aceite;
- ler a tabela de prioridade e estados em `caso/regras.md`.

## Entrega

O registro vale para a AV1, com a rubrica de [avaliacao.md](../../avaliacao.md). Prazo: 23h59 do dia do encontro, horário de Brasília.
