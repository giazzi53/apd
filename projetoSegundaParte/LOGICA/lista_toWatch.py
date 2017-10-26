from LOGICA import usuario
toWatch = []

def adicionar_toWatch(cpf, filme):
    for u in usuario.usuarios:
        if len(u) == 4:
            usuario.usuarios.append(True)
            toWatch.append([cpf, filme])
        elif len(u) == 5:
            for c in toWatch:
                if c[0] == cpf:
                    c.append(filme)
    return toWatch