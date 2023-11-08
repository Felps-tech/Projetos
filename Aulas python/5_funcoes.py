# Paradigma Imperativo | Sequencial
# imperare

# variaveis, atribuicoes e sequencia
# C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2

# bloco externo
nome = "Gabriel"  # variavel global


def minha_funcao():  # bloco interno
    nome = 'Ana'
    tupla = 2, 5, 6, 7, 9
    print(nome)
    print(tupla)
    if nome == 'Ana':
        print("Impressao do bloco interno da condicao if")
    for x in tupla:
        print(x)


print(nome)
minha_funcao()


lista = [1, 2, 3, 4, 5]
print(lista)

retorno = lista.pop()
var1 = print('Hello World')
print(lista)
print("O retorno da funcao pop:", retorno)
print('O retorno da funcao print:', var1)  # sem retorno


def ola_mundo():
    print('ola mundo')


def Hello_World():
    return ('Hello World')


print(var1)
ola_mundo()  # com retorno
Hello_World()  # sem retorno
retorno = Hello_World()  # com retorno
print(retorno)
print(Hello_World())  # com retorno


def par_ou_impar():  # funcao pass evita erros
    numero = 4
    if (numero % 2) == 0:
        return 'Numero Par'
    return 'Numero Impar'


print(par_ou_impar())
