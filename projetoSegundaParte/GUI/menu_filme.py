from LOGICA import filmes
import random


def menu_adicionar_filme():
    titulo = input("Entre com o titulo do filme:")
    genero = input("Entre com o genero do filme:")
    ano = int(input("Entre com o ano do filme:"))
    cod_filme = random.randint(100, 999)
    filmes.adicionar_filmes(titulo, genero, ano, cod_filme)
    print("O codigo do filme é:", cod_filme)

    
def menu_listar_filmes():
    movie = filmes.filmes
    for i in range(len(movie)):
        print("Titulo: {}\nGenero: {}".format(movie[i][0], movie[i][1]))
        print("Ano: {}\nCodigo: {} \n-------------".format(movie[i][2],
                                                           movie[i][3]))


def menu_buscar_filme_cod():
    cod = int(input("Entre com o codigo: "))
    result_busca = filmes.buscar_filme_cod(cod)
    if result_busca is None:
        print("Não foi encontrado filme com esse codigo")
    else:
        print("As informaçoes sobre o filme são:", result_busca)


def menu_buscar_filmes_genero():
    genero = input("Entre com o genero do filme: ")
    result_busca = filmes.buscar_filmes_genero(genero)
    if result_busca is None:
        print("Não foi encontrado nenhum filme com esse genero.")
    else:
        print("O(s) filme(s) com esse genero são:", result_busca)


def menu_remover_filmes_genero():
    genero = input("Entre com o genero de filmes a ser removido: ")
    filmes.remover_filmes_genero(genero)
    print("Filmes do genero {} removidos.".format(genero))


def menu_remover_filme_cod():
    cod = int(input("Entre com o codigo do filme a ser removido: "))
    removido = filmes.remover_filme_cod(cod)
    if removido:
        print("Filme {} removido com sucesso.".format(removido))
    else:
        print("Filme não encontrado.")


def exibir_menu():
    run_menu = True
    while run_menu:
        print(
            "\n----------------\n" +
            "1 - Adicionar filme \n" +
            "2 - Listar filmes \n" +
            "3 - Buscar filme por codigo  \n" +
            "4 - Buscar filmes por genero \n" +
            "5 - Remover filmes por genero\n" +
            "6 - Remover filmes por codigo\n" +
            "0 - Sair\n" +
            "----------------")
        op = int(input("Entre com a opcao desejada:"))

        if op == 1:
            menu_adicionar_filme()
        elif op == 2:
            menu_listar_filmes()
        elif op == 3:
            menu_buscar_filme_cod()
        elif op == 4:
            menu_buscar_filmes_genero()
        elif op == 5:
            menu_remover_filmes_genero()
        elif op == 6:
            menu_remover_filme_cod()
        elif op == 0:
            run_menu = False
