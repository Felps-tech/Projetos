def funcao(x):
    return x**2 + x

def teorema_do_valor_intermediario():
    valor1 = float(input("Digite o primeiro valor do intervalo "))
    valor2 = float(input("Digite o segundo valor do intervalo "))
    if (funcao(valor1) * funcao(valor2)) >= 0:
        print("Não é possível aplicar o Teorema do Valor Intermediário neste intervalor.")
        continuar = input("Deseja continuar? (S,N)").upper()
        if continuar == "S":
            teorema_do_valor_intermediario()
        else:
            return
    while abs(valor2 - valor1) > 0.00001:
        c = (valor1 + valor2)/2
        if funcao(c) == 0:
                return print(f"A raiz da funcao é: {c}")
        elif funcao(valor1) * funcao(c) < 0:
            valor2 = c
        else:
            valor1 = c  
    return print(f"A raiz da funcao é: {(valor1 + valor2)/2}")

teorema_do_valor_intermediario()