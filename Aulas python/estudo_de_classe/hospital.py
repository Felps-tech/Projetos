from datetime import date

class Paciente:
    
    def __init__(self, nome, idade, cpf, email):
        print('Construtor')
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        
    
    @classmethod
    def idadeAnoNascimento(cls, nome, anoNascimento, cpf, email):
        idade = date.today().year - anoNascimento
        #   Paciente  - pode ser alterado pelo nome da classe
        return cls(nome, idade, cpf, email)
        
class Medico:
    pass


'''paciente = Paciente('Mona lisa', 20, '000.000.000-00', 'mona@gmail.com')
print(paciente.__dict__)
print(Paciente.idadeAnoNascimento(2003))'''

paciente = Paciente.idadeAnoNascimento('Mona lisa', 1922, '000.000.000-00', 'mona@gmail.com')
print(paciente.__dict__)
print(paciente.idade)