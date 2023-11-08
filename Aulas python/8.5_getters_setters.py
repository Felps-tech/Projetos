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
         
    
    def get_idade(self):
        return self.__idade 
    
    
    def set_idade(self, idade):
        self.__idade = idade
        
    
    def get_matricula(self):
        return self.__matricula
     

aluno1 = Aluno('Felps','18',12345)
print(aluno1.get_nome)  # GETTER
aluno1.set_nome = 'Felipe'  # SETTER
print(aluno1.get_nome)  # GETTER

print(aluno1.get_idade()) # GETTER NÃO SIMPLIFICADO
aluno1.set_idade(20) # SETTER NÃO SIMPLIFICADO
print(aluno1.get_idade()) # GETTER NÃO SIMPLIFICADO

print(aluno1.get_matricula())
print(aluno1.notas)
