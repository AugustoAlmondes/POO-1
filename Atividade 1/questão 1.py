figura = 0

while(figura != 4):
    print("\nfigura\n1- QUADRADO \n2- TRIANGULO\n3- CIRCULO\n4- SAIR\n")
    figura = int(input(" Digite um numero de acordo com a figura: "))
    if(figura == 1):
        lado = int(input("Digite o valor de um dos lados: ")) 
        print("Area = {}".format(lado * lado))
    if(figura == 2):
        base, altura = map(int,input("Digite a Altura e a Base: ").split())
        print("Area =  {}".format((base * altura)/2))
    if(figura == 3):
        raio = int(input("Digite o raio: "))
        print("Area = {}".format(3.14 * raio**2))