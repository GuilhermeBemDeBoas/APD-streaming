from logica import filme
avaliacoes = []

def avaliar_filme(cod_filme, cpf, nota):
    from logica import usuario
    from logica import historico
    avaliacao = [cod_filme, cpf, nota]
    avaliacoes.append(avaliacao)


def assistir_filme(cod_filme, cpf):
    from logica import usuario
    from logica import historico
    cpf = usuario.buscar_usuario(cpf)
    cod_filme = filme.buscar_filme(cod_filme)
    print("Iniciando Filme..")
    nota = int(input("Uma nota de 0 a 10: "))
    avaliar_filme(cod_filme, cpf, nota)
    historico.registrar_filme_assistido(cod_filme, cpf)




