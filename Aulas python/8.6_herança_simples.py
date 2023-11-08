class Pessoa:
    
    # SuperClasse
    
    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print('Classe Pessoa')
        
        
    def imprimir_nome(self):
        return f'Estou retornando o valor armazenado na variavel nome {self.nome}'

#Herança da Super Classe
class Aluno(Pessoa):

    # SubClasse

    def __init__(self, nome):
        # Pessoa.__init(self, nome)
        # super() não precisa de self
        # super() - chama a classe herdada - Super Classe
        super().__init__(nome) # __init__ da classe Pessoa
        self.matricula = None
        self.notas = []
        print('Classe Aluno')
        
    '''def __init__(self):            __init__ da classe Aluno
        self.nome = None
        self.data_nascimento = None
        self.cpf = None
        self.rg = None
    '''

    def estudar(self):
        return 'Estudando...'

#Herança da Super Classe
class Professor(Pessoa):
     
    # SubClasse
    
    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []
        print('Classe Professor')
        
    '''def __init__(self):
        self.nome = None
        self.data_nascimento = None
        self.cpf = None
        self.rg = None
    '''
        
    def lecionar(self):
        return 'Ensinando...'

print('---' * 30)

aluno1 = Aluno('Felps')
print(aluno1.imprimir_nome()) # Atributos de outra classe

print('---' * 30)

professor1 = Professor('Fermat')
print(professor1.imprimir_nome()) # Atributos de outra classe

print('---' * 30)

pessoa1 = Pessoa('Rodrigo')
print(pessoa1.imprimir_nome()) # Atributos de outra classe

print('---' * 30)
