from logica import filme
from logica import usuario

filmes_assistidos = []

def registrar_filme_assistido(cod_filme,cpf):
    f = filme.buscar_filme(cod_filme)
    u = usuario.buscar_usuario(cpf)
    
    

def listar_filmes_assistidos(cpf):
    pass

def avaliar_filme(cod_filme,cpf,nota):
    cod_filme = filme.buscar_filme(cod_filme)
    cpf = usuario.buscar_usuario(cpf)
    for i in usuarios:
        if (usuario[i][0])==cpf:
            usuario[i][5].append(nota)
            
def assistir_filme(cod_filme, cpf):
    cpf = usuario.buscar_usuario(cpf)
    cod_filme = filme.buscar_filme(cod_filme)
    historico.registrar_filme_assistido(cod_filme,cpf)
