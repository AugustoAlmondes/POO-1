decimal = int(input("Digite um numero: "))
binario = 0
contador = 0
aux = 0
string2 = ' '

while(decimal != 0):
    string = decimal%2
    string = str(string)
    string2 = string + string2
    decimal = decimal//2
print(string2)