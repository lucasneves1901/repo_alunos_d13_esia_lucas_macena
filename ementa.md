# Plano de ensino: D1.3

**Prompting Técnico, Especificação e Contexto** · Pós-Graduação Lato Sensu em Engenharia de Software e IA · CESAR School · Turma 01, 2026.2.

## 1. Identificação

| Campo | Definição |
|---|---|
| Professor | Victor Hugo Wanderley Freire |
| Lugar no curso | Terceira disciplina do Módulo 1; encerramento do módulo |
| Carga horária | 24h: 18h ao vivo e 6h de estudo autônomo |
| Formato | Remoto ao vivo, 42 alunos, seis blocos de 180 minutos |
| Ferramenta das práticas | Claude Code, com o acesso da turma informado pelo professor |
| Preparação | Abrir a pasta do kit, escrever um pedido e salvar um arquivo; retomados com apoio no bloco 1 |

## 2. Ementa

Tratamento de prompts como artefatos de especificação técnica, e não apenas comandos textuais. Trabalho com clareza de objetivo, critérios de sucesso, exemplos, restrições, decomposição de problemas, documentos de contexto, SDDs, instruções persistentes e versionamento de decisões. Aplicação em requisitos, testes, documentação, revisão de código e arquitetura.

## 3. O que vamos aprender

Ao final, cada estudante deverá conseguir:

1. Escrever o que precisa, quais limites devem ser respeitados, como a resposta deve vir e como outra pessoa vai conferi-la.
2. Escolher uma técnica de prompting pelo problema que ela ajuda a resolver e reconhecer seu limite.
3. Selecionar e ordenar as informações da tarefa, explicando o efeito na resposta e no esforço de execução.
4. Dividir uma tarefa em partes que possam ser executadas e conferidas separadamente.
5. Escrever instruções duradouras de projeto, úteis a pessoas e à IA.
6. Guardar versões, registrar mudanças e conferir novamente os casos conhecidos quando algo mudar.

## 4. Conteúdo programático

Pedido como artefato de engenharia; técnicas e critérios de escolha; especificação e critérios de aceite; decomposição; engenharia de contexto; instruções persistentes e versionamento. Os nomes técnicos serão apresentados depois da explicação em português e retomados no glossário.

## 5. Calendário e produtos

Horário de Brasília. Almoço dos sábados: 12h às 14h, fora da carga. Encerramento às 17h.

| Bloco | Data e horário | Tema | Produto |
|---|---|---|---|
| 1 | 06/11/2026, 19h às 22h | Escrever um pedido claro | Pedido inicial, versão revista e devolutiva |
| 2 | 07/11/2026, 9h às 12h | Escolher uma técnica | Comparação de três técnicas e dois modelos |
| 3 | 07/11/2026, 14h às 17h | Escrever o combinado e conferir | Especificação, critérios e revisão por colega |
| 4 | 13/11/2026, 19h às 22h | Dividir para conseguir conferir | Unidades de trabalho e teste da passagem entre elas |
| 5 | 14/11/2026, 9h às 12h | Escolher o contexto | Quatro montagens, resultados e decisão |
| 6 | 14/11/2026, 14h às 17h | Guardar instruções e revisões | Instruções persistentes, histórico e regressão |

## 6. Como serão as aulas

Um caso fictício curto, Fila Clara, acompanha os seis encontros. Primeiro o professor mostra um exemplo. Depois a turma faz uma tentativa com apoio e trabalha em pares ou grupos. O colega confere o resultado usando o que está escrito. Cada pessoa registra sua contribuição, inclusive quando trabalha em grupo.

No bloco 1, 15 minutos retomam as disciplinas anteriores. Os comandos básicos entram durante a prática, em pequenos passos. Não haverá instalação de modelos locais, integração de API, subagentes, RAG ou construção de infraestrutura.

| Momento | Bloco 1 | Blocos 2 a 6 |
|---|---:|---:|
| Abertura e retomada | 15min | 10min |
| Conceitos, mecanismos e exemplos resolvidos | 50min | 45min |
| Demonstração operacional do professor | 10min | 10min |
| Prática acompanhada | 25min | 25min |
| Organização e entrada nas salas | 8min | 8min |
| Prática em pares/grupos | 42min | 52min |
| Retorno das salas | 8min | 8min |
| Discussão de três casos | 12min | 12min |
| Registro e fechamento | 10min | 10min |
| **Total** | **180min** | **180min** |

