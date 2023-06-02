from random import random

import random

def gerar():
    x = random.randint(1,3)
    return x

gabarito = []
apostador1 = []
apostador2 = []
apostador3 = []
acerto1 = 0
acerto2 = 0
acerto3 = 0

for i in range (13):
    gabarito.append(gerar())
    apostador1.append(gerar())
    apostador2.append(gerar())
    apostador3.append(gerar())

print("Gabarito:\n{}".format(gabarito))
print("Apostador 1:\n{}".format(apostador1))
print("Apostador 2:\n{}".format(apostador2))
print("Apostador 3:\n{}\n".format(apostador3))

for i in range(13):
    if apostador1[i] == gabarito[i]:
        acerto1 += 1
    if apostador2[i] == gabarito[i]:
        acerto2 += 1
    if apostador3[i] == gabarito[i]:
        acerto3 += 1

print("Apostador 1: {}".format(acerto1))
print("Apostador 2: {}".format(acerto2))
print("Apostador 3: {}".format(acerto3))

if acerto1 == 13:
    print("O jogador 1 Ganhou")
if acerto2 == 13:
    print("O jogador 2 Ganhou")
if acerto3 == 13:
    print("O jogador 3 Ganhou")
else:
    print("Nao houve ganhador")