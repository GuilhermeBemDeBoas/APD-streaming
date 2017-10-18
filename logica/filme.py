filmes = []

codigo_geral = 0


def _gerar_codigo():
    global codigo_geral
    codigo_geral += 1
    return codigo_geral


def adicionar_filme(titulo, genero, ano):
    codigo = _gerar_codigo()

    filme = [codigo, titulo, genero, ano]
    filmes.append(filme)


def listar_filmes():
    return filmes


def buscar_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            return f
    return None


def buscar_filme_por_genero(genero):
    for f in filmes:
        if (f[0] == genero):
            return f
    return None


def remover_filme(cod_filme):
    for f in filmes:
        if (f[0] == cod_filme):
            filmes.remove(f)
            return True
    return False


def iniciar_filme():
    adicionar_filme("Star-Wars", "Ficção", 1977)