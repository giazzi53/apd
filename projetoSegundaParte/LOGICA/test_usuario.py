import unittest
from LOGICA import usuario


class TestUsuario(unittest.TestCase):
    
    def setUp(self):
        usuario.usuarios = []

    # testa se ao adicionar um usuario, a sublista tem o tamanho 4, evidenciando
    # que a sublista contem todos as infos necessarias

    def test_adicionar_usuario(self):
        usuario.adicionar_usuario(222222, "Joao", "joaosilva@gmail.com", "123abc")
        self.assertEqual(4, len(usuario.usuarios[0]))

    # testa se a listagem de usuarios esta realmente retornando a lista completa
    # com as informacoes esperadas

    def test_listar_usuarios(self):
        usuario.listar_usuarios()
        self.assertEqual([], usuario.listar_usuarios())
    # testa se a busca esta realmente retornando o usuario esperado com as
    # informacoes esperadas

    def test_buscar_usuario(self):
        usuario.adicionar_usuario(222222, "Joao", "joaosilva@gmail.com", "123abc")
        self.assertEqual([222222, 'Joao', 'joaosilva@gmail.com', '123abc'], usuario.buscar_usuario(222222))

    # teste para remover um usuario
    def test_remover_usuario(self):
        usuario.adicionar_usuario(222222, "Joao", "joaosilva@gmail.com", "123abc")
        usuario.remover_usuario(222222)
        self.assertEqual(0, len(usuario.usuarios))
        

if __name__ == '__main__':
    unittest.main(exit=False)
