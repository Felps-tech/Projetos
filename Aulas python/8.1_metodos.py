class Conta:  # pertence a propria classe - self
    
    # Atributo de Classe
    taxa = 0.5
    
    # Método de Classe - funciona com a classe recebe parâmetro que faz referencia a própria classe
    # DECORADOR
    @classmethod  #   class
    def retornarCodigo(cls):
        print('Codigo: 555')
        
    # Método Estático - não vai saber nada sobre a classe vai apenas lidar com os parâmetros de receber
    @staticmethod  #  não necessita de parâmetro
    def retornarCodigoBanco():
        return '345'
        
    # Atributos de Instâncias
    def __init__(self, numero, titular, saldo=2000):
        self._numero = numero 
        self.titular = titular 
        self.__saldo = saldo 
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

    def depositar(outro, valor):
        outro.__saldo += valor
        outro.transacao(outro.__saldo)


    def sacar(self, valor):
        self.__saldo -= valor
        self.transacao(self.__saldo)

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)


conta1 = Conta(123, 'Felps')  
conta2 = Conta(456, 'Cauã', 5000)  

# Método de Classe   #   Não é necessario a chamada das instâncias
Conta.retornarCodigo() # Convenção
print(conta2.retornarCodigo())

# Método Estático
Conta.retornarCodigoBanco() # Convenção
print(conta1.retornarCodigoBanco())