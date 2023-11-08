print('Escolha o funcao que deseja utilizar:')
x = input('1 - soma\n2 - subtracao\n3 - multiplicacao\n4 - divisao ')
y = input('Digite o primeiro valor ')
z = input('Digite o segundo valor ')
w = float(y) + float(z)
s = float(y) - float(z)
m = float(y) * float(z)
d = float(y) / float(z)
if float(x) == 1:
    print(f'A soma e: {w}')
elif float(x) == 2:
    print(f'A subtracao e: {s}')
elif float(x) == 3:
    print(f'A multiplicacao e: {m}')
elif float(x) == 4:
    print(f'A divisao e: {d}')
