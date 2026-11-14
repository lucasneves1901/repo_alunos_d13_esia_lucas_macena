# Avaliação: poucos artefatos, conferência clara

**Proposta para D1.3:** práticas 20%, reescrita 30%, conjunto final 50%. Os pesos vêm do plano base. Datas e procedimentos operacionais devem ser comunicados no primeiro encontro. Não são importadas as regras particulares da D1.1.

## Cálculo

Cada instrumento recebe nota de 0 a 10. **Nota = 0,20 × AV1 + 0,30 × AV2 + 0,50 × AV3.** Critérios usam níveis 0, 1 ou 2: 0 = sem evidência; 1 = parcial ou depende de explicação extra; 2 = atendido e verificável. A nota é a soma de `peso do critério × nível ÷ 2`, dividida por 10.

## AV1: participação nas seis práticas · 20%

Cada atividade gera um registro individual de quatro seções curtas, na mesma pasta dos arquivos da atividade. O registro começa nos minutos finais do bloco e pode ser entregue até 23h59 do mesmo dia, horário de Brasília. Quem atuou em grupo identifica sua parte e escreve sua própria conclusão. A nota AV1 é a média das seis notas de prática, após tratar ocorrências e eventuais avaliações equivalentes pelo fluxo institucional.

| Critério por prática | Peso |
|---|---:|
| Produz o artefato solicitado e identifica sua contribuição | 40% |
| Confere com um critério e registra evidência concreta | 40% |
| Explica uma mudança, escolha ou dúvida fundamentada | 20% |

Não se avalia quantidade de fala, rapidez de digitação ou número de chamadas. A discussão escrita vale como participação. O professor registra níveis e uma evidência; dá devolutiva coletiva a cada bloco e comentário individual nos blocos 3 e 6.

## AV2: reescrita da especificação · 30%

**Individual, 2h, prazo proposto 11/11/2026, 23h59, Brasília.** Partir do bloco 3: guardar v1, ler a devolutiva, corrigir para v2 e mostrar como conferir. Entregar até duas páginas de texto principal, com v1, v2 e evidências anexas. Incluir **duas unidades de trabalho**, cada uma com entrada, saída e critério; é uma primeira aproximação da decomposição, aprofundada no bloco 4.

| Critério | Peso |
|---|---:|
| Objetivo, entradas, limites e formato estão claros | 25% |
| Critérios distinguem acerto/erro e incluem um caso de fronteira | 35% |
| Duas partes podem ser conferidas e a dependência está explícita | 20% |
| Histórico liga uma mudança à devolutiva e a uma nova verificação | 20% |

Usar o [modelo de especificação](modelos/especificacao.md) e o [histórico](modelos/historico.md). Pode usar Claude Code para revisar; deve apontar uma sugestão aceita e uma rejeitada ou desnecessária, com motivo. Se nenhuma sugestão foi rejeitada, explicar o que foi conferido antes de aceitar.

## AV3: conjunto final de artefatos · 50%

**Individual, 2h de finalização, prazo proposto 19/11/2026, 23h59, Brasília.** Usar um recorte compartilhável de projeto real ou seu equivalente fictício. O projeto Fila Clara é a alternativa didática disponível para quem não puder compartilhar. O trabalho já começa em aula, sem exigir implementar um produto.

Entregar uma pasta com:

1. `especificacao.md`: tarefa, limites, formato, critérios e técnica escolhida com motivo.
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

Ausência e nota são registros distintos. Ausência em avaliação por motivo justo e comprovado segue solicitação e validação institucional; o plano base prevê nova avaliação em até cinco dias úteis. Não se aplica automaticamente a regra de “sem reposição” da D1.1. Outras ocorrências e atrasos seguem orientação da coordenação; não se inventa penalidade neste material.

O colega presente integra um trio ou realiza a tarefa com um revisor designado. A contribuição individual continua identificada. Falha de acesso/cota registrada permite análise da contingência fornecida e conferência por escrito, com a mesma rubrica; medições ausentes não podem ser apresentadas como reais. Cabe ao professor completar a comparação entre modelos quando faltante. A AV3 pode ser finalizada sem nova chamada após o término da licença.

## O que significa nível 2

Outra pessoa consegue localizar a regra, repetir a conferência e entender sua decisão. “Ficou melhor” não basta. “Na v1 faltava excluir fechado; na v2 incluí o critério e conferi o registro T3” é uma evidência verificável.
