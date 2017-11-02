usuarios = []
avaliacoes = []

def adicionar_usuario(cpf,nome,email,senha, tipo):
    usuario = [cpf,nome,email,senha, tipo,avaliacoes]
    # print(usuario)
    # print(usuarios)
    file = open("usuario.txt","a")
    file.writelines("[" + cpf + ", " + nome +  ", " + email +  ", " + senha +  ", " + tipo + "]\n")
    # iniciar_usuarios()
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
    # usuarios = []
    n = 0
    file = open("usuario.txt", "r")
    aux = file.readlines(n)
    for h in aux:
        usuarios.append(aux[n][1:len(aux[n]) - 2].split(", "))

        n = n + 1
    # print(usuarios)


