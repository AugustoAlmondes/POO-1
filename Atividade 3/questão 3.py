class Elevador:
    def __init__(self,totalandares, capacidade):
        self._andaratual = 0
        self._totalandares = totalandares
        self._capacidade = capacidade
        self._pessoaspre = 0

    @property
    def andaratual(self):
        return self._andaratual
    
    @andaratual.setter
    def andaratual(self, andaratual):
        self._andaratual = andaratual

    @property
    def totalandares(self):
        return self._totalandares
    
    @property
    def capacidade(self):
        return self._capacidade
    
    @property
    def pessoaspre(self):
        return self._pessoaspre
    
    @pessoaspre.setter
    def pessoaspre(self, pessoaspre):
        self._pessoaspre = pessoaspre
    
    def adicionarpessoa(self, pessoas):
        #print(self.pessoaspre,"Pessoas presentes")
        if capacidade >= (self._pessoaspre + pessoas):
            self.pessoaspre += pessoas
            print("________________________\n")
            print(self.pessoaspre,"Pessoas presentes")
        else:
            print("________________________\n")
            print("Elevador cheio")

    def removerpessoas(self,pessoas):
        if self.pessoaspre < pessoas:
            print("________________________\n")
            print("Pessoas inexistentes")
        else:
            self.pessoaspre -= pessoas
            print("________________________\n")
            print(self.pessoaspre,"Pessoas presentes")

    def subirandar(self,andar):
        if andar > self.totalandares:
            print("________________________\n")
            print("Andar inexistente")
        else:
            self.andaratual = andar
            print("________________________\n")
            print("Andar atual: ",self.andaratual)

    def descerandar(self, andar):
        if (self.andaratual - andar) < 0:
            print("________________________\n")
            print("Andar inexistente")
        else:
            self.andaratual = andar
            print("________________________\n")
            print("Andar atual: ",self.andaratual)

opcao = 0

while opcao != 6:
    print("________________________\n"
    "1 - Quantidade Pessoas\Andares\n"
    "2 - Quantas Pessoas Entraram\n"
    "3 - Quantas Pessoas Sairam\n"
    "4 - Subir Para Andar\n"
    "5 - Descer Para Andar\n"
    "6 - Sair\n")
    opcao = int(input("opcao: "))

    if opcao == 1:
        print("________________________\n")
        capacidade = int(input("Capacidade: "))
        print("________________________\n")
        andares = int(input("Andares: "))
        elevador = Elevador(andares, capacidade)

    elif opcao == 2:
        print("________________________\n")
        pessoas = int(input("Quantas pessoas: "))
        elevador.adicionarpessoa(pessoas)

    elif opcao == 3:
        print("________________________\n")
        pessoas = int(input("Quantas pessoas sairam: "))
        elevador.removerpessoas(pessoas)
    
    elif opcao == 4:
        print("________________________\n")
        andar = int(input("Escolha um andar: "))
        elevador.subirandar(andar)    
    
    elif opcao == 5:
        print("________________________\n")
        andar = int(input("Escolha um andar: "))
        elevador.descerandar(andar)
