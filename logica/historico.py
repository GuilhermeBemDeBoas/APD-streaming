from logica import filme
from logica import usuario

filmes_assistidos = []

def registrar_filme_assistido(cod_filme,cpf):
    f = filme.buscar_filme(cod_filme)
    u = usuario.buscar_usuario(cpf)
    
    

def listar_filmes_assistidos(cpf):
    pass

