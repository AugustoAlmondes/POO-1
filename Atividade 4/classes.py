from os import system
from random import randint
from tributavel import *
from contas import *
from historico import *
from segurovida import *

Tributo.register(ContaCorrente)
Tributo.register(Seguro)

class Verifica():
    def calcular(self, x):
        if	(isinstance(x,	Tributo)):
            return x.tributo()

class Cliente:
    def __init__(self,nome, cpf, data, profissao):
        self._nome = nome
        self._cpf = cpf
        self._data = data
        self._profissao = profissao

    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def data(self):
        return self._data
    
    @property
    def profissao(self):
        return self._profissao

class Funcionario:
    def __init__(self,nome, cpf, data, salario):
        self._nome = nome
        self._cpf = cpf
        self._data = data
        self._salario = salario

    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf

    @property
    def data(self):
        return self._data
    
    @property
    def salario(self):
        return self._salario

def aleatorio():
    return randint(100,1000)

def verificar(verificar_cpf):
    for i in dic_cliente.keys():
        if i == verificar_cpf:
            return 1

def verificarContaC(verificar_cpf):
    if verificar_cpf in dic_corrente:
        return 0
    else:
        return 1

def verificarContaP(verificar_cpf):
    if verificar_cpf in dic_poupanca:
        return 0
    else:
        return 1

def verificar_seg(verificar_cpf):
    if verificar_cpf in dic_seguro:
        return 0
    else:
        return 1

def listar():
    for i in dic_cliente.keys():
        print(i)
        #dic_cliente[i].listar()

opcao = 5
dic_cliente = {}
dic_funcionario = {}
dic_conta = {}
dic_poupanca = {}
dic_corrente = {}
dic_seguro = {}
lista_tributo = []

x = 0
y = 0

