from math import sqrt

class Armazenar:
    def __init__(self):
        self.lista1 = []
        self.lista2 = []

    def adicionar(self,x, y):
        self.lista1.append(x)
        self.lista2.append(y)

class Calcular:
    def __init__(self):
        self.menor = 0
        self.pontos = ' '
        self.pontosF = ' '
        self.resultado = []
    
    def distancia(self,lista1,lista2):
        num = 1
        aux = 0
        for i in range(9):
            if i != 10:
                num = 1

            distancia = ((lista1[0]-lista1[i+num])**2) + ((lista2[0]-lista2[i+num])**2)
            distancia = sqrt(distancia)

            if aux != 1:
                self.menor = distancia
                aux += 1
            
            if distancia < self.menor:
                self.menor = distancia
                self.pontosF = f'x:{lista1[0]} y:{lista2[0]}' 
                self.pontos = f'x:{lista1[i+num]} y:{lista2[i+num]}'

            self.resultado.append(distancia)
            

    def printar(self):
        #print(self.resultado)
        print("__________________")
        print("Pontos fixos: {}".format(self.pontosF))
        print("Menor Distancia: {}".format(self.menor))
        print("Coordenadas: {}".format(self.pontos))
        print("__________________")
        
def main():
    calcular = Calcular()
    armazenar = Armazenar()
    for i in range(10):
        x = float(input("Digite a coordenada x{}: ".format(i)))
        y = float(input("Digite a coordenada y{}: ".format(i)))
        armazenar.adicionar(x,y)

    calcular.distancia(armazenar.lista1,armazenar.lista2)
    calcular.printar()


main()