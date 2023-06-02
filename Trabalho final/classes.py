from abc import ABC,abstractmethod
from imposto import *

class Armazena:
    def __init__(self):

        self._lista_imposto = []
        self._dic_cliente = {}
        self._dic_funcionario = {}
        self._dic_produto = {}

        @property
        def lista_imposto(self):
            return self._lista_imposto

        @lista_imposto.setter
        def lista_imposto(self, lista_imposto):
            self._lista_imposto = lista_imposto

        @property
        def dic_cliente(self):
            return self._dic_cliente

        @dic_cliente.setter
        def dic_cliente(self, dic_cliente):
            self._dic_cliente = dic_cliente

        @property
        def dic_funcionario(self):
            return self._dic_funcionario
        
        @dic_funcionario.setter
        def dic_funcionario(self, dic_funcionario):
            self._dic_funcionario = dic_funcionario

        @property
        def dic_produto(self):
            return self._dic_produto

        @dic_produto.setter
        def dic_produto(self, dic_produto):
            self._dic_produto = dic_produto
            
class Produto:
    def __init__(self,codigo, marca, valor, quantidade):
        self._codigo = codigo
        self._marca = marca
        self._valor = valor
        self._quantidade = quantidade

    @property
    def codigo(self):
        return self._codigo

    @property
    def marca(self):
        return self._marca

    @property
    def valor(self):
        return self._valor

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade += quantidade

    def imposto(self):
        return self.quantidade * 0.08
        
    
    def realizarCompra(self,marca, quantidade,desconto):
        if quantidade <= self.quantidade:
            valortotal = (quantidade * self._valor)
            valordesconto = valortotal * desconto
            valortotal = valortotal - valordesconto
            print("Produto: {}".format(marca))
            print("Desconto de R${:.2f}".format(valordesconto))
            print("Valor total: R${:.2f}".format(valortotal))
            
            if desconto == 0.2:
                opcao = int(input("Efetuar Compra?\n"
                "1 - Sim\n"
                "2 - Não\n"
                "Opcao: "))

                if opcao == 1:
                    self.quantidade = -quantidade
                    print("________________________")
                    print("Compra Realizada com Sucesso")
                else: 
                    print("________________________")
                    print("Compra Cancelada")
            elif desconto == 0.0:
                opcao = int(input("Efetuar Compra?\n"
                "1 - Sim\n"
                "2 - Não\n"
                "Opcao: "))
                if opcao == 1:
                    self.quantidade = -quantidade
                    print("________________________")
                    print("Compra Realizada com Sucesso")
                else: 
                    print("________________________")
                    print("Compra Cancelada")

        else:
            print("Insficiencia no Estoque")

    def reporEstoque(self,quantidade):
        self.quantidade = quantidade

    def verificaEstoque(self):
        print("________________________")
        print("Marca: {}".format(self.marca))
        print("Quantidade em Estoque: {}".format(self.quantidade))

    def prateleira(self):
        print("________________________")
        print("Marca: {}".format(self.marca))
        print("Preço p/ unidade: R$ {:.2f}".format(self.valor))

    @staticmethod
    def embalar():
        print("Produto Embalado")
        print("Obrigado pela compra, volte sempre!! S2 ")

class Verifica():
    def calcular(self, x):
        if	(isinstance(x,	Imposto)):
            return x.imposto()

class Pessoa(ABC):
    def __init__(self,nome, cpf, data):
        self._nome = nome
        self._cpf = cpf
        self._data = data

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
    

class Cliente(Pessoa):
    def __init__(self,nome, cpf, data, profissao):
        super().__init__(nome, cpf, data)
        self._profissao = profissao

    @property
    def profissao(self):
        return self._profissao

class Funcionario(Pessoa):
    def __init__(self,nome, cpf, data, salario):
        super().__init__(nome, cpf, data)
        self._salario = salario

    @property
    def salario(self):
        return self._salario
