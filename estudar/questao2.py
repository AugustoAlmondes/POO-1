from asyncio.base_subprocess import BaseSubprocessTransport
from random import randint
class Agenda:

    def __init__(self, nome, idade,altura):
        self._nome = nome
        self._idade = idade
        self._altura = altura

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade

    @property
    def altura(self):
        return self._altura

    def remover(self,chave):
        dic_armazenar.pop(chave)

    def buscar(self):
        nome = input("Digite o nome que deseja buscar: ")
        for i in dic_armazenar.keys():
            if dic_armazenar[i]._nome == nome:
                print(dic_armazenar[i]._nome)
                print(dic_armazenar[i]._idade)
                print(dic_armazenar[i]._altura)
    
    def imprime(self):
        for i in dic_armazenar.keys():
            print(dic_armazenar[i].nome)
            print(dic_armazenar[i].idade)
            print(dic_armazenar[i].altura)

def aleatorio():
    return randint(100,1000)

def listar():
    for i in dic_armazenar.keys():
        print("Nome: ",dic_armazenar[i].nome)
        print("Chave: ", i)
    

opcao = 10
contador = 0
dic_armazenar = {}

while(opcao != 0):

    opcao = int(input("0 - sair\n1 - armazenar\n2 - remover\n3 - buscar\n4 - imprimir\n5- Listar\n:"))

    if opcao == 1:
        contador += 1
        if contador == 10:
            print("Excesso de pessoa")
        else:
            chave = aleatorio()
            nome = input("Digite o nome: ")
            idade = input("Digite o idade: ")
            altura = input("Digite o altura: ")
            print("Chave da Pessoa: ",chave)
            dic_armazenar[chave] = Agenda(nome,idade,altura)
    
    if opcao == 5:
        listar()
    
    if opcao == 2:
        listar()
        chave = int(input("Digite a chave: "))
        dic_armazenar[chave].remover(chave)
    
    if opcao == 3:
        Agenda.buscar(dic_armazenar)
        
    if opcao == 4:
        Agenda.imprime(dic_armazenar)