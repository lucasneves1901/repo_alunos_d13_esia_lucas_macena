## R1 — prioridade
Impacto e urgência são inteiros de 1 a 3. Somar os dois. Soma >= 5: alta; soma 3 ou 4: media; soma 2: baixa. As entradas são válidas.
---

## R2 — estados
Ativos têm estado aberto ou em_andamento. Fechado fica fora. Preservar a ordem de entrada.
---

## Dados fictícios
| ID | Departamento | Estado | Impacto | Urgência |
|---|---|---|---|---|
| T1 | Oficina | aberto | 3 | 2 |
| T2 | Laboratório | em_andamento | 1 | 2 |
| T3 | Oficina | fechado | 3 | 3 |
| T4 | Oficina | em_andamento | 1 | 1 |
| T5 | Laboratório | aberto | 2 | 2 |
| T6 | Oficina | aberto | 2 | 3 |
