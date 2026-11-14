# Especificação da lista
Objetivo: listar os chamados ativos visíveis para uma pessoa da Oficina.
Entrada: regras R1–R3 e registros T1–T6 em caso/regras.md; consultante da Oficina.
Limites: não inventar prazo, acesso global ou regra adicional; não alterar arquivos.
Saída: tabela ID | prioridade, preservando a ordem dos registros.
Critérios: incluir somente aberto ou em_andamento da Oficina; classificar por R1;
não incluir fechado nem registros de outro departamento; manter as duas colunas e a ordem.
Casos para conferir: T1 entra com alta; T3 fica fora por fechado; T4 entra com baixa.
