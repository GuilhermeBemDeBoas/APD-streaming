filmes = []

codigo_geral = 0


def _gerar_codigo():
    # global codigo_geral
    # codigo_geral += 1
    # return codigo_geral

    file = open("codigo.txt", "r")
    cod = int(file.read())
    # print(cod, "CODIGO")
    cod = cod + 1
    # print(cod)
    file.close()
    file = open("codigo.txt", "w")
    file.write(str(cod))
    return str(cod)


def adicionar_filme(titulo, genero, ano):
    codigo = str(_gerar_codigo())
    filme = [codigo, titulo, genero, ano]
    filmes.append(filme)
    file = open("filme.txt", "a")
    file.writelines("[" + codigo + ", " + titulo + ", " + genero + ", " + ano + "]\n")


def listar_filmes():
    return filmes


def buscar_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            return f
    return None


def buscar_filme_por_genero(genero):
    for f in filmes:
        if (f[2] == genero):
            return f


def remover_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            filmes.remove(f)
            return True
    return False


def iniciar_filme():
    n = 0
    file = open("filme.txt", "r")
    aux = file.readlines(n)
    for h in aux:
        filmes.append(aux[n][1:len(aux[n]) - 2].split(", "))

        n = n + 1
    # print(filmes)
#     adicionar_filme("Star-Wars", "Ficção", 1977)