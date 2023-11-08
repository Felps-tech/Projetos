x = int(input('Digite o primeiro valor '))
y = int(input('Digite o segundo valor '))
z = int(input('Digite o terceiro valor '))
w = int(input('Digite o quarto valor '))
m = 0
n = 0

if x > y and x > z and x > w:
    m = x
elif y > x and y > z and y > w:
    m = y
elif z > x and z > y and z > w:
    m = z
else:
    m = w

if x < y and x < z and x < w:
    n = x
elif y < x and y < z and y < w:
    n = y
elif z < x and z < y and z < w:
    n = z
else:
    n = w

print(f'O maior numero eh: {m}')
print(f'O menor numero eh: {n}')
