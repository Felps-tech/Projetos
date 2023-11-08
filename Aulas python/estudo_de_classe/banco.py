'''
Visibilidade - Modificador de Acesso

Privada (private) - restritiva -> Define que os atributos e métodos só podem ser manipulados dentro da classe. impede o interpretador
Protegida (protected) - intermediária -> Define que os atributos e métodos só podem ser manipulados dentro da classe 
e nas classes que herdam da classe onde foram definidos. 
Pública (public) - menos restritiva -> Defnne que os atributos e métodos são acessiveis em qualquer lugar.

'''

class Conta:  # pertence a propria classe - self
    
    # Atributo de Classe
    taxa = 0.5
    
    # Método de Classe
    # DECORADOR
    @classmethod  #   class
    def retornarCodigo(cls):
        print('Codigo: 555')
        
    # Método Estático
    @staticmethod
    def retornarCodigoBanco():
        return '345'
        
    # Atributos de Instâncias
    def __init__(self, numero, titular, saldo=2000):
        #  atributos   variaveis
        self._numero = numero # Visibilidade Protegida (protected) '_'
        self.titular = titular # Visibilidade Pública (public) ''
        self.__saldo = saldo # Visibilidade Privada (private) '__'
        self.__historico = [saldo]
    
    def saldo(self):
        print(f'Saldo Atual: R${self.__saldo}')
        
        
    def transacao(self, saldo):
        self.__historico.append(saldo)
        
        
    def extrato(self):
        print('-----Extrato----')
        print(f'Conta: {self.titular}')
        for saldo in self.__historico:
            print(f'Saldo: R${saldo}')

#       parametro 'self'
    def depositar(outro, valor):
        #'self' nomeado como 'outro'
        outro.__saldo += valor
        outro.transacao(outro.__saldo)


    def sacar(self, valor):
        self.__saldo -= valor
        self.transacao(self.__saldo)

# Encapsulamento
    def transferir(self, valor, destino):
        # self serve para referir a conta usada ao invés de colocar qualquer conta
        self.sacar(valor)
        destino.depositar(valor)


conta1 = Conta(123, 'Felps')  
conta2 = Conta(456, 'Cauã', 5000)  

conta1.transferir(300, conta2)
conta1.saldo()
conta2.saldo()
conta1.extrato()

# Instâncias da Classe Conta
'''
conta1 = Conta(123, 'Felps')  
conta2 = Conta(456, 'Cauã', 5000)  

print(f'Títular: {conta1.titular} - Saldo: R${conta1.__saldo}')
print(f'Títular: {conta2.titular} - Saldo: R${conta2.__saldo}')
        
print(conta1.__dict__)
print(conta2.__dict__)

conta2.extrato()
'''
'''# Atributo dinâmico -> Criado em tempo de execução
conta1.signo = 'Touro' # adiciona atributo

print(conta1.__dict__)
print(conta2.__dict__)

del conta1.signo # deleta atributos

print(conta2.__dict__)

# Método da classe
Conta.retornarCodigo() # Convenção
conta1.retornarCodigo()

# Método Estático
print(Conta.retornarCodigoBanco()) # Convenção
print(conta2.retornarCodigoBanco())
'''