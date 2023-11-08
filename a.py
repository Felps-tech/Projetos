quant,i,X,XS = 2,0,0,0
lista = []
def calcular_quant(lista,index,valor,quant,quantS):
    for index in lista:
        if index[0] == valor:
            quant += 1
            if index[3] == "S":
                quantS += 1
while i < quant: 
    geracao = str(input("Informe sua geracao. (X, Y, Z) ")).upper()
    sexo = str(input("Informe seu sexo. (M, F) ")).upper()
    pratica = str(input("Pratica ou Praticou futebol? (S, N) ")).upper()
    ganhar = str(input("O Brasil vai ganhar em 2026? (S, N) ")).upper()
    lista.append([geracao, sexo, pratica + "P", ganhar])
    i+=1

C = calcular_quant(lista,0,"X",X,XS)
print(C)

        