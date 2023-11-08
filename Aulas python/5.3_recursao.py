# reducao de um numero inteiro de um em um

def reduzir_numero(numeroInt):
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1


reduzir_numero(10)

'''
1 - checar se o nosso numero nao é igual a 0
2 - se ele não for igual a 0 - reduzir 1

5 (N - 1)
  4 (5 - 1)
    3 (4 - 1)
      2 (3 - 1)
        1 (2 - 1)
          0 (1 - 1)
'''


def reduzir(numero):
    print(numero)
    if numero > 0:
        # N - 1
        reduzir(numero - 1)
        print(numero)


reduzir(10)

print('---' * 30)

# Fatorial Sem Recurção


def fatorialS(valor):
    fatorial = 1
    if valor == 0:
        return 1
    else:
        for x in range(1, valor + 1):
            fatorial *= x
        return fatorial


print(fatorialS(0))
print(fatorialS(4))

# Fatorial Solução Recursiva


def fatorialR(valor):
    if valor == 0:  # Critério de parada
        return 1
    else:
        # Parâmetro de chamada recursiva
        return valor * fatorialR(valor - 1)


print(fatorialR(5))
