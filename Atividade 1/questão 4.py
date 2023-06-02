def primo(numero):
    contador = 0
    for i in range(2,numero):
        if(numero % i == 0):
            contador += 1
    if contador == 0:
        print("E primo")
    else:
        print("Nao e primo")

numero = int(input("Digite um numero: "))
primo(numero)

contador = 0

num1, num2 = map(int,input("Digite dois numero: ").split())
contador2 = 0;
for i in range(num1, num2+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 
        contador += 1
if contador == 0:
    print("Não existe nenhum número primo dentro desse intervalo")

       

