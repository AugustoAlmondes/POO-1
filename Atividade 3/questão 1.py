from random import randint

class Pessoa:
    def __init__(self,nome, data, altura, idade):
        self._nome = nome
        self._data = data
        self._altura = altura
        self._idade = idade

    def listar_usu(self):
        print("Nome: ", self._nome)
        print("Data de Nascimento: ", self._data)
        print("Altura: ", self._altura)
        print("Idade: ", self._idade)

        @property
        def nome(self):
            return self._nome
        
        @property
        def data(self):
            return self._data

        @property
        def altura(self):
            return self._altura

        @nome.setter
        def nome(self, nome):
            self._nome = nome
        
        @altura.setter
        def altura(self, altura):
            self._altura = altura
        
        @data.setter
        def data(self, data):
            self._data = data

def imprimir():
    for i in dicionario.keys():
        print()
        dicionario[i].listar_usu()

def aleatorio():
    return randint(100,1000)

opcao = 3
data = []
dicionario = {}
while opcao != 0:
    opcao = int(input("\n0 - Sair\n"
    "1 - adicionar dados de uma pessoa\n"
    "2 - Imprimir dados de uma pessoa\n"
    "Digite  opcao: "))

    if opcao == 1:
        data = []
        nome = input("Digite o nome: ")
        dia, mes, ano = map(int, input("Digite o Dia, Mes, Ano (DD MM AAAA): ").split())
        idade = 2022 - ano
        chave = aleatorio()
        data.append(str(dia))
        data.append(str(mes))
        data.append(str(ano))

        for i in data:
            data2 = "/".join(data)

        data2 = str(data2)
        altura = input("Digite a altura: ")
        #pessoa = Pessoa(nome, data2, altura)
        dicionario[chave] = Pessoa(nome, data2, altura, idade)
    
    if opcao == 2:
        imprimir()