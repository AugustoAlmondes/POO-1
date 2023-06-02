import random

def gerar():
    x = random.randint(0,100)
    return x

def tentativas(x):
    for i in range(10):
        valor = int(input("Digite um numero: "))
        print("Tentativa {}".format(i+1))
        if valor == x:
            print("Parabéns, você acertou!!")
            break

opcao = 2

while(opcao != 0):
    x = gerar()
   #print (x)
    tentativas(x)
    opcao = int(input("Digite\n1 - Reiniciar\n0 - Sair\nOpcao: "))



        
