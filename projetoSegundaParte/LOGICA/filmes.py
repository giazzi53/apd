filmes = []


def adicionar_filmes(titulo, genero, ano, cod_filme):
    movie = [titulo, genero, ano, cod_filme]
    filmes.append(movie)

    
def listar_filmes():
    return filmes

    
def buscar_filme_cod(cod_filme):
    for c in filmes:
        if c[3] == cod_filme:
            return c
    return


def buscar_filmes_genero(genero_filme):
    results = []
    for i in range(len(filmes)):
        for g in filmes[i]:
            if g == genero_filme:
                results.append(filmes[i][0])
    if results:
        return results
    else:
        return


def remover_filmes_genero(genero):
    remove = []
    for g in filmes:
        for i in range(len(filmes)):
            if g[1] == genero:
                remove.append(g)
                break
    for j in range(len(remove)):
        filmes.remove(remove[j])


def remover_filme_cod(cod):
    for c in filmes:
        if c[3] == cod:
            filmes.remove(c)


def iniciar_filmes():
    adicionar_filmes("Interstellar", "Sci-Fi", 2014, 100)
    adicionar_filmes("The Godfather", "Drama", 1972, 101)
