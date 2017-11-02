from logica import usuario
from logica.usuario import usuarios
from gui import interface_usuario
from gui import menu_filme
from logica import filme
from gui import menu_usuario

def login():
    j = True
    while j == True:
        email = input("E-mail: ")
        senha = input("Senha: ")
        for i in usuarios:
            if(i[2] == email):
                # print("foi 1")
                if(i[3] == senha):
                    j = False
                    # print("foi 2")
                    if(i[4] == "1"):
                        interface_usuario.mostrar_menu()
                    else:
                        tipo = "2"
                        menu_filme.mostrar_menu(tipo)
        if(j == True):
            print("\nUsuario ou senha incorretos.\n ")

def principal():
    a = True
    while a == True:
        print("(1) Login")
        print("(2) Cadastro")
        print("(0) Fechar o programa")
        escolha = input("Digite a operacao desejada: ")

        if (escolha == "1"):
            login()
        elif (escolha == "2"):
            menu_usuario.menu_registro()
        elif (escolha == "0"):
            break
        else:
            a == True

# def teste():
#     n = 0
#     file = open("teste.txt", "r")
#     aux = file.readlines(n)
#     # print(aux)
#     for h in aux:
#
#         usuarios.append(aux[n][1:len(aux[n])-2].split(", "))
#
#         n = n + 1
#     print(usuarios)

    # interface_usuario.mostrar_menu()

if __name__ == "__main__":
    # teste()
    usuario.iniciar_usuarios()
    filme.iniciar_filme()
    # filme._gerar_codigo()
    principal()