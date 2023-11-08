# Paramentros de funcoes

# parametro é os valores utilizados na definicao de uma função
def minha_funcao():
    # corpo da função
    var = 'maria'
    return var


var = minha_funcao()
print(var)


def nome_da_funcao(parametro):
    # corpo da funcao
    print('ola', parametro)


parametro = input('Qual o seu nome? ')
nome_da_funcao(parametro)
# argumento é o nome utilizado na chamada de uma funçâo

print('---' * 30)


def imprime_rg(nome, sobrenome):
    print(f'Olá, {nome} {sobrenome}')


imprime_rg(nome='rodrigo', sobrenome='augusto')
# se colocar mais argumentos nao funciona

print('---' * 30)


def imprime_noso(nome=None, sobrenome=None):
    if nome is not None:
        print('nome: ', nome)
        print('sobrenome ', sobrenome)
        print('---' * 30)
    else:
        print('Digite os seus dados')


imprime_noso()
print('---' * 30)
imprime_noso('Gemma', 'de Paula')

# Parametro Padrao - Define argumentos nao obrigatorios

# definicao da funcao| obrigatorio | obrigatorio | nao obrigatorio |


def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None):
    print('---' * 30)
    print('Titulo: ', nomeImovel)
    print('Numero de Quartos ', n_quartos)
    if vagasGaragem is not None:
        print('Vagas na garagem ', vagasGaragem)


# exemplos de n argumentos <= n dos parametros
imprimir_imovel('Casa 3 Quartos - SP', 3)
imprimir_imovel('Apartamento - MG', 2, 1)

# exemplo de n argumentos > n dos parametros
'''imprimir_imovel('Loja Comercial', 2, 5, 'Desconto')'''
