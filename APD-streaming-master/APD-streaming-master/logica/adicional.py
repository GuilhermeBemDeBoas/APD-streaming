from logica import filme
from logica import usuario
from logica import historico

def avaliar_filme(cod_filme,cpf,nota):
    cod_filme = filme.buscar_filme(cod_filme)
    cpf = usuario.buscar_usuario(cpf)
    for i in usuarios:
        if (usuario[i][0])==cpf:
            usuario[i][5].append(nota)
def assistir_filme(cod_filme):
    cod_filme = filme.buscar_filme(cod_filme)
    adicional.avaliar_filme(cod_filme,cpf,nota)
    historico.registrar_filme_assistido(cod_filme,)
