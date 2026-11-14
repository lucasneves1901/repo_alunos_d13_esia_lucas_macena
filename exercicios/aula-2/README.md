# Prática da aula 2: Três formas de pedir a mesma classificação

Disciplina: D1.3 Prompting Técnico, Especificação e Contexto · Encontro: 07/11/2026, 9h · Professor: Victor Hugo Wanderley Freire

## Objetivo

Comparar pedido direto, pedido com exemplos e revisão na mesma tarefa e escolher uma técnica pelos acertos, pela variação e pelo esforço.

## Vínculo com a aula

- conceitos pedido direto, exemplos e revisão, slides 3 a 11;
- demonstração dos slides 21 e 22: o caso P1 a P4 com e sem exemplos, descrito em `apoio/protocolo-tecnicas.md`;
- prática acompanhada do slide 23: a primeira linha da ficha, preenchida com o professor.

## Ponto de partida

- `entrada.md` e `protocolo.md` da prática, enviados pelo professor no chat; eles trazem as descrições D1 a D8 e os três pedidos prontos;
- ficha `registro.md` desta pasta;
- o que você produz: as respostas da sua dupla, os acertos e a sua escolha de técnica.

## Entrada

As descrições D1 a D8 de `entrada.md`. A política de classificação da equipe chega no chat depois das execuções, para a conferência.

## Saída esperada

Na pasta `entregas/seu-nome/aula-2/`:

- `respostas.md`, com a resposta de cada tentativa da dupla, na ordem em que rodou;
- `registro.md`, com a tabela do grupo e a sua escolha.

## Critério de pronto

- [ ] a dupla rodou a sua técnica 2 vezes em cada modelo, sempre numa conversa nova;
- [ ] cada tentativa tem acertos de 0 a 8, contados contra a política;
- [ ] a tabela do grupo tem as 3 técnicas nos 2 modelos;
- [ ] a escolha cita os acertos, a diferença entre as tentativas e o número de chamadas;
- [ ] campo sem medida está como N/D, nunca como zero.

## Tempo estimado

91 minutos em aula: 25 de prática acompanhada, 8 para entrar na sala, 52 em grupo e 6 para o registro.

## Passos

1. Com o professor, preencha a primeira linha da ficha.
2. Na sala, cada dupla assume uma técnica: A, pedido direto; B, exemplos; C, revisão.
3. Copie `entrada.md` para uma pasta nova, fora do kit, e inicie o Claude Code nela.
4. Rode o pedido da sua técnica 2 vezes no modelo A e 2 vezes no modelo B. Abra uma conversa nova a cada tentativa. Na técnica C, os dois pedidos ficam na mesma conversa.
5. Quando o professor liberar a política no chat, conte os acertos. Junte as três duplas na tabela do grupo e escreva a sua escolha.

## Plano B

- só um modelo disponível: rode as 4 tentativas nele e marque o modelo B como N/D; o professor mostra a comparação entre modelos;
- sem acesso ao Claude Code: confira as respostas da dupla vizinha e marque "execução observada";
- a conta não mostra consumo: registre o número de chamadas e o tempo no relógio.

## Extensão opcional

- rode uma terceira tentativa da sua técnica e veja se a variação muda. Não vale ponto extra.

## Pré-requisitos

- prática da aula 1: pedido com tarefa, informações e formato;
- trocar de modelo com `/model` e abrir conversa nova com `/clear`.

## Entrega

A prática não tem nota nem prazo. Guarde os arquivos e o registro: as duas atividades avaliativas de [avaliacao.md](../../avaliacao.md) partem deles.