As pausas de interpretação, leitura e dúvidas curtas estão dentro desses tempos. Serão mantidos 21 pares, reunidos em sete grupos de seis nos blocos 2, 4 e 5. Na ausência de um parceiro, forma-se um trio; os papéis alternam e o registro continua individual.

Os slides explicam cada conceito em três etapas: definição e funcionamento; exemplo resolvido; limite e pergunta com resposta comentada. São 28 slides por aula. Quinze minutos da demonstração anterior foram incorporados à explicação conceitual com exemplos; a prática acompanhada e o trabalho dos estudantes mantêm seus tempos. O PDF dos slides permite retomar a explicação sem depender só da fala do professor.

O mapa e o fechamento percorrem os mesmos seis conceitos. Diagramas mostram sequências, decisões, ciclos e comparações conforme a relação estudada. Cada demonstração usa dois atos da mesma tarefa, declara o que muda e conecta a observação aos conceitos. Caminhos e instruções de preparação ficam no material de apoio.

## 7. Exercícios com Claude Code

Os pedidos e modelos de registro já vêm no kit. As tarefas exigem leitura e escrita de documentos curtos. Quando houver código, ele será pequeno e acompanhado de uma tabela de resultados esperados. O uso da IA deve ser identificado; a verificação e a explicação do resultado são do estudante.

Nos blocos 2 e 5, comparam-se dois modelos ou duas versões disponíveis no Claude Code. O professor verifica o acesso antes das execuções. A prática usa sessões novas, arquivos definidos e critérios iguais. Se um segundo modelo não estiver disponível, a comparação entre técnicas/contextos continua e a comparação entre modelos fica registrada como pendente de execução demonstrada, sem inventar resultados.

## 8. Avaliação

Desenho didático proposto: **20% práticas + 30% reescrita + 50% conjunto final de artefatos**. A [avaliação](avaliacao.md) detalha critérios, limites de tamanho, cálculo e tratamento de ocorrências. Não há nota por falar em público ou por quantidade de chamadas à IA.

## 9. Estudo autônomo

| Atividade | Tempo | Entrega | Prazo proposto |
|---|---:|---|---|
| L0: leitura orientada de duas referências básicas | 2h | Fichamento curto, formativo | 11/11/2026, 23h59 |
| AV2: reescrita do bloco 3 | 2h | Especificação revista, decomposição curta e registro | 11/11/2026, 23h59 |
| AV3: organizar e conferir o conjunto final | 2h | Pasta versionada com os artefatos já construídos | 19/11/2026, 23h59 |

Os trabalhos são desenvolvidos progressivamente em aula. A AV3 usa as duas horas para revisar, conferir e organizar, sem exigir construir uma aplicação nova. Horário de Brasília.

## 10. Acessibilidade e apoio

Materiais em texto selecionável, glossário prévio, instruções por escrito, descrição oral de diagramas, fonte ampliada e tempo para leitura. Contribuição por texto tem o mesmo valor que a oral. A organização das salas considera o acompanhamento de Libras, combinado com a coordenação. Quem tiver dificuldade começa pelo pedido-modelo e pelo primeiro critério; a extensão opcional não dá pontos extras.

## 11. Frequência e ocorrências

O plano base informa limite de falta de 25%, reprovação por falta acima desse limite, gravações após 48h disponíveis por 90 dias apenas para revisão e abono somente pela Secretaria com comprovante. Gravação não gera presença. Ausência em atividade avaliativa será tratada conforme fluxo institucional, inclusive nova avaliação por motivo justo e comprovado mediante solicitação. A disciplina não cria dispensa automática dessa regra.

## 12. Materiais e dados

Claude Code, editor de texto e kit local; nenhum exercício exige crédito de API ou dados de empregador. O caso e seus números são fictícios. Para aplicar a um projeto real, usar apenas um recorte autorizado e anonimizado; quem não puder compartilhar usa o equivalente didático. O acesso ao Claude Code está informado pelo professor, mas disponibilidade de modelos, cota e vigência após 14/11 precisam ser conferidas. A entrega final pode ser concluída com os registros já obtidos em aula.

## 13. Bibliografia

Básica: Schulhoff et al., *The Prompt Report* (2024); Mei et al., *A Survey of Context Engineering for Large Language Models* (2025); Chen et al., *Promptware Engineering* (2025). Complementar: Liu et al.; Stoica et al.; Villamizar et al.; Ronanki et al.; White et al.; Berryman e Ziegler. [Lista completa e referências operacionais](referencias.md).
