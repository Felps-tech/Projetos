'''biblioteca: COLEÇAO NAO ORDENADA,
               MUTAVEL E QUE NAO PERMITE
               VALORES DUPLICADOS'''

# chave:valor
dicio = {'nome': 'Gabriel', 'valor_logico': True, 'ano': 1993}
# como escrever um dicionario
print(dicio)

dicio['nome'] = 'Pedro'  # alteraçao de item no dicionario
print(dicio)

dicio['idade'] = 32  # adiçao de nova chave
print(dicio)

dicio.update({'nome': 'Ana'})  # alteracao dicionario
print(dicio)

dicio.update({'estado': 'Rio_de_janeiro'})  # adicao dicionario
print(dicio)

# a funcao popitem elimina o ultimo item apenas da versao 3.7 e acima
# em outras versoes(abaixo de 3.7) eliminava uma chave aleatoria
dicio.popitem()
print(dicio)

dicio.pop('valor_logico')
print(dicio)

del dicio['ano']
print(dicio)

dicio.clear()
print(dicio)

print('---' * 30)

dados = {'nome': 'Rodrigo', 'estado_civil': 'casado'}
print(dados)

for x in dados:  # mostra as chaves
    print(x)

for x in dados.keys():  # mesma coisa
    print(x)

print('---' * 30)

for x in dados:  # mostra os dados
    print(dados[x])

for x in dados.values():  # mesma coisa
    print(x)

print('---' * 30)

for x, y in dados.items():  # ambos(chaves e dados)
    print(x, y)

print('---' * 30)

identidade = dados.copy()  # copiar
print(identidade)

dicio2 = dict(dados)  # copiar
print(dicio2)

dados['idade'] = 27  # nao sofrem alteraçao
print(dados)
print(identidade)
print(dicio2)

print('---' * 30)

dicionario = {  # mesma coisa so que mais ordenada
    'nome': 'Bruna',
    'idade': 27,
    'nacionalidade': 'brasileira'
}
print(dicionario)  # printar o dicionario completo

print(dicionario['idade'])  # printar apenas um conjunto no dicionario

print(dicionario['nome'])

print(dicionario.get('nacionalidade'))

print(dicionario.keys())  # todas as chaves no dicionario

print(len(dicionario))

print(dicionario.values())

if 'idade' in dicionario:
    print(True)
else:
    print(False)

print(dicionario.items())

print('---' * 30)

# index     0        1        2
tupla = ('item1', 'item2', 'item3')
x = 0
dicio = dict.fromkeys(tupla, x)
# tranforma tupla em chaves
# e o 'x' em valor de todas as chaves
print(dicio)

nario = {
    'nario1': {
        'nome': 'Carlos',
        'idade': 22,
        'nacionalidade': 'americano'
    },
    'nario2': {
        'nome': 'Gemma',
        'idade': 19,
        'estado_civil': 'casada',
        'nario3': {
            'nome': 'Felps',
            'idade': 18,
            'caracteristica': 'marido_Gemma'
        }
    }
}

print(nario)
