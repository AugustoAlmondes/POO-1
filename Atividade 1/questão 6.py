preco = 5.00
quantidade = 120
lmaximo = 0
pmaximo = 0
qmaximo = 0

while(preco != 1.00):
    lucro = preco * quantidade
    lucro = lucro - 200
    print("preço ingresso = {:.2f}, quantidade = {}, lucro = {:.2f}".format(preco, quantidade, lucro))
    preco = preco - 0.5
    quantidade = quantidade + 26
    if(lucro > lmaximo):
        lmaximo = lucro
        pmaximo = preco
        qmaximo = quantidade
print("\n")
print("Lucro maximo = {:.2f}\nPreco do ingresso = {:.2f}\nQuantidade vendida = {}".format(lmaximo,pmaximo + 0.5,qmaximo-26))