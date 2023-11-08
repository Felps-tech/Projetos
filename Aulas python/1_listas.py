'''lista: COLEÇÃO ORDENADA, MUTAVEL E QUE PERMITE VALORES DUPLICADOS'''

# index     0        1       2         3        4
# index (-) -5       -4      -3        -2       -1
lista = ['felps', 'tiago', 'joao', 'natally', 'caua']

print(type(lista))    # mostra o tipo da lista
print(lista.count('felps'))   # conta o tanto de vezes que 'felps' foi escrito

print(lista[1])    # mostra o elemento de index 1
print(lista[-5])    # mostra o elemento com index -5, inverte a ordem
print(lista[::])    # imprime a lista inteira
print(lista[1:])    # imprime do 1 ate o ultimo index
print(lista[:4])    # imprime do primeiro ate o terceiro(quarto elemento) index
print(lista[2:4])   # imprime do segundo ate o terceiro(quarto elemento) index
print(len(lista))    # tamanho da lista lenght

for x in lista:
    # interavel com a lista, detecta se existe algo na lista e imprime
    print(x)
for x in range(len(lista)):
    # interavel com a lista, range(x) analisa o 1 elemento até o elemento x-1
    print(x, lista[x])    # mostra o numero do index de cada elemento
nome = 'lista'

print(nome[2:4])    # funciona com string
lista2 = [1, 2, 3, 5, 7, 11]

print(lista2)
lista3 = [1.4, 3.7, 5, 7.2, 9.0, 11.42, 13.1]

print(lista3)
somadelista = lista2 + lista3
# soma de duas lista, pode ser trocado por lista2 = lista2 + lista3

print(somadelista)

print(sum(lista2))    # soma de todos os numeros não necessariamente inteiros
print(sum(lista3))

print(max(lista2))    # mostra o maior numero da lista
print(max(lista3))

print(min(lista2))    # mostra o menor numero da lista
print(min(lista3))

lista2[0] = 4
# mudança de elemento em uma lista em base do index
print(lista2)
lista2[1:] = [2, 5, 3, 8, 10]
# mudança de varios elementors
print(lista2)
lista2[1:2] = [7, 8, 69]
# mudança de um numero maior do que os espaços escolhidos
print(lista2)
# ocorre apenas o aumento da lista em base do index selecionado
lista2[1:6] = [18]
# mudança de um numero menor que os espaços escolhidos
print(lista2)
# ocorre a remoçao dos indexes selecionados

nome = 'lista no python'
valor = range(10)
elemento = 'i'

print(nome)
print(valor)    # imprime a função literal

print(list(valor))    # imprime a função em forma de lista
print(list(nome))

if elemento in nome:
    print('elemento esta em nome')

# index       0        1        2
lista5 = ['gemma', 'davi', 'lorrayne']    # criação de lista
print(lista5)
lista5.append('natan')    # adiciona apenas um elemento
print(lista5)
lista5.append(['leo', 'ju'])
# toda lista é um elemento, apesar de haver mais de um elemente dentro
print(lista5)
lista5.extend(['caua', 'vini'])
# adiciona mais de um elemento dentro da lista
print(lista5)
lista5.remove('natan')    # remove por nome na lista
print(lista5)
lista5.remove(['leo', 'ju'])
# remove a lista, apenas funciona se digitar a lista inteira
print(lista5)
lista5.pop(2)    # remove por index // pop() remove o ultimo
print(lista5)
lista5.sort()
# ordena em ordem alfabetica ou de tamanho(se for inteiro/float)
print(lista5)
lista5.sort(reverse=True)    # inverte a lista
print(lista5)

lista4 = ['Ana', 'Debora', 'Gemma', 'Elisa', 'beatriz']
print(lista4)
lista4.sort()
# separa as listas em letra maiuscula e minuscula e ordem alfabetica
print(lista4)
lista4.sort(key=str.lower)
# trata todos os elementos em minusculo e separa mas nao deixa minusculo
print(lista4)

copia1 = [1, 2, 3]
copia2 = copia1
print(copia1)
print(copia2)
copia1.append(4)
# se duas lista se copiam ambas vao receber as mesmas alteraçoes independente
print(copia1)
print(copia2)
copia2.append(5)
print(copia1)
print(copia2)

copia3 = ['a', 'b', 'c']
copia4 = copia3.copy()
print(copia3)
print(copia4)
copia3.append('d')    # nesse a lista 4 copia a 3 e nao iguala em ambos
print(copia3)
print(copia4)
copia4.append('e')
print(copia3)
print(copia4)


del lista5[3]    # deleta index 3
print(lista5)
lista5.clear()   # remove todos os elementos
print(lista5)

texto = 'carro e avião'
print(list(texto))

texto = texto.split(' ''e'' ')    # imprime separado por espaço 'e' espaço
print(texto)

tupla = (2, 4, 1, 6)
print(type(tupla))
lista6 = list(tupla)  # transformador de lista
print(lista6)
print(type(lista6))
