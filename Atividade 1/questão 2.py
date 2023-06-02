def fat (numero):
    
    if numero == 1:
        return 1
    else:
        return numero * fat(numero - 1)
        
cont = 1
fatorial = 1

numero = int(input("digite o numero: "))

while(cont <= numero):
    fatorial = cont * fatorial
   
    cont+=1
print(fatorial)
valor = fat(numero)
print(valor)




