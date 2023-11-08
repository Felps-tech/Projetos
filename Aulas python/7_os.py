import os

print(os.name)

# Verificar se um arquivo existe
print(os.path.exists('texto.py'))
print(os.path.exists('texto.txt'))

# Verifica se um diretório existe
print(os.path.exists('carlos'))
print(os.path.exists('pastanova'))

# Exemplo de caminhos
print(os.path.exists('pastanova/texto.py'))

# Criando diretório
os.mkdir('diretorio criado')

# Deletando diretório   
os.rmdir('diretorio criado')
   
# Renomeando arquivos e diretórios
'''
os.rename('texto.txt', 'ola mundo.txt')
os.rename('ola mundo.txt', 'texto.txt')
'''