from logica import filme
from logica import usuario
from logica import historico




def avaliar_filme(cod_filme, cpf, nota):
    cod_filme = filme.buscar_filme(cod_filme)
    cpf = usuario.buscar_usuario(cpf)
    usuarios = usuario.listar_usuarios()
    for i in usuarios:
        if (usuario[i][0] == cpf):
            usuario[i][5].append(nota)


def assistir_filme(cod_filme, cpf):
    cpf = usuario.buscar_usuario(cpf)
    cod_filme = filme.buscar_filme(cod_filme)
    nota = int(input("Uma nota de 0 a 10: "))
    avaliar_filme(cod_filme, cpf, nota)
    historico.registrar_filme_assistido(cod_filme, cpf)


def menu_assistir():
    cpf = int(input("Seu CPF: "))
    c = filme.assitir_filme(cpf)
    cod_filme = int(input("Codigo: "))
    f = filme.assistir_filme(cod_filme)
    if (f == False):
        print("Filme não encontrado")
    else:
        print("Iniciando Filme..")
        menu_avaliar()


def menu_avaliar():
    cpf = int(input("Seu CPF: "))
    c = filme.avaliar_filme(cpf)
    cod_filme = int(input("Codigo: "))
    f = filme.avaliar_filme(cod_filme)
    nota = int(input("Que nota voce da para esse filme de 1 a 5"))
    if nota < 1 or nota > 5:
        nota = int(input("Que nota voce da para esse filme de 1 a 5"))
    n = filme.avaliar_filme(nota)