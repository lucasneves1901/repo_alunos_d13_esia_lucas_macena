# Atividade 5: Quatro contextos para a mesma pergunta

Disciplina: D1.3 Prompting Técnico, Especificação e Contexto · Encontro: 14/11/2026, 9h · Professor: Victor Hugo Wanderley Freire

## Objetivo

Comparar quatro montagens de contexto na mesma pergunta e escolher o menor contexto suficiente, com evidência de qualidade, tamanho e tempo.

## Vínculo com a aula

- conceitos seleção, ruído, ordem e orçamento, slides 3 a 14;
- demonstração dos slides 21 e 22: a mesma pergunta com o contexto mínimo, sem R3, e com o completo;
- prática acompanhada do slide 23: uma linha da ficha e o primeiro ponto no gráfico.

## Ponto de partida

- 4 pastas prontas em `experimentos/contexto/`: `minima`, `completa`, `invertida` e `ruido`; cada uma contém só `entrada.md`;
- pergunta fixa e critérios Q1 a Q4 em `apoio/protocolo-contexto.md`;
- gráfico em `apoio/comparar-contextos.html`;
- o que você executa: as condições que o grupo lhe atribuir.

## Entrada

A pergunta fixa de `apoio/protocolo-contexto.md` e o `entrada.md` de cada pasta.

## Saída esperada

Na pasta `entregas/seu-nome/aula-5/`:

- uma resposta por condição que você rodou, com o nome da condição, por exemplo `A-minima.md`;
- `registro.md`, com a tabela do grupo e a sua decisão de contexto.

## Critério de pronto

- [ ] cada condição rodou numa conversa nova, iniciada dentro da cópia da pasta da condição;
- [ ] cada resposta tem qualidade de 0 a 4 pelos critérios Q1 a Q4 e a marca de tarefa concluída, sim ou não;
- [ ] a tabela do grupo tem as 4 condições no modelo A, e o modelo B tem valor ou N/D com motivo;
- [ ] a decisão cita 1 informação que fica, 1 que sai e 1 limite do experimento.

## Tempo estimado

91 minutos em aula: 25 de prática acompanhada, 8 para entrar na sala, 52 em grupo e 6 para o registro.

## Passos

1. Com o professor, rode uma condição e preencha uma linha da ficha.
2. Na sala, o grupo distribui as 8 condições, 4 contextos em 2 modelos: 1 ou 2 por pessoa. Grupos ímpares começam pela mínima; grupos pares, pelo ruído.
3. Rode cada condição como diz `apoio/protocolo-contexto.md`: cópia da pasta, conversa nova, pergunta fixa sem mudança.
4. Dê a nota de 0 a 4, marque se a tarefa foi concluída e anote o tempo.
5. Junte as 8 linhas na tabela do grupo, preencha o gráfico e escreva a sua decisão.

## Plano B

- só um modelo disponível: rode as 4 condições nele e marque o modelo B como N/D; o professor mostra a comparação entre modelos;
- o Claude Code leu outro arquivo: marque a tentativa como contaminada e repita se houver tempo;
- sem acesso ao Claude Code: confira a resposta de um colega com Q1 a Q4 e marque "execução observada".

## Extensão opcional

- repita uma condição para ver a variação, ou proponha um limite em caracteres e confira se ele basta. Não vale ponto extra.

## Pré-requisitos

- atividade 2: conversa nova a cada tentativa e troca de modelo com `/model`;
- copiar uma pasta e abrir o terminal dentro dela.

## Entrega

O registro vale para a AV1, com a rubrica de [avaliacao.md](../../avaliacao.md). Prazo: 23h59 do dia do encontro, horário de Brasília.
