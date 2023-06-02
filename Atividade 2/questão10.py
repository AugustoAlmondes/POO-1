from math import sqrt


lista = []
variancia = []
soma = 0
valor = 0
for i in range(1,101):
    lista.append(i)

for i in range(100):
    soma = soma + lista[i]

media = soma/100
mediana = (lista[49]+lista[50])/2

for i in range(100):
    variancia.append((i - media)**2)

for i in variancia:
    valor = valor + i

valor = valor /100

desvio = sqrt(valor)

print("Media:",media)
print("Mediana:",mediana)
print("Desvio padrão:",desvio)
print("Variancia:",valor)
