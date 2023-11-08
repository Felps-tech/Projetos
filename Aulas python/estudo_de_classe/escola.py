class Aluno:
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula
        self.notas = None
               
      
    # GETTERS
        
    # SETTERS
 
   
    @property # Enxerga o Método como um atributo - não precisa dos ()
    def get_nome(self):
        return self.__nome 
    
    
    @get_nome.setter # Defini como o setter de uma propriedade
    def set_nome(self, nome):
        self.__nome = nome
        
    @property    
    def get_idade(self):
        return self.__idade 
    
    @get_idade.setter
    def set_idade(self, idade):
        self.__idade = idade
        
    
    def get_matricula(self):
        return self.__matricula
     

aluno1 = Aluno('Felps','18',12345)
print(aluno1.get_nome)
aluno1.set_nome = 'Felipe'
print(aluno1.get_nome)

print(aluno1.get_idade)
aluno1.set_idade = 20
print(aluno1.get_idade)

print(aluno1.get_matricula())
print(aluno1.notas)


'''
class Quadrado:
    
    def __init__(self, lado):
        self.__lado = lado
        self.__area = lado * lado
        
    def retorna_area(self):
        print(self.__area)
        
quadrado = Quadrado(3)
quadrado.retorna_area()
quadrado.area = 7 # adiciona um atributo não utilizado
quadrado.retorna_area()
print(quadrado.__dict__)
quadrado._Quadrado__area = 13
quadrado.retorna_area()

# NAME MANGLING - _Classe__atributo  -  Mudar atributos privados
# '''