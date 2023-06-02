from random import randint

class Pessoa:
    def __init__(self,nome,data,altura,idade):
        self._nome = nome
        self._data = data
        self._altura = altura
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def data(self):
        return self._data
    
    @property
    def altura(self):
        return self._altura

    @property
    def idade(self):
        return self._idade

    def imprimir(self):
        #print(self._nome)
        print(dic_armazenar[i].nome)
        print(dic_armazenar[i].data)
        print(dic_armazenar[i].altura)
        print(dic_armazenar[i].idade)
        
def aleatorio():
    return randint(100,1000)

dic_armazenar = {}
opcao = 5
data = []

while(opcao != 0):
    opcao = int(input("Digite a opcao: \n"
    "0 - Sair\n"
    "1 - Adicionar pessoa\n"
    "2 - Imprimir Dados da Pessoa"
    "Opcao: "))

    if opcao == 1:
        chave = aleatorio()
        nome = input("Digite o nome: ")
        dia,mes,ano = map(int, input("Digite a data de Aniversário DD MM AA: ").split())
        idade = 2022 - ano

        data.append(str(dia))
        data.append(str(mes))
        data.append(str(ano))

        for i in data:
            data2 = "/".join(data)

        altura = float(input("Digite altura: "))
        dic_armazenar[chave] = Pessoa(nome,data2,altura,idade)

    if opcao == 2:
        for i in dic_armazenar.keys():
            #dic_armazenar[i].imprimir()
            Pessoa.imprimir(i)