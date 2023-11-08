'''
Encapsulamento: Utilização de varias processos em um só
'''

class Conta:
    
    
    taxa = 0.5
    
    @classmethod 
    def retornarCodigo(cls):
        print('Codigo: 555')
        

    @staticmethod
    def retornarCodigoBanco():
        return '345'
        
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

# Encapsulamento
    def transferir(self, valor, destino):
        # self serve para referir a conta usada ao invés de colocar qualquer conta
        self.sacar(valor)  # processo 'sacar'
        destino.depositar(valor)  # processo 'depositar'