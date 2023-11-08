# Polimorfismo - só existe com herança
# Execução da mesma função de formas diferentes

class Pessoa:
    
    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        
        
    def imprimir_nome(self):
        return f'Estou retornando o valor armazenado na variavel nome {self.nome}'
    
    # Não é necessario a escrita desse codigo - mas se for escrito passará pela classe pessoa
    '''def trabalhar(self): # MOLDE
        print('Trabalhando...') # NÃO SERA IMPRESSO POIS OUVE A SOBREPOSIÇÃO 
    '''
class Administrador(Pessoa):

    def trabalhar(self): # TRABALHO DO ADMINISTRADOR
        nome_classe = self.__class__.__name__
        return f'Classe {nome_classe} Organizando Planilhas...'

class Professor(Pessoa):
     
    
    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []
        
    def trabalhar(self): # TRABALHO DO PROFESSOR
        nome_classe = self.__class__.__name__
        return f'Classe {nome_classe} Ensinando...'


class Aluno(Pessoa):

    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = []

    def estudar(self):
        return 'Estudando...'


professor1 = Professor('Marcos')
administrador1 = Administrador()
print(professor1.trabalhar())
print(administrador1.trabalhar())