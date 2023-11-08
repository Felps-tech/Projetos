'''
Nivel de herança: A quantidade de classes que são herdadas
class(Administrado) -> class(Pessoa) -> class(ABC)

Recomendado no máximo 4 heranças
'''

class Funcionario:
    # SE AMB0S NÃO HOUVER def trabalhar SERA REALIZADO NA ULTIMA HERANÇA
    def trabalhar(self):
        print('Trabalhando...')

class FrontEnd(Funcionario):
    
    def trabalhar(self):
        print('FrontEnd')
    '''
    def frontend(self):
        print('FrontEnd')  NÃO HAVERA CONFLITO POR É UM MÉTODO DIFERENTE
    '''
        
    '''pass''' # NÃO HAVERIA CONFLITO COM O FRONT END
        
class BackEnd(Funcionario):
    
    def trabalhar(self):
        print('BackEnd')
    '''
    def bakcend(self):
        print('BackEnd')  NÃO HAVERA CONFLITO POR É UM MÉTODO DIFERENTE
    '''
        
    '''pass''' # NÃO HAVERIA CONFLITO COM O FRONT END
   
# MÉTODO DE RESOLUÇÃO, SERÁ EXECUTADO NA PRIMEIRA HERANÇA
class FullStack(FrontEnd, BackEnd): # Herança multipla #MRO
    
    pass
    
    '''def trabalhar(self):   # SEM CONFLITO, MÉTODO JÁ ENCONTRADO
        print('FullStack')'''
        
Jose = FrontEnd()
Marcos = BackEnd()
Carlos = FullStack()

Jose.trabalhar() #Jose.frontend()
Marcos.trabalhar() #Marcos.backend()
Carlos.trabalhar()