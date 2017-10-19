usuarios = []

def adicionar_usuario(cpf,nome,email,senha):
    usuario = [cpf,nome,email,senha]
    usuarios.append(usuario)

def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for u in usuarios:
        if(u[0] == cpf):
            return u

def remover_usuario(cpf):
    for u in usuarios:
        if (u[0] == cpf):
            usuarios.remove(u)
            return True
    return False

def iniciar_usuarios():
    adicionar_usuario(11111111111,"Cristiano","Cristiano@email.com",123456)
    adicionar_usuario(22222222222, "Guilherme", "Guilherme@email.com",654321)

