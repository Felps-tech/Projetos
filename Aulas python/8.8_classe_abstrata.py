'''
Classe concreta: São classes que são criados objetos dessa classe para fazer métodos dentro da classe

Classe abstrata: Uma Classe Abstrata pode ser considerada um projeto para outras classes.
Ela permite que você crie um conjunto de métodos que devem ser criados em qualquer subclasse construída a partir da classe abstrata. 

'''
#          CLASSE ABSTRATA
from abc import ABC, abstractmethod

# Classe abstrata
class Pessoa(ABC): #Necessita herdar de uma classe abstrata
    
    def __init__(self, nome=None, data=None, cpf=None, rg=None): #Métodos concretos
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print('Executando o construtor da classe pessoa')
        
        
    def imprimir_nome(self):
        return self.nome
    
    @abstractmethod  # Método abstrato | MOLDE
    def trabalhar(self):
        print('Implemente a funcionalidade deste método')

# Classe concreta
class Administrador(Pessoa):

    def trabalhar(self):
        return super().trabalhar()
    
# Classe concreta
class Professor(Pessoa):
     
    
    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []
        
    def trabalhar(self): # TRABALHO DO PROFESSOR
        nome_classe = self.__class__.__name__
        print(f'Classe {nome_classe} Ensinando...')
    
# Classe concreta
class Aluno(Pessoa):

    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = []

    def estudar(self):
        return 'Estudando...'

professor1 = Professor('Marcos')
administrador1 = Administrador()
administrador1.trabalhar()
professor1.trabalhar()

