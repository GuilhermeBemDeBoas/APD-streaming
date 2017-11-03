from logica import filme
from logica import usuario

historicos = []

def registrar_filme_assistido(cod_filme,cpf):
    cliente = usuario.buscar_usuario(cpf)
    fil = filme.buscar_filme(cod_filme)
    historico = [cliente,fil]
    
    historicos.append(historico)    

def listar_filmes_assistidos(cpf):
    for h in historicos:
        if (h[0][0] == cpf):
            return h

