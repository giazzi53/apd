from LOGICA import usuario

def imprimir_usuario(usuario):
    print("CPF: ",  usuario[0])
    print("Nome: ", usuario[1])
    print("Email: ", usuario[2])
    print("Senha: ", usuario[3])
    print()


def menu_adicionar():
    print ("\nAdicionar usuário \n")
    cpf = int(input("CPF: "))
    nome = input("Nome: ")
    email = input("Email: ")
    senha = int(input("Senha: "))
    usuario.adicionar_usuario(cpf, nome, email, senha)


def menu_listar():
    print ("\nListar usuários \n")
    usuarios = usuario.listar_usuarios()
    for u in usuarios:
        imprimir_usuario(u)


def menu_buscar():
    print("\nBuscar usuário por CPF \n")
    cpf = int(input("CPF: "))
    u = usuario.buscar_usuario(cpf)
    if (u == None):
        print ("Usuário não encontrado")
    else:
        imprimir_usuario(u)


def menu_remover():
    print("\nRemover usuário \n")
    cpf = int(input("CPF: "))
    u = usuario.remover_usuario(cpf)
    if (u == False):
        print("Usuário não encontrado")
    else:
        print("Usuário removido")


def mostrar_menu():
    run_usuario = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo usuário \n" +
             "(2) Listar usuário \n" +
             "(3) Buscar usuário por CPF \n" +
             "(4) Remover usuário \n" +
             "(0) Voltar\n"+
            "----------------")

    while(run_usuario):
        print(menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 0):
            run_usuario = False
    

