from logica import usuario
from logica.usuario import usuarios
from gui import interface_usuario
from gui import menu_filme
from logica import filme

def principal():
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