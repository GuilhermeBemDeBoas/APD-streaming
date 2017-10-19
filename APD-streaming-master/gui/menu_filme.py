from logica import filme

def imprimir_usuario(filme):
    print ("Titulo: ", usuario[0])
    print ("Genero: ", usuario[1])
    print ("Ano: ", usuario[2])
    print()

def menu_adicionar():
    print ("\nAdicionar Filme \n")
    titulo = str(input("Titulo: "))
    Genero = str(input("Genero: "))
    email = int(input("Ano: "))
    filme.adicionar_filme(titulo, genero, ano)

def menu_listar():
    print ("\nListar Filmes\n")
    filme = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)

def menu_buscar():
    print("\nBuscar Filme por Codigo \n")
    codigo = int(input("Codigo: "))
    f = filme.buscar_filme(cod_filme)
    if (f == None):
        print ("Filme não encontrado")
    else:
        imprimir_filme(f)

def menu_buscar_genero():
    ():
    print("\nBuscar Filme por Genero \n")
    codigo = int(input("Genero: "))
    f = buscar_filme_por_genero(genero)
    if (f == None):
        print ("Filme não encontrado")
    else:
        imprimir_filme(f)
        
def menu_remover():
    print ("\nRemover Filme \n")
    codigo = int(input("Codigo: "))
    f = filme.remover_filme(cod_filme)
    if (f == False):
        print ("Filme não encontrado")
    else:
        print ("Filme Removido")

def mostrar_menu():
    run_usuario = True
    menu = ("\n---------------\n"+
             "(1) Adicionar novo Filme \n" +
             "(2) Listar Filmes \n" +
             "(3) Buscar Filme por codigo \n" +
             "(4) Buscar Filme por genero \n" +
             "(5) Remover Filme \n" +
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
