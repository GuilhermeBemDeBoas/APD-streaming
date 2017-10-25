# from logica import usuario
from gui import menu_usuario
# from logica import filme
from gui import menu_filme

# def inicializar_dados():
    # usuario.iniciar_usuarios()
    # filme.iniciar_filme()

def mostrar_menu():
    run_menu = True

    # inicializar_dados()

    menu = ("\n----------------\n"+
             "(1) Menu Usuário \n" +
             "(2) Menu Filme \n" +
             "(0) Sair\n" +
             "-----------------")
    while(run_menu):
        print (menu)

        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_usuario.mostrar_menu()
        elif (op == 2):
            menu_filme.mostrar_menu(tipo=1)
        elif (op == 0):
            print ("Saindo do programa...")
            run_menu = False
        else:
            print ("Valor invalido")
