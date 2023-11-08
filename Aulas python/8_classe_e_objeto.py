# Paradigma orientado à objetos

'''
Classe concreta - Um conjunto de objetos com as mesmas caracteristicas
Objeto - Representação do mundo real como um tipo de dado de uma classe
Construtor - É uma função criada implicitamente com o mesmo nome da classe
Atributo - São as variáveis de uma classe
'''
# self - objeto que se refere a si mesmo
class Paciente:
    
    def __init__(self, nome, idade, cpf, email):
        print('Construtor')
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email


'''

Simulação de Eventos Discretos -> Paradigma Orientado à Objetos

Relação -> Destacando funções e variáveis

------------------------------------------------------

Conceitos Estruturais

-Classe

Classe é uma estrutura que abstrai um conjunto de objetos com características
similares. Definindo o comportamento dos seus objetos através das estruturas:

1- Atributos
2- Métodos

A classe define um tipo de dado abstrato

- Objeto

Um objeto é a representação de um conceito/entidade do mundo real,
que pode ser física ou conceitual e possui um significado bem definido
para um determinado software

'''

# Abstração
# Reúso e a Coesão
# Acoplamento, herança, polimorfismo, GAP semântico

'''

Conceitos Fundamentais

-Abstração

Processo pelo qual se isolam atributos de um objeto,
considerando os que certos grupos de objetos tenham em comum

-Reúso

Não existe Prática em programação do que repetir código

'''