'''
Visibilidade - Modificador de Acesso

Privada (private) - restritiva -> Define que os atributos e métodos só podem ser manipulados dentro da classe. impede o interpretador
Protegida (protected) - intermediária -> Define que os atributos e métodos só podem ser manipulados dentro da classe 
e nas classes que herdam da classe onde foram definidos. 
Pública (public) - menos restritiva -> Defnne que os atributos e métodos são acessiveis em qualquer lugar.

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

    def depositar(outro, valor):
        outro.__saldo += valor
        outro.transacao(outro.__saldo)


    def sacar(self, valor):
        self.__saldo -= valor
        self.transacao(self.__saldo)

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
