from LOGICA import lista_toWatch
run_menu = True

def adicionar_filme(cpf, filme):
    lista =  lista_toWatch.adicionar_toWatch(cpf, filme)
    print(lista)




def exibir_menu():
    while run_menu:
        print(
            "\n----------------\n" +
            "1 - Adicioar filme a lista..\n" +
            "2 - Acessar menu Usuario." +
            "3 - Acessar menu Usuario"
        )