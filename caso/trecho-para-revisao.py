# Trecho didático com divergência intencional em relação a R2.
# Entradas válidas. O esperado vem do contrato, não deste código.
def listar_ativos(chamados):
    return [c for c in chamados if c["estado"] == "aberto"]
