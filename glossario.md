# Palavras da disciplina, em linguagem direta

| Palavra | Significado nesta disciplina | Exemplo |
|---|---|---|
| Prompt | Pedido enviado à IA | “Explique R2 em duas frases” |
| Contexto | Informações que a IA recebe para fazer a tarefa | Regra R2 e lista de chamados |
| Modelo | O componente que produz a resposta | Nome exibido pelo Claude Code |
| Sessão | Uma conversa e suas informações disponíveis | Nova conversa para uma tentativa |
| Artefato | Resultado de trabalho que pode ser guardado e revisto | Um pedido salvo em arquivo |
| Especificação | Combinado escrito sobre o que fazer e como conferir | Objetivo, entrada, limites, saída e critérios |
| Restrição | Um limite que precisa ser respeitado | “Não inventar uma regra nova” |
| Critério de aceite | Condição observável para aceitar o resultado | “Excluir o estado fechado” |
| Requisito | Necessidade ou comportamento esperado | “Listar chamados ativos” |
| História de usuário | Forma curta de descrever quem precisa de quê e por quê | “Como suporte, quero ver os chamados ativos...” |
| Zero-shot | Pedido sem exemplo de resposta | Informar tarefa, dados e formato |
| Few-shot | Pedido com exemplos de entrada e saída | Mostrar dois casos antes do novo caso |
| Decomposição | Dividir uma tarefa em partes conferíveis | Definir regra, listar testes, escrever documento |
| Crítica e revisão | Conferir um rascunho por critérios e corrigir o que falhou | Procurar um estado incluído indevidamente |
| Raciocínio explicitado | Explicação verificável da solução apresentada | Mostrar a soma e citar a regra; não exigir pensamentos internos |
| Autoconsistência | Gerar soluções diversas e agregar suas respostas para escolher a mais consistente | A maioria também pode errar; a prática de duas repetições apenas observa variação |
| Fronteira | Ponto em que uma regra muda de comportamento | Soma 4 é media; soma 5 é alta |
| Rastreabilidade | Ligação de uma afirmação ou mudança à sua origem | Um critério identifica a regra R2 que o sustenta |
| Tipo de dado | Forma de representar um valor, como texto ou número | ID em texto; soma como número |
| Conferência semântica | Conferência do significado, além do formato | JSON válido pode trazer a prioridade errada |
| Dependência | Informação ou decisão de outra parte necessária para trabalhar | Testes recebem uma especificação confirmada |
| Acoplamento | Quanto mudanças numa parte afetam as demais | Mudar uma regra exige rever os casos que dependem dela |
| Granularidade | Tamanho escolhido para as unidades de trabalho | Uma tarefa única ou três unidades com contratos próprios |
| Oráculo de teste | Referência usada para saber o resultado esperado | R1 e a soma conferida determinam a prioridade correta |
| Orçamento de contexto | Planejamento do espaço destinado a instruções, histórico, documentos e geração | Reservar espaço sem tratar caracteres como tokens exatos |
| Ferramenta | Recurso que lê, escreve ou executa uma ação | Claude Code ler um arquivo |
| Saída estruturada | Resposta em campos combinados | Tabela com ID, prioridade e regra |
| JSON | Formato de texto com chaves e valores | `{"id":"T1","prioridade":"alta"}` |
| SDD | Desenvolvimento orientado a especificação | Escrever o combinado antes de produzir e conferir |
| Documento de especificação | Registro do comportamento esperado e seus limites | `especificacao.md`; a sigla SDD varia entre textos |
| Token | Pequena unidade de texto processada pelo modelo | Pode ser parte de uma palavra; não é sinônimo de caractere |
| Janela de contexto | Limite de informação que cabe em uma interação | Conversa e arquivos ocupam esse espaço |
| Latência | Tempo de espera definido para a medição | Segundos do envio até a resposta final |
| Variância/dispersão | Quanto os resultados variam | Notas 3 e 4 para a mesma condição |
| Instrução persistente | Orientação do projeto reutilizada entre tarefas | Convenção escrita no `CLAUDE.md` |
| Versionamento | Guardar versões e explicar mudanças | v1, v2 e v3 com histórico |
| Diff | Diferença entre duas versões | Um limite corrigido no texto |
| Regressão | Algo que funcionava deixar de funcionar após uma mudança | O prompt novo passar a incluir chamados fechados |
| Pull request | Pedido de revisão de uma mudança em repositório | Colega comenta o texto antes da integração |

As definições são apoio de leitura e de interpretação. Não propõem sinais em Libras. Sempre que um termo voltar, o professor o liga a um arquivo ou a um exemplo conhecido.
