import unittest

from fila_clara.cli import carregar, listar
from fila_clara.regras import ativos, prioridade, visiveis


class TestePrioridade(unittest.TestCase):
    def test_faixas_da_r1(self):
        self.assertEqual(prioridade(1, 1), "baixa")
        self.assertEqual(prioridade(2, 2), "media")
        self.assertEqual(prioridade(2, 3), "alta")


class TesteAtivosEVisiveis(unittest.TestCase):
    def test_r2_tira_fechado_e_mantem_a_ordem(self):
        chamados = [{"id": "X1", "estado": "aberto"}, {"id": "X2", "estado": "fechado"},
                    {"id": "X3", "estado": "em_andamento"}]
        self.assertEqual([c["id"] for c in ativos(chamados)], ["X1", "X3"])

    def test_r3_so_o_proprio_departamento(self):
        ids = [c["id"] for c in visiveis(carregar(), "Laboratório")]
        self.assertEqual(ids, ["T2", "T5"])


class TesteListar(unittest.TestCase):
    def test_lista_da_oficina(self):
        self.assertEqual(listar(carregar(), "Oficina"), ["T1 | alta", "T4 | baixa", "T6 | alta"])


if __name__ == "__main__":
    unittest.main()
