# Passagem de U1 para U2
U1 entrega a regra confirmada e os dados abaixo.
U2 deve produzir uma tabela com três casos: T1, T3 e T4, nessa ordem.
Para cada caso: entrada, incluir/excluir e prioridade quando incluído.
O caso considera um registro por vez e a lista de ativos visíveis a quem consulta.
Se faltar informação, registrar a lacuna, sem inventar o resultado.

# Fila Clara: recorte da D1.3

Organização fictícia que recebe chamados das áreas Oficina e Laboratório. Vamos escrever pedidos, requisitos, testes e documentação para esse serviço. O contrato retoma as regras didáticas da D1.1; não é preciso lembrar aquela aula para começar.

| ID | Regra vigente |
|---|---|
| R1 | Impacto e urgência são inteiros de 1 a 3. Somar os dois. Soma maior ou igual a 5: `alta`; soma 3 ou 4: `media`; soma 2: `baixa`. |
| R2 | Chamados ativos têm estado `aberto` ou `em_andamento`. `fechado` fica fora. Manter a ordem da lista recebida. |
| R3 | Uma pessoa só pode visualizar chamados do próprio departamento. Estado e prioridade não mudam essa regra. |
| R4 | Testes e documentação precisam respeitar R1, R2 e R3. |

As entradas são válidas. `media` é escrito sem acento na saída. Não há regra de prazo de atendimento, envio de e-mail, administrador com acesso geral, banco de dados ou autenticação a implementar. Se isso aparecer numa resposta, é uma sugestão nova e depende de decisão; não é requisito deste caso.

## Pequenos exemplos resolvidos

- Impacto 2 e urgência 3: soma 5, prioridade `alta`.
- A lista X1 aberto, X2 fechado, X3 em_andamento tem dois ativos: X1 e X3, nessa ordem.
- Uma pessoa da Oficina não vê um chamado do Laboratório, mesmo com prioridade alta.

## Os registros das práticas

| ID | Departamento | Estado | Impacto | Urgência |
|---|---|---|---:|---:|
| T1 | Oficina | aberto | 3 | 2 |
| T2 | Laboratório | em_andamento | 1 | 2 |
| T3 | Oficina | fechado | 3 | 3 |
| T4 | Oficina | em_andamento | 1 | 1 |
| T5 | Laboratório | aberto | 2 | 2 |
| T6 | Oficina | aberto | 2 | 3 |

Os mesmos dados estão em `chamados.json`. As tarefas definem quais regras usar; não se deve acrescentar filtro por departamento se a tarefa pedir somente classificação de prioridade.

## Decisão confirmada
A pessoa consultante é da Oficina.