while opcao != 0:
    opcao = int(input(
       "________________________"
       "\n 0 - sair"
       "\n 1 - Cadastrar Funcionario"
       "\n 2 - Cadastrar Cliente"
       "\n 3 - Criar Conta Corrente"
       "\n 4 - Criar Conta Poupanaça"
       "\n 5 - Criar Seguro de Vida"
       "\n 6 - Calcular Tributação"
       "\n 7 - Sacar"
       "\n 8 - Depositar"
       "\n 9 - Transferir"
       "\n 10 - Histórico de Conta"
       "\n 11 - Informações do Banco"
       "\n________________________"
       "\nDigite o numero da função: "))

    if opcao == 1:
        nome = input("________________________\nDigite o nome do Usuário: ")
        cpf = int(input("Digite o CPF: "))
        data = input("Digite a Data de Nascimento: ")
        salario = float(input("Digite o Salário: "))
        dic_funcionario[cpf] = Funcionario(nome,cpf,data,salario)

    elif opcao == 2:
        nome = input("________________________\nDigite o nome do Usuário: ")
        cpf = int(input("Digite o CPF: "))
        data = input("Digite a Data de Nascimento: ")
        profissao = input("Digite a Profissao do usuário: ")
        cliente = Cliente(nome, cpf, data, profissao)
        dic_cliente[cpf] = Cliente(nome, cpf, data, profissao)
        #print(dic_cliente[chave].cpf)

    elif opcao == 3:
        verificar_cpf = int(input("Digite o CPF do Clinte para criar a conta Corrente: "))
        x = verificar(verificar_cpf)
        y = verificarContaC(verificar_cpf)
        #print(y)
        if x == 1:
            print("O Cliente esta cadastrado no Sistema")
            if y == 1:
                numero = aleatorio()
                saldo = float(input('________________________\nDigite o saldo: '))
                dic_corrente[verificar_cpf] = ContaCorrente(dic_cliente[verificar_cpf], numero, saldo)
                print("Conta Criada Com Sucesso!")
                x = 0
                y = 0
            else:
                print("O Usuário ja possui uma conta Corrente")
        else:
            print("Cliente não esta Cadastrado no Sistema")
        
    elif opcao == 4:
        verificar_cpf = int(input("Digite o CPF do Clinte para criar a conta Poupança!: "))
        x = verificar(verificar_cpf)
        y = verificarContaP(verificar_cpf)
        if x == 1:
            print("O Cliente esta cadastrado no Sitema")
            if y == 1:
                numero = aleatorio()
                saldo = float(input('________________________\nDigite o saldo: '))
                dic_poupanca[verificar_cpf] = ContaPoupanca(dic_cliente[verificar_cpf], numero, saldo)
                print("Conta Poupança Criada Com Sucesso!")
                x = 0
                y = 0
            else:
                print("O Usuário ja possui uma conta Poupança")
        else:
            print("Cliente não esta Cadastrado no Sistema")

    elif opcao == 5:
        verificar_cpf = int(input("Digite o CPF do Cliente: "))
        x = verificar(verificar_cpf)
        if x == 1:
            print("________________________\nO Cliente esta cadastrado no Sitema")
            y = verificar_seg(verificar_cpf)
            if y == 0:
                print("________________________\nO Cliente ja possui seguro")
                opcao2 = int(input("Deseja Criar outro Seguro:\n"
                "1 - Sim\n"
                "2 - Não\n"
                "Opcao: "))
                if opcao2 == 1:
                    valor = float(input("________________________\nDigite o Valor da parcela: "))
                    total = float(input("Digite o Valor total do Seguro: "))
                    if valor > total:
                        print("________________________\nA Parcela não pode ser maior que o Valor Total")
                    else:
                        dic_seguro[verificar_cpf].append(Seguro(valor,total))
                        print("________________________\nSeguro Criado com Sucesso!!")
            else:
                print("________________________\nO Cliente não possui um Seguro")
                valor = float(input("________________________\nDigite o Valor da parcela: "))
                total = float(input("Digite o Valor total do Seguro: "))
                if valor > total:
                        print("________________________\nA Parcela não pode ser maior que o Valor Total")
                else:
                    lista =[Seguro(valor,total)]
                    dic_seguro[verificar_cpf] = lista
                    print("________________________\nSeguro Criado com Sucesso!!")

    elif opcao == 6:
        tributo = 0.0
        verifica = Verifica()

        for x in dic_seguro.values():
            for z in x:
                tributo += verifica.calcular(z)
        
        for y in dic_corrente.values():
            tributo += verifica.calcular(y)
        lista_tributo.append(tributo)

        for i in range(len(lista_tributo)):
            print(i+1," ",lista_tributo[i])
            
    elif opcao == 7:
        verificar_cpf = int(input("Digite o CPF do Usuário: "))
        x = verificar(verificar_cpf)
        if x == 1:
            print("________________________\nO Cliente esta cadastrado no Sitema")
            opcao3 = int(input("Escolha qual conta irá realizar a ação:\n"
            "1 - Poupança\n"
            "2 - Corrente\n"
            "3 - Sair\n"
            "Opcao: "))
            if opcao3 == 1:
                y = verificarContaP(verificar_cpf)
                if y == 0:
                    print("________________________\nUsuário possui uma conta Poupuança")
                    saque = float(input("Digite o valor do saque: "))
                    if saque < dic_poupanca[verificar_cpf]._saldo:
                        dic_poupanca[verificar_cpf].sacar(saque)
                    else:
                        print("________________________\nSaldo insuficiente")
                else:
                    print("________________________\nUsuário não possui conta Poupança")
            elif opcao3 == 2:
                y = verificarContaC(verificar_cpf)
                if y == 0:
                    print("________________________\nUsuário possui uma conta Corrente")
                    saque = float(input("Digite o valor do saque: "))
                    if saque < dic_corrente[verificar_cpf]._saldo:
                        dic_corrente[verificar_cpf].sacar(saque)
                    else:
                        print("________________________\nSaldo insuficiente")
                else:
                    print("________________________\nUsuário não possui conta Corrente")
            elif opcao3 == 3:
                pass
        else:
            print("________________________\nO Cliente não está cadastrado")
    
    elif opcao == 8:
            verificar_cpf = int(input("Digite o CPF do Usuário: "))
            x = verificar(verificar_cpf)
            if x == 1:
                print("________________________\nO Cliente esta cadastrado no Sitema")
                opcao3 = int(input("Escolha qual conta irá realizar a ação:\n"
                "1 - Poupança\n"
                "2 - Corrente\n"
                "3 - Sair\n"
                "Opcao: "))
                if opcao3 == 1:
                    y = verificarContaP(verificar_cpf)
                    if y == 0:
                        print("________________________\nUsuário possui uma conta Poupuança")
                        deposito = float(input("Digite o valor do deposito: "))
                        dic_poupanca[verificar_cpf].depositar(deposito)
                        print("deposito realizado com Sucesso")
                    else:
                        print("________________________\nUsuário não possui conta Poupança")
                elif opcao3 == 2:
                    y = verificarContaC(verificar_cpf)
                    if y == 0:
                        print("________________________\nUsuário possui uma conta Corrente")
                        deposito = float(input("Digite o valor do deposito: "))
                        dic_corrente[verificar_cpf].depositar(deposito)
                        print("deposito realizado com Sucesso")
                    else:
                        print("________________________\nUsuário não possui conta Poupança")
                elif opcao3 == 3:
                    pass

    elif opcao == 9:
        conta1 = int(input("________________________\nDigite o CPF do Usuário que fará a transferencia: "))
        x = verificar(conta1)
        if x == 1:
            print("________________________\nUsuário está registrado")
            opcao4 = int(input("Escolha qual conta irá realizar a ação:\n"
            "1 - Poupança\n"
            "2 - Corrente\n"
            "3 - Sair\n"
            "Opcao: "))
            if opcao4 == 1:
                y = verificarContaP(conta1)
                if y == 0:
                    print("________________________\nUsuário possui conta Poupança!")
                    
                    valor1 = float(input("________________________\nDigite o valor da transferencia: "))

                    if valor1 < dic_poupanca[conta1]._saldo:
                        conta2 = int(input("________________________\nDigite o CPF do usuário a receber: "))
                        w = verificar(conta2)
                        if w == 1:
                            print("________________________\nUsuário está registrado")
                            opcao5 = int(input("________________________\nEscolha qual conta irá realizar a ação:\n"
                            "1 - Poupança!\n"
                            "2 - Corrente\n"
                            "3 - Sair\n"
                            "Opcao: "))
                            if opcao5 == 1:
                                y = verificarContaP(conta2)
                                if y == 0:
                                        print("________________________\nUsuário possui conta Poupança!")
                                        dic_poupanca[conta2]._saldo = dic_poupanca[conta2]._saldo + valor1
                                        dic_poupanca[conta1]._saldo = dic_poupanca[conta1]._saldo - valor1
                                        dic_poupanca[conta2]._historico.add_transacao('| Transferencia |')
                                        dic_poupanca[conta1]._historico.add_transacao('| Transferencia |')                  
                                        print("________________________\nTransferencia Realizada com Sucesso")
                                else:
                                    print("________________________\nNão possui conta Poupança!")  

                            if opcao5 == 2:
                                y = verificarContaC(conta2)
                                if y == 0:
                                        print("________________________\nUsuário possui conta Corrente")                                        
                                        dic_corrente[conta2]._saldo = dic_corrente[conta2]._saldo + valor1
                                        dic_poupanca[conta1]._saldo = dic_poupanca[conta1]._saldo - valor1
                                        dic_corrente[conta2]._historico.add_transacao('| Transferencia |')
                                        dic_poupanca[conta1]._historico.add_transacao('| Transferencia |')
                                        print("________________________\nTransferencia Realizada com Sucesso")
                                else:
                                    print("________________________\nNão possui conta Corrente")   
                    else:
                        print("________________________\nvalor insuficiente")
                else:
                    print("Usuário não possui uma conta Poupança!")

            elif opcao4 == 2:
                y = verificarContaC(conta1)
                if y == 0:
                    print("________________________\nUsuário possui conta Corrente")
                    valor1 = float(input("________________________\nDigite o valor da transferencia: "))
                    if valor1 < dic_corrente[conta1]._saldo:
                        conta2 = int(input("________________________\nDigite o CPF do usuário a receber: "))
                        w = verificar(conta2)
                        if w == 1:
                            print("________________________\nUsuário está registrado")
                            opcao6 = int(input("________________________\nEscolha qual conta irá realizar a ação:\n"
                            "1 - Poupança!\n"
                            "2 - Corrente\n"
                            "3 - Sair\n"
                            "Opcao: "))
                            if opcao6 == 1:
                                y = verificarContaP(conta2)
                                if y == 0:
                                        print("________________________\nUsuário possui conta Poupança!")
                                        dic_poupanca[conta2]._saldo = dic_poupanca[conta2]._saldo + valor1
                                        dic_corrente[conta1]._saldo = dic_corrente[conta1]._saldo - valor1
                                        dic_poupanca[conta2]._historico.add_transacao('| Transferencia |')
                                        dic_corrente[conta1]._historico.add_transacao('| Transferencia |')
                                        print("________________________\nTransferencia Realizada com Sucesso")
                                else:
                                    print("________________________\nNão possui conta Poupança!")  

                            if opcao6 == 2:
                                y = verificarContaC(conta2)
                                if y == 0:
                                        print("________________________\nUsuário possui conta Corrente")                            
                                        dic_corrente[conta2]._saldo = dic_corrente[conta2]._saldo + valor1
                                        dic_corrente[conta1]._saldo = dic_corrente[conta1]._saldo - valor1
                                        dic_corrente[conta2]._historico.add_transacao('| Transferencia |')
                                        dic_corrente[conta1]._historico.add_transacao('| Transferencia |')
                                        print("________________________\nTransferencia Realizada com Sucesso")
                                else:
                                    print("________________________\nNão possui conta Corrente")   
                    else:
                        print("________________________\nvalor insuficiente")
                else:
                    print("Usuário não possui uma conta Corrente")
            elif opcao6 == 3:
                pass
        else:
            print("print(________________________\nusuário não registrado")
    
    elif opcao == 10:
        opcao7 = int(input("Escolha a Opção:\n"
        "1 - Conta Corrente\n"
        "2 - Conta Poupança\n"
        "Opção: "))

        if opcao7 == 1:
            verificiar_cpf = int(input("Digite o CPF do usuário: "))
            x = verificarContaC(verificar_cpf)
            if x == 0:
                dic_corrente[verificar_cpf].historico.imprime_transacoes()
            else:
                print("Usuário não possui conta Corrente")
        if opcao7 == 2:
            verificiar_cpf = int(input("Digite o CPF do usuário: "))
            x = verificarContaP(verificar_cpf)
            if x == 0:
                dic_poupanca[verificar_cpf].historico.imprime_transacoes()
            else:
                print("Usuário não possui conta Poupança")

    elif opcao == 11:
        quantidade = 0
        opcao6 = int(input("Escolha a Opção:\n"
        "1 - Total de Conta\n"
        "2 - Clientes Cadastrados\n"
        "3 - Contas e Seguros de Vida\n"
        "Opção: "))

        if opcao6 == 1:
            contaP = len(dic_poupanca)
            print("________________")
            print("|Poupanças: ",contaP,"|")
            contaC = len(dic_corrente)
            print("|Correntes: ",contaC,"|")
            totalC = contaP + contaC
            print("________________________\nTotal de contas: ",totalC)

        elif opcao6 == 2:
            print("________________________\n Clientes Registrados\n________________________")
            for i in dic_cliente.keys():
                print(dic_cliente[i]._nome)
            print("________________________")

        elif opcao6 == 3:
            print("________________________\n Clientes Registrados\n________________________")
            for i in dic_cliente.keys():
                print(dic_cliente[i]._nome)
                if i in dic_seguro:
                    print("Quantidade de Seguros: ",len(dic_seguro[i]))
                if i in dic_corrente:
                    quantidade += 1
                if i in dic_poupanca:
                    quantidade += 1
                print("Quantidade de Contas: ",quantidade)
                quantidade = 0
                print("________________________")
            print("________________________")