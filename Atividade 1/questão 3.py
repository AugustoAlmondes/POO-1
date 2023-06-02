def fatorial(numero):
    cont = 1
    fat = 1
    while cont <= numero:
        fat = cont * fat
        cont += 1
    return fat


opcao = int(input("Escolha as seguintes opcoes:\n -1 Para combinacao\n -2 Para arranjo\n "))
if(opcao == 1):
    n, r = map(int, input("Digite dois numeros: ").split())
    valor = fatorial(n)
    valor2 = fatorial(r)
    valor3 = fatorial(n - r)
    valor = valor/(valor2 * valor3)
    print(valor)
if(opcao == 2):
    n, p = map(int, input("Digite dois numero: ").split())
    valor = fatorial(n)
    valor2 = fatorial(n-p)
    valor = valor/valor2
    print(valor)