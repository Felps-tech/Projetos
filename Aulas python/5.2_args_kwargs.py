# Argumento arbitrario *args

# | obrigatorio | obrigatorio | nao obrigatorio | argumento arbitrario


def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None, *args):
    print('---' * 30)
    print('Titulo: ', nomeImovel)
    print('Numero de Quartos ', n_quartos)
    if vagasGaragem is not None:
        print('Vagas na garagem ', vagasGaragem)


imprimir_imovel('Casa 3 Quartos - SP', 3)
imprimir_imovel('Apartamento - MG', 2, 1, 'Desconto')

# args = Essa funcao recebe argumentos que nao serão atribuidos em tuplas
print('---' * 30)


def imprimir_nomes(*nomes):
    print(nomes)


# cria-se uma tupla
imprimir_nomes('ana', 'beatriz', 'carla1')

# lista em tupla
lista = ['ana', 'beatriz', 'carla2']
imprimir_nomes(lista)

# lista | desempacotamento
lista = ['ana', 'beatriz', 'carla3']
imprimir_nomes(*lista)


def imprimir_sobrenomes(sobrenomes):
    print(sobrenomes)


lista2 = ['silva', 'pereira', 'angelico']
imprimir_sobrenomes(lista2)

# **kwargs = Keyword Arguments
# Essa funcao recebe argumentos que serao atribuidos em um dicionario


'''def imprimir_nomes(**kwargs):
    print(kwargs)
'''


def imprimir_nomes(**nomes):
    print(nomes)


imprimir_nomes(nomes='ana', sobrenomes='julia', idade=10)
