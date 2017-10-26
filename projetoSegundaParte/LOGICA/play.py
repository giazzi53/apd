from GUI import menu_filme
from LOGICA import filmes  
    
def reproduzir_filme():
    print("Os filmes disponíveis para assistir são: ") 
    print(menu_filme.menu_listar_filmes())
    cod_filme = int(input("Digite o código do filme que deseja assistir: "))
    a = filmes.buscar_filme_cod(cod_filme)
    if a == None:
        print("Esse filme não existe na lista")
    else:
        print("Deu play ao filme ", a[0])
          

          

          
