'''sets: Colecao nao ordenada, imutavel e que nao permite valores duplicados
   conhecido tambem como conjunto
'''

conjunto = {'item1', 'item2', 'item3'}
print(type(conjunto))  # a ordem nao vai estar certa
print(conjunto)  # nao ordenada
print(len(conjunto))

conjunto1 = {1, 4.3, False, 'Valorant', 1}  # nao permite valor duplicados
print(conjunto1)

tupla = (3, 7, 9, 5)
print(type(tupla))
conjunto2 = set(tupla)  # transformador de set
print(conjunto2)
print(type(conjunto2))

conjunto3 = {'item1', 'item2', 'item3', 'item4'}
for x in conjunto3:
    print(x)

conjunto4 = {1, 4, 2, 5, 9}
print(2 in conjunto4)  # true
print(6 in conjunto4)  # false

conjunto5 = {1, 2, 3, 4, 5, 6}
print(conjunto5)

conjunto5.add(7)  # adiciona um elemento
print(conjunto5)

conjunto6 = {'Overwatch', 'LeagueOfLegends', 1, 4, 9}  # adiciona um set
conjunto5.update(conjunto6)
print(conjunto5)

conjunto5.remove('Overwatch')  # remove um elemento
print(conjunto5)

conjunto5.intersection_update(conjunto6)  # intersecçao de dois sets
print(conjunto5)

conjunto5.symmetric_difference_update(conjunto6)
print(conjunto5)  # valores que nao tem em ambos

conjunto5.pop()  # remove um valor aleatorio
print(conjunto5)

conjunto6.remove('Overwatch')  # remove um valor especificado
print(conjunto6)

conjunto6.discard('Overwatch')  # remove um valor mesmo nao existente
print(conjunto6)

conjunto6.clear()  # limpa o set
print(conjunto6)

conjunto7 = {'Roberto_Carlos', 1, 2.4, 2}
conjunto8 = {'Galvao_Bueno', 1, 3.5, 4}

conjunto9 = conjunto7.union(conjunto8)
print(conjunto9)

conjunto10 = conjunto7.intersection(conjunto8)
print(conjunto10)

conjunto11 = conjunto7.symmetric_difference(conjunto8)
print(conjunto11)
