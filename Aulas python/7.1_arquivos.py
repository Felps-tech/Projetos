arquivo = open('receita.txt')
print(arquivo.closed)
print('---' * 30)
print(arquivo.read())
print('---' * 30)
arquivo2 = open('./receita/brigadeiro.txt')
print(arquivo2.readline())
print(arquivo2.readline())
print(arquivo2.readline())
print(arquivo2.readline())
print('---' * 30)
print(arquivo2.read())
print('---' * 30)
print(arquivo2.closed)
arquivo2.close()
print(arquivo2.closed)
#                                   readable
with open('./receita/brigadeiro.txt', 'r') as arquivo3:
    print(arquivo3.read())
    print(arquivo3.closed)
print(arquivo3.closed)
#                    writeable
with open('texto.txt', 'w') as texto:
    texto.write('rodrigo')
    texto.close()
    
    texto_super_foda = ' CARALHOOOOO'
#                   appendable
with open('texto.txt', 'a') as texto:
    texto.write(texto_super_foda)
    texto.close()
    
# wb  write binary