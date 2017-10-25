from logica import usuario
from logica.usuario import usuarios
from gui import interface_usuario
from gui import menu_filme
from logica import filme

def principal():
    j = True
    while j == True:
        email = input("email: ")
        senha = input("Senha: ")
        for i in usuarios:
            if(i[2] == email):
                # print("foi 1")
                if(i[3] == senha):
                    j = False
                    # print("foi 2")
                    if(i[4] == 1):
                        interface_usuario.mostrar_menu()
                    else:
                        tipo = 2
                        menu_filme.mostrar_menu(tipo)
        if(j == True):
            print("\nUsuario ou senha incorretos.\n ")




    # interface_usuario.mostrar_menu()

if __name__ == "__main__":
    usuario.iniciar_usuarios()
    filme.iniciar_filme()
    principal()