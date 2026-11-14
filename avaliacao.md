# Avaliação: duas atividades

A nota da D1.3 vem de duas atividades individuais. As práticas em aula não têm nota: o que você produz nelas é o ponto de partida das duas atividades. Pesos e prazos são a proposta do plano de ensino, no horário de Brasília. As regras particulares da D1.1 não valem aqui.

| Atividade | Peso | Prazo | Parte de |
|---|---:|---|---|
| 1. Especificação revisada | 40% | 11/11/2026, 23h59 | Especificação do bloco 3 |
| 2. Conjunto final de artefatos | 60% | 19/11/2026, 23h59 | Arquivos dos blocos 2, 4, 5 e 6 |

## Cálculo

Cada atividade recebe nota de 0 a 10. **Nota = 0,40 × Atividade 1 + 0,60 × Atividade 2.** Cada critério recebe nível 0, 1 ou 2: 0 = sem evidência; 1 = parcial ou depende de explicação extra; 2 = atendido e verificável. A nota é a soma de `peso do critério × nível ÷ 2`, dividida por 10.

## As práticas em aula

Cada prática gera arquivos e um registro de quatro seções na sua pasta de `entregas/`. O registro não tem nota nem prazo. Ele guarda a evidência que as duas atividades pedem: o que você produziu, o que conferiu e o que mudou. Os registros já entregues continuam valendo como evidência. Não se avalia quantidade de fala, rapidez de digitação ou número de chamadas.

## Atividade 1: especificação revisada · 40%

**Individual, 2h, prazo 11/11/2026, 23h59.** É a antiga AV2, com o mesmo enunciado e os mesmos critérios. Quem entregou a AV2 não refaz nada: a entrega vale como Atividade 1.

Partir do bloco 3: guardar v1, ler a devolutiva, corrigir para v2 e mostrar como conferir. Entregar até duas páginas de texto principal, com v1, v2 e evidências anexas. Incluir **duas unidades de trabalho**, cada uma com entrada, saída e critério; é uma primeira aproximação da decomposição, aprofundada no bloco 4.

| Critério | Peso |
|---|---:|
| Objetivo, entradas, limites e formato estão claros | 25% |
| Critérios distinguem acerto/erro e incluem um caso de fronteira | 35% |
| Duas partes podem ser conferidas e a dependência está explícita | 20% |
| Histórico liga uma mudança à devolutiva e a uma nova verificação | 20% |

Usar o [modelo de especificação](modelos/especificacao.md) e o [histórico](modelos/historico.md). Pode usar Claude Code para revisar; deve apontar uma sugestão aceita e uma rejeitada ou desnecessária, com motivo. Se nenhuma sugestão foi rejeitada, explicar o que foi conferido antes de aceitar.

## Atividade 2: conjunto final de artefatos · 60%

**Individual, 2h de finalização, prazo 19/11/2026, 23h59.** É a antiga AV3. Usar um recorte compartilhável de projeto real ou seu equivalente fictício. O projeto Fila Clara é a alternativa didática disponível para quem não puder compartilhar. O trabalho já começa em aula, sem exigir implementar um produto.

Entregar uma pasta com:

1. `especificacao.md`: a v2 da Atividade 1, ou uma nova se mudar de tarefa, com a técnica escolhida e o motivo.
2. `decomposicao.md`: duas a quatro partes com entrada, saída, responsável e conferência.
3. `contexto.md`: o que entrou, saiu e em que ordem; evidência de pelo menos duas condições, efeito observado, tempo e consumo disponível ou N/D justificado.
4. `CLAUDE.md`: instruções persistentes específicas e executáveis.
5. `historico.md` e versões: **v1 inicial + v2 e v3**, duas revisões com motivo, devolutiva e nova conferência.
6. `verificacao.md`: três casos conhecidos reavaliados; pedido e saída guardados, modelo, data e limitações. Identificar a contribuição da IA.

Limite: quatro páginas equivalentes de texto principal somando os itens 1 a 4, mais histórico e evidências curtas. Pode entregar os arquivos Markdown; não é necessário montar apresentação. O teste de regressão é uma conferência pequena de três casos, sem criar framework de avaliação.

| Critério | Peso |
|---|---:|
| Especificação e critérios permitem conferir; partes se conectam | 25% |
| Técnica é escolhida por necessidade, com limite reconhecido | 15% |
| Decisão de contexto usa efeito observado e esforço/consumo | 20% |
| Instruções persistentes são úteis, específicas e conferíveis | 20% |
| Duas revisões e nova conferência mostram o que mudou | 20% |

## Ausência, parceiro e dificuldade de acesso

Ausência e nota são registros distintos. Faltar a uma aula não muda a nota, que vem só das duas atividades; a falta conta na frequência. Entrega perdida por motivo justo e comprovado segue solicitação e validação institucional; o plano base prevê nova avaliação em até cinco dias úteis. Não se aplica automaticamente a regra de “sem reposição” da D1.1. Outras ocorrências e atrasos seguem orientação da coordenação; não se inventa penalidade neste material.

O colega presente integra um trio ou realiza a tarefa com um revisor designado. A contribuição individual continua identificada. Falha de acesso/cota registrada permite análise da contingência fornecida e conferência por escrito, com a mesma rubrica; medições ausentes não podem ser apresentadas como reais. Cabe ao professor completar a comparação entre modelos quando faltante. A Atividade 2 pode ser finalizada sem nova chamada após o término da licença.

## O que significa nível 2

Outra pessoa consegue localizar a regra, repetir a conferência e entender sua decisão. “Ficou melhor” não basta. “Na v1 faltava excluir fechado; na v2 incluí o critério e conferi o registro T3” é uma evidência verificável.
