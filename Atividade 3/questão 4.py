class Televisao:
    def __init__(self):
        self.volumeatual = 0
        self.canalatual = 0

    def aumentarcanal(self):
        if self.canalatual == 100:
            print("________________________\n")
            print("Canal Maximo")
        else:
            self.canalatual+=1
            print("________________________\n")
            print("Canal Atual: ",self.canalatual)
    
    def diminuircanal(self):
        if self.canalatual == 0:
            print("________________________\n")
            print("Canal Minimo")
        else:
            self.canalatual -= 1
            print("________________________\n")
            print("Canal Atual: ",self.canalatual)

    def diminuirvolume(self):
        if self.volumeatual == 0:
            print("________________________\n")
            print("Volume Minimo")
        else:
            self.volumeatual -= 1
            print("________________________\n")
            print("Volume Atual: ",self.volumeatual)
    
    def aumentarvolume(self):
        if self.volumeatual == 100:
            print("________________________\n")
            print("Volume Maximo")
        else:
            self.volumeatual += 1
            print("________________________\n")
            print("Volume Atual: ",self.volumeatual)

    def mudarcanal(self):
        print("________________________\n")
        canal = int(input("Digite o canal que deseja mudar: "))
        if canal > 100 or canal < 0:
            print("________________________\n")
            print("Canal inexistente")
        else:
            self.canalatual = canal
            print("________________________\n")
            print("Canal Atual: ",self.canalatual)
        
    def mostrarvalor(self):
        print("________________________\n")
        print("Volume: ",self.volumeatual)
        print("Canal: ",self.canalatual)

class Controle:
    def __init__(self,televisao):
        self.televisao = televisao

    def aumentar(self):
        self.televisao.aumentarvolume()

    def diminuir(self):
        self.televisao.diminuirvolume()

    def aumentarcanal(self):
        self.televisao.aumentarcanal()
    
    def diminuircanal(self):
        self.televisao.diminuircanal()
    
    def mudarcanal(self):
        self.televisao.mudarcanal()

    def mostrarvalor(self):
        self.televisao.mostrarvalor()
        
opcao = 0

tel = Televisao()
controle = Controle(tel)

while opcao != 7:
    print("________________________\n"
    "1 - Aumentar Volume\n"
    "2 - Diminuir Volume\n"
    "3 - Aumentar Canal\n"
    "4 - Dimninuir Canal\n"
    "5 - Mudar canal\n"
    "6 - Mostrar Valores\n"
    "7 - Desligar\n")
    opcao = int(input("Digite a opcao: "))

    if opcao == 1:
        controle.aumentar()
    
    elif opcao == 2:
        controle.diminuir()
    
    elif opcao == 3:
        controle.aumentarcanal()
    
    elif opcao == 4:
        controle.diminuircanal()

    elif opcao == 5:
        controle.mudarcanal()
    
    elif opcao == 6:
        controle.mostrarvalor()