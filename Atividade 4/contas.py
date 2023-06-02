import abc
from historico import *
class Conta(abc.ABC):

    def __init__(self,cliente, numero, saldo):
        self._cliente = cliente
        self._numero = numero
        self._saldo = saldo
        self._historico = Historico()

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def historico(self):
        return self._historico
        
    @historico.setter
    def historico(self):
        self._historico = Historico  
    
    def sacar(self, valor):
        self._saldo -= valor
        print('Saque realizado com sucesso')
        print('Saldo da conta: ',self._saldo)
        self._historico.add_transacao('| Saque         |')

    def depositar(self, valor):
        self._saldo += valor
        print('Valor depositado com sucesso')
        print('Valor atual: ', self._saldo)
        self._historico.add_transacao('| Depositado    |')

class ContaPoupanca(Conta):
    
    def __init__(self, cliente, numero, saldo):
        super().__init__( cliente, numero, saldo)

class ContaCorrente(Conta):
    
    def __init__(self, cliente, numero, saldo):
        super().__init__( cliente, numero, saldo)
    
    def tributo(self):
        return self._saldo * 0.01