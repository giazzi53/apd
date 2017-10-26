usuarios = []


def adicionar_usuario(cpf, nome, email, senha):
    user = [cpf, nome, email, senha]
    usuarios.append(user)


def listar_usuarios():
    return usuarios


def buscar_usuario(cpf):
    for u in usuarios:
        if u[0] == cpf:
            return u
    return None


def remover_usuario(cpf):
    for u in usuarios:
        if u[0] == cpf:
            usuarios.remove(u)
            return True
    return None

def iniciar_usuarios():
    adicionar_usuario(222222, "Joao", "joao.silva@gmail.com", 42343)
    adicionar_usuario(333333, "Guilherme", "gui.silva@gmail.com", 10343)
