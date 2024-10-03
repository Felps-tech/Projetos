from cmath import *

def funcao(x):
    return 2*x**x**x**x -1

def teorema_do_valor_intermediario():
    while True:
        valor1 = float(input("Digite o primeiro valor do intervalo: "))
        valor2 = float(input("Digite o segundo valor do intervalo: "))
        
        if funcao(valor1) is None or funcao(valor2) is None or funcao(valor1).real * funcao(valor2).real >= 0:
            print("Não é possível aplicar o Teorema do Valor Intermediário neste intervalo.")
            continuar = input("Deseja continuar? (S/N)").upper()
            if continuar != "S":
                break
        else:
            encontrou_raiz = False  
            while abs(valor2 - valor1) > 0.0000000001:
                c = (valor1 + valor2) / 2
                if funcao(c).real == 0:
                    print(f"A raiz da função é: {c}")
                    encontrou_raiz = True 
                    break
                elif funcao(valor1).real * funcao(c).real < 0:
                    valor2 = c
                else:
                    valor1 = c
            
            if not encontrou_raiz:
                print(f"A raiz da função é: {(valor1 + valor2) / 2}")

teorema_do_valor_intermediario()
