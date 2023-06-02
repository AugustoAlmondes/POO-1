from random import randint

def aleatorio():
    return randint(100,1000)

class Agenda:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def listar_usu(self):
        print("Nome: ", self.nome)
        print("Altura: ", self.altura)
        print("Idade: ", self.idade)

    def remover(self):
        nomeremover = input("Digite a pessoa que deseja remover: ")
        for i in dicionario.keys():
            if dicionario[i].nome == nomeremover:
                print("________________________")
                print("Usuário deletado")
                return i

    def imprimirAgenda(self):
        for i in dicionario.keys():
            print()
            dicionario[i].listar_usu()

    def imprimirPessoa(self):
        nomebusca = input("Digite o nome da pessoa: ")
        for i in dicionario.keys():
            if nomebusca == dicionario[i].nome:
                print("________________________")
                dicionario[i].listar_usu()
                
opcao = 0
dicionario = {}
contador = 0

while opcao != 5:
    print("________________________\n"
    "1 - Armazenar Pessoa\n"
    "2 - Remover Pessoa\n"
    "3 - Buscar Pessoa\n"
    "4 - Imprimir Agenda\n"
    "5 - Sair")
    opcao = int(input("Digite a opcao: "))

    if opcao == 1:
        if contador < 10:
            contador += 1
            print("________________________")
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            altura = input("Digite a altura: ")
            #agenda = Agenda(nome, idade, altura)
            chave = aleatorio()
            dicionario[chave] = Agenda(nome, idade, altura)
            print("________________________")
            print(contador,"Pessoas Armazenadas")
        else:
            print("________________________")
            print("Máximo de pessoas armazenadas")

    if opcao == 2:
        numero = Agenda.remover(dicionario)
        dicionario.pop(numero)
        contador -= 1

    if opcao == 3:
        Agenda.imprimirPessoa(dicionario)
    
    if opcao == 4:
        Agenda.imprimirAgenda(dicionario)