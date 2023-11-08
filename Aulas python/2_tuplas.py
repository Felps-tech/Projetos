'''tuplas: COLEÇÃO ORDENADA, IMUTAVEL E QUE PERMITE VALORES DUPLICADOS'''

# tupla é uma lista imutavel
# index     0        1        2        3
tupla = ('item1', 'item2', 'item3', 'item1')
print(tupla)
print(len(tupla))
print(type(tupla))
print(tupla[2])
tupla = 'verde', 'amarelo'
'''reescrever uma variavel pode ser
sem parenteses mas é necessario a virgula'''
print(tupla)

tuplafalsa = ('isso e uma sting apesar dos parenteses')
print(tuplafalsa)
print(type(tuplafalsa))
tupla1 = ('esse e uma tupla porque tem uma virgula no final',)
print(tupla1)
print(type(tupla1))
tupla2 = 'e nem precisa de parenteses',
print(tupla2)
print(type(tupla2))

'''tranformaçao de tupla para lista'''
# alteraçao de tupla (nao recomendado)

tupla0 = 'item1', 'item2'
lista = list(tupla0)
print(tupla0)
print(lista)

lista.append('item3')
print(lista)

tupla0 = tuple(lista)
print(tupla0)

tupla01 = ('a',)
tupla02 = ('b', 'c')

tupla03 = tupla01 + tupla02
print(tupla03)

tupla03 = tupla01 * 3
print(tupla03)

for x in tupla03:
    print(x)

for y in range(len(tupla03)):
    print(y, tupla03[y])

(x, y, z) = tupla03
print('x:', x)
print('y:', y)
print('z:', z)

tupla03 = 1, 2, 3, 4, 5
(x, *y, z) = tupla03
print('x:', x)  # recebe o primeiro
print('y:', y)  # recebe que eu nao quero em forma de lista
print('z:', z)  # recebe o ultimo valor

lista = ['Felps', 4, 3.9, True]
print(type(lista))
tupla3 = tuple(lista)  # tranformador de tuplas
print(tupla3)
print(type(tupla3))
