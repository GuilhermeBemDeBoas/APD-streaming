usuarios = []

def adicionar_usuario(cpf,nome,email,senha, tipo):
    usuario = [cpf,nome,email,senha, tipo]
    file = open("usuario.txt","a")
    file.writelines("[" + cpf + ", " + nome +  ", " + email +  ", " + senha +  ", " + tipo + "]\n")
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
    n = 0
    file = open("usuario.txt", "r")
    aux = file.readlines(n)
    for h in aux:
        usuarios.append(aux[n][1:len(aux[n]) - 2].split(", "))

        n = n + 1


