from logica import filme

def imprimir_filme(filme):
    print ("Titulo: ", filme[1])
    print ("Genero: ", filme[2])
    print ("Ano: ", filme[3])
    print("Codigo: ", filme[0])
    print()

def menu_adicionar():
    print ("\nAdicionar Filme \n")
    titulo = str(input("Titulo: "))
    genero = str(input("Genero: "))
    ano = str(input("Ano: "))
    filme.adicionar_filme(titulo,genero,ano)

def menu_listar():
    print ("\nListar Filmes\n")
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)

def menu_buscar():
    print("\nBuscar Filme por Codigo \n")
    cod_filme = (input("Codigo: "))
    f = filme.buscar_filme(cod_filme)
    if (f == None):
        print ("Filme não encontrado")
    else:
        imprimir_filme(f)

def menu_buscar_genero():
    print("\nBuscar Filme por Genero \n")
    g = str(input("Genero: "))
    f = filme.buscar_filme_por_genero(g)
    if (f == None):
        print ("Filme não encontrado")
    else:
        imprimir_filme(f)
        
def menu_remover():
    print ("\nRemover Filme \n")
    cod_filme = (input("Codigo: "))
    f = filme.remover_filme(cod_filme)
    if (f == False):
        print ("Filme não encontrado")
    else:
        print ("Filme Removido")

def menu_assistir():
    from logica import adicional
    cpf = int(input("Seu CPF: "))
    cod_filme = int(input("Codigo: "))
    f = adicional.assistir_filme(cod_filme, cpf)


def mostrar_menu(tipo):
    run_filme = True
    if(tipo == "2"):

        menu = ("\n---------------\n" +
                "(1) Listar Filmes \n" +
                "(2) Buscar Filme por codigo \n" +
                "(3) Buscar Filme por genero \n" +
                "(4) Assistir Filme \n" +
                "(0) Sair\n" +
                "----------------")
        while (run_filme):
            print(menu)
            op = int(input("Digite sua escolha: "))

            if (op == 1):
                menu_listar()
            elif (op == 2):
                menu_buscar()
            elif (op == 3):
                menu_buscar_genero()
            elif (op == 4):
                menu_assistir()

            elif (op == 0):
                run_filme = False




    else:
        menu = ("\n---------------\n" +
                "(1) Adicionar novo Filme \n" +
                "(2) Listar Filmes \n" +
                "(3) Buscar Filme por codigo \n" +
                "(4) Buscar Filme por genero \n" +
                "(5) Remover Filme \n" +
                "(0) Voltar\n" +
                "----------------")

        while (run_filme):
            print(menu)
            op = int(input("Digite sua escolha: "))

            if (op == 1):
                menu_adicionar()
            elif (op == 2):
                menu_listar()
            elif (op == 3):
                menu_buscar()
            elif (op == 4):
                menu_buscar_genero()
            elif (op == 5):
                menu_remover()
            elif (op == 0):
                run_filme = False
