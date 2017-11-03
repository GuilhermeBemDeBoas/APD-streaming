from logica import usuario

def imprimir_usuario(usuario):
    print ("CPF: ", usuario[0])
    print ("Nome: ", usuario[1])
    print ("Email: ", usuario[2])
    print ("Senha: ", usuario[3])
    print ("Tipo de conta: ", usuario[4])
    print()

def menu_adicionar():
    print ("\nAdicionar Usuário \n")
    cpf = str(input("CPF: "))
    nome = str(input("Nome: "))
    email = str(input("Email: "))
    senha = str(input("Senha: "))
    tipo = str(input("Tipo de conta: "))
    usuario.adicionar_usuario(cpf,nome,email,senha,tipo)

def menu_registro():
    print("\nCadastro: \n")
    cpf = str(input("CPF: "))
    nome = str(input("Nome: "))
    email = str(input("Email: "))
    senha = str(input("Senha: "))
    tipo = "2"
    usuario.adicionar_usuario(cpf, nome, email, senha, tipo)
    print("Cadastro Realizado com Sucesso!")

def menu_listar():
    print ("\nListar Usuários\n")
    usuarios = usuario.listar_usuarios()
    for u in usuarios:
        imprimir_usuario(u)

def menu_buscar():
    print("\nBuscar Usuário por CPF \n")
    cpf = input("CPF: ")
    u = usuario.buscar_usuario(cpf)
    if (u == None):
        print ("Usuário não encontrado")
    else:
        imprimir_usuario(u)

def menu_remover():
    print ("\nRemover Usuário \n")
    cpf = int(input("CPF: "))
    u = usuario.remover_usuario(cpf)
    if (u == False):
        print ("Usuário não encontrado")
    else:
        print ("Usuário Removido")

def mostrar_menu():
    run_usuario = True
    menu = ("\n---------------\n"+
             "(1) Adicionar novo Usuário \n" +
             "(2) Listar Usuário \n" +
             "(3) Buscar Usuário por CPF \n" +
             "(4) Remover Usúario \n" +
             "(0) Voltar\n"+
            "----------------")
    while (run_usuario):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif (op == 2):
            menu_listar()
        elif (op == 3):
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 0):
            run_usuario = False


