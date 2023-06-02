from random import randint
import datetime
import abc

class Conta(abc.ABC):

    def __init__(self, titular, numero, saldo = 0):
        self._numero = numero
        self._saldo = saldo
        self._titular = titular
        self._historico = Historico()

    @abc.abstractmethod
    def	atualiza():
        pass

        @property
        def titular_nome(self):
            return self._titular.nome

        @property
        def titular_sobrenome(self):
            return self._titular.sobrenome

        @property
        def numero(self):
            return self._numero

        @property
        def titular_cpf(self):
            return self._titular.cpf

        @property
        def saldo(self):
            return self._saldo
   
        @property
        def historico(self):
            return self._historico

        @saldo.setter
        def saldo(self, saldo):
            self._saldo = saldo

        @historico.setter
        def historico(self):
            self._historico = Historico

    def transferir(self,conta2, valor):
        self._saldo -= valor
        conta2._saldo += valor

    '''def listar(self):
        print(self.titular_nome)
        print(self.titular_cpf)
        print(self.numero)
        print("{:.2f}".format(self.saldo))'''

    def listar(self):
        print(self._titular.nome, self._titular.sobrenome)
        print(f'CPF: ',self._titular.cpf)
        print(f'Número da conta: ',self._numero)
        print(f'Saldo da conta R$: ', self._saldo)

    def sacar(self, valor):
        self._saldo -= valor
        print('Saque realizado com sucesso')
        print('Saldo da conta: ',self._saldo)

    def depositar(self, valor):
        self._saldo += valor
        print('Valor depositado com sucesso')
        print('Valor atual: ', self._saldo)

    def extrato(self):
        print('Numero da conta: ', self._numero)
        print('Saldo da conta: ', self._saldo)

class ContaInvestimento(Conta):
    
    def __init__(slef, titular, numero, saldo):
        super().__init__(titular, numero, saldo)
    
    def	atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

class ContaCorrente(Conta):

    def __init__(slef, titular, numero, saldo):
        super().__init__(titular, numero, saldo)
    
    def	atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

class ContaPolpanca(Conta):
    
    def __init__(slef, titular, numero, saldo):
        super().__init__(titular, numero, saldo)
    
    def	atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3

class Historico():
    def __init__(self):
        self._data_criacao = datetime.datetime.now()
        self._transacoes = []
        
    @property
    def data_criacao(self):
        return self._data_criacao
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def add_transacao(self, t):
        self._transacoes.append(t)

    def imprime_transacoes(self):
        print(f'Data de abertura: {self._data_criacao}')
        for t in self._transacoes:
            print(t)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def cpf(self):
        return self._cpf


def aleatorio():
    return randint(100,1000)

dicionario = {}

def listar():
    for i in dicionario.keys():
        print()
        dicionario[i].listar()

if __name__ == "__main__":
    cc = ContaCorrente('Augusto', 17, 1000)
    print(cc._titular)

while True:

    opcao = int(input(
       "________________________"
       "\n 1 - criar"
       "\n 2 - listar"
       "\n 3 - sacar"
       "\n 4 - depositar"
       "\n 5 - excluir"
       "\n 6 - transferencia"
       "\n 7 - Extrato"
       "\n 8 - sair"
       "\n________________________"
       "\nDigite o numero da função: "))

    if opcao == 1:

        nome = str(input('________________________\nDigite o nome: '))
        sobrenome = str(input("Digite o Sobrenome: "))
        cpf = int(input("Digite o CPF: "))
        saldo = float(input('Digite o saldo: '))
        chave = aleatorio()
        cliente = Cliente(nome, sobrenome, cpf)
        dicionario[chave] = Conta(cliente, chave, saldo)

    elif opcao == 2:
        listar()

    elif opcao == 3:
        listar()
        opcao2 = int(input("________________________\nDigite o numero da conta: "))
        valor2 = int(input("Digite o valor que deseja sacar: "))
        if valor2 < dicionario[opcao2]._saldo:
            dicionario[opcao2].sacar(valor2)
        else:
            print("________________________\nSaldo insuficiente")

    elif opcao == 4:
        listar()
        opcao2 = int(input("________________________\nDigite o numero da conta: "))
        valor2 = int(input("Digite o valor que deseja depositar: "))
        dicionario[opcao2].depositar(valor2)

    elif opcao == 5:
        listar()
        opcao2 = int(input("________________________\nDigite o numero da conta: "))
        dicionario.pop(opcao2)

    elif opcao == 6:
        listar()
        conta1 = int(input("________________________\nDigite a conta que sera tranferida: "))
        conta2 = int(input("Digite a conta que receberá: "))
        valor2 = float(input("digite o valor a ser transferido: "))
        if valor2 < dicionario[conta1]._saldo:
            dicionario[conta1].transferir(dicionario[conta2],valor2)
        else:
            print("________________________\nSaldo insuficiente")

    elif opcao == 7:
        listar()
        conta1 = int(input("________________________\nDigite a conta para ver extrato: "))
        dicionario[conta1]._historico.imprime_transacoes()

    elif opcao == 8:
        break
