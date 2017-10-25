usuarios = []

def adicionar_usuario(cpf,nome,email,senha, tipo):
    usuario = [cpf,nome,email,senha, tipo]
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
    #### tipo 1 = admin | tipo 2 = usuario padrão ####
    adicionar_usuario(1, "admin", "admin@admin.com", "1", 1)
    adicionar_usuario(11111111111,"Cristiano","Cristiano@email.com","123456", 2)
    adicionar_usuario(22222222222, "Guilherme", "Guilherme@email.com","654321", 2)


