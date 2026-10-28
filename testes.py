
import unittest
import grafos as programa


def matriz_de_arestas(qnt_vertices, arestas):
    matriz = [
        [0] * len(arestas)
        for _ in range(qnt_vertices)
    ]

    for coluna, (u, v) in enumerate(arestas):
        matriz[u - 1][coluna] = 1
        matriz[v - 1][coluna] = 1

    return matriz


class TestesGrafos(unittest.TestCase):

    def test_ciclo_c4_euleriano_e_circuito_valido(self):
        # C4: todos os vértices têm grau 2 e o grafo é conexo.
        arestas = [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 1),
        ]
        matriz = matriz_de_arestas(4, arestas)

        self.assertTrue(programa.euleriano(arestas, matriz))

        circuito = programa.circuito_euler(arestas, matriz)
        self.assertIsNotNone(circuito)
        self.assertTrue(programa.valida_circuito(arestas, circuito))

    def test_caminho_p4_nao_e_euleriano(self):
        # P4: os vértices das pontas têm grau ímpar (1).
        arestas = [
            (1, 2),
            (2, 3),
            (3, 4),
        ]
        matriz = matriz_de_arestas(4, arestas)

        self.assertFalse(programa.euleriano(arestas, matriz))
        self.assertIsNone(programa.circuito_euler(arestas, matriz))

    def test_duas_componentes_ciclicas_desconectadas(self):
        # Dois ciclos C4 separados. Todos os graus são pares,
        # mas os vértices de grau positivo não pertencem à mesma componente.
        arestas = [
            (1, 2), (2, 3), (3, 4), (4, 1),
            (5, 6), (6, 7), (7, 8), (8, 5),
        ]
        matriz = matriz_de_arestas(8, arestas)

        self.assertFalse(programa.conexo(arestas, matriz))
        self.assertFalse(programa.euleriano(arestas, matriz))
        self.assertIsNone(programa.circuito_euler(arestas, matriz))

    def test_grafo_vazio_tratado_explicitamente(self):
        # um grafo sem arestas é considerado Euleriano,
        # mas circuito_euler retorna None.
        arestas = []
        matriz = matriz_de_arestas(4, arestas)

        self.assertTrue(programa.conexo(arestas, matriz))
        self.assertTrue(programa.euleriano(arestas, matriz))
        self.assertIsNone(programa.circuito_euler(arestas, matriz))
        self.assertFalse(programa.valida_circuito(arestas, None))


if __name__ == "__main__":
    unittest.main(verbosity=2)
