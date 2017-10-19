from logica import usuario
from gui import menu_usuario

def inicializar_dados():
    usuario.iniciar_usuarios()

def mostrar_menu():
    run_menu = True

    inicializar_dados()

    menu = ("\n----------------\n"+
             "(1) Menu Usuário \n" +
             "(0) Sair\n" +
             "-----------------")
    while(run_menu):
        print (menu)

        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_usuario.mostrar_menu()
        elif (op == 0):
            print ("Saindo do programa...")
            run_menu = False
        else:
            print ("Valor invalido")
