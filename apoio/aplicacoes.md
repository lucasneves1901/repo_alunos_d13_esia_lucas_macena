# O mesmo combinado em cinco tipos de trabalho

A estrutura é sempre a mesma: tarefa, informações, limites, saída e conferência. Muda só o artefato.

| Aplicação | Pedido pequeno no Claude Code | Saída | Como conferir |
|---|---|---|---|
| Requisitos | Transformar a demanda A em história e critérios, separando sugestões | História e três critérios | Cada afirmação tem origem nas regras ou está marcada como dúvida |
| Testes | Propor casos de prioridade nos limites de soma 4 e 5 | Tabela entrada e esperado | Calcular a soma à mão e conferir R1 |
| Documentação | Explicar R2 para uma pessoa nova em até 80 palavras | Parágrafo com exemplo | Inclui aberto e em_andamento, exclui fechado, preserva a ordem |
| Revisão de código | Confrontar `caso/trecho-para-revisao.py` com R2 | Achado, linha, motivo e caso que revela o problema | Rastrear aberto, fechado e em_andamento |
| Arquitetura | Registrar a decisão de manter a regra numa função separada | Contexto, duas opções, decisão e consequência | A decisão diz o que evita e o que custa |

## Exemplo resolvido de teste

Tarefa: um caso que separe as faixas media e alta. Impacto 2 e urgência 2 dão soma 4, media. Impacto 2 e urgência 3 dão soma 5, alta. Os dois casos conferem a fronteira de R1; não cobrem o sistema inteiro.

## Pedido de revisão do código

```text
Leia caso/trecho-para-revisao.py e somente a regra R2 de caso/regras.md.
Faça uma revisão sem alterar arquivos. Responda em tabela:
achado | evidência no código | caso que revela o problema | correção sugerida.
Não acrescente requisito de banco, login ou tratamento de entrada inválida.
```

O código tem uma divergência de propósito. O esperado vem de R2, não da saída do código. Quem não executa Python rastreia a lista linha a linha e registra "inspeção manual".
