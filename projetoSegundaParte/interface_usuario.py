from GUI import menu_filme, menu_usuario, menu_lista_toWatch
from LOGICA import filmes, usuario, play

def inicializar_dados():
    filmes.iniciar_filmes()
    # usuario.inciar_usuarios()

inicializar_dados()
flag = True
while flag:
    print(
        "\n----------------\n" +
        "1 - Acessar menu Filmes.\n" +
        "2 - Acessar menu Usuario.\n"+
        "3 - Acessar menu ToWatch\n" +
        "4 - Dar play"
    )
    op = int(input("Entre com a opção desejada:"))
    while op != 1 and op != 2 and op != 3 and op != 4:
        print("Opção incorreta.")
        op = int(input("Entre com a opção desejada:"))
    if op == 1:
        menu_filme.exibir_menu()
    elif op == 2:
        menu_usuario.mostrar_menu()
    elif op == 3:
        menu_lista_toWatch.exibir_menu()
    elif op == 4:
        play.reproduzir_filme()

