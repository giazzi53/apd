import unittest
from LOGICA import filmes


class TestFilmes(unittest.TestCase):

    def setUp(self):
        filmes.filmes = []

# testa se ao adicionar um filme, a sublista tem o tamanho 4, evidenciando
# que a sublista contem todos as infos necessarias
    def test_adicionar_filmes(self):
        filmes.adicionar_filmes("filme", "genero", 2017, 1)
        self.assertEqual(4, len(filmes.filmes[0]))

    # testa se a busca esta realmente retornando o codigo esperado com as
    # informacoes esperadas.
    def test_buscar_filmes_cod(self):
        filmes.adicionar_filmes("filme", "genero", 2017, 1)
        self.assertEqual(["filme", "genero", 2017, 1],
                         filmes.buscar_filme_cod(1))

    # testa se a busca funciona com somente um filme do genero.
    def test_buscar_filmes_genero(self):
        filmes.adicionar_filmes("filme", "genero", 2017, 1)
        self.assertEqual(["filme"], filmes.buscar_filmes_genero("genero"))

    # testa se a busca funciona com mais de um filme do mesmo genero.
    def test_buscar_filmes_generos(self):
        filmes.adicionar_filmes("filme", "genero", 2017, 1)
        filmes.adicionar_filmes("movie", "genero", 1996, 2)
        self.assertEqual(2, len(filmes.buscar_filmes_genero("genero")))

    # teste para remover filme por codigo
    def test_remover_filme_codigo(self):
        filmes.adicionar_filmes("filme", "genero", 2017, 1)
        filmes.remover_filme_cod(1)
        self.assertEqual(0, len(filmes.filmes))

    # teste para remover um filme de um genero
    def test_remover_filmes_genero(self):
        filmes.adicionar_filmes("filme", "genero", 2017, 1)
        filmes.remover_filmes_genero("genero")
        self.assertEqual(0, len(filmes.filmes))

    # teste para remover mais de um filme do mesmo genero
    def test_remover_filmes_generos(self):
        filmes.adicionar_filmes("filme", "genero", 2017, 1)
        filmes.adicionar_filmes("movie", "genero", 1996, 2)
        filmes.remover_filmes_genero("genero")
        self.assertEqual(0, len(filmes.filmes))


if __name__ == '__main__':
    unittest.main(exit=False)
