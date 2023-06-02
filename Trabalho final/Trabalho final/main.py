from classes import *
from random import randint
from imposto import *

armazena = Armazena()
Imposto.register(Produto)

def gerarcodigo():
    return randint(100,1000)

def verificar(verificar_cpf):
    for i in armazena._dic_funcionario.keys():
        if armazena._dic_funcionario[i].cpf == verificar_cpf:
            return 1

def verificarC(verificar_cpf):
    for i in armazena._dic_cliente.keys():
        if armazena._dic_cliente[i].cpf == verificar_cpf:
            return 1

def verificarProduto(marca):
    for i in armazena._dic_produto.keys():
        if armazena._dic_produto[i]._marca == marca:
            print("PRODUTO CADASTRADO")
            return 1

def procurarCodigo(marca):
    for i in armazena._dic_produto.keys():
        if armazena._dic_produto[i]._marca == marca:
            return i 

def calcularImposto():
    imposto = 0.0
    verificar = Verifica()
    for y in armazena._dic_produto.keys():
        imposto = verificar.calcular(armazena._dic_produto[y])
        armazena._lista_imposto.append(imposto)
    print("________________________\nValor do Imposto: R${:.2f}".format(imposto))

opcao = -1

while opcao != 0:
    try:
        opcao = int(input("________________________\n---SEJA BEM VINDO AO BÁSICO DE CASA---\n       Sua loja Boa e Barata\n"
        "________________________"
        "\n 0 - sair"
        "\n 1 - Cadastrar Funcionario"
        "\n 2 - Cadastrar Cliente"
        "\n 3 - Adicionar Produto"
        "\n 4 - Repor Estoque"
        "\n 5 - Realizar Compra"
        "\n 6 - Prateleira"
        "\n 7 - Verificar Estoque"
        "\n 8 - Embalar Produto"
        "\n________________________"
        "\nDigite o numero da função: "))

        if opcao == 1:
            print('---ADICIONAR FUNCIONARIO---')
            nome = input("________________________\nDigite o nome do Usuário: ")
            cpf = int(input("Digite o CPF(11 Dígitos): "))
            if verificar(cpf) != 1:
                data = input("Digite a Data de Nascimento: ")
                salario = float(input("Digite o Salário: "))
                armazena._dic_funcionario[cpf] = Funcionario(nome,cpf,data,salario)
                print("FUNCIONÁRIO REGISTRADO COM SUCESSO!")
            else:
                print("________________________\nFuncionario ja cadastrado")

        elif opcao == 2:
            print('---ADICIONAR CLIENTE---')
            nome = input("________________________\nDigite o nome do Usuário: ")
            cpf = int(input("Digite o CPF (11 Dígitos): "))
            if verificarC(cpf) != 1:
                data = input("Digite a Data de Nascimento: ")
                profissao = input("Digite a Profissao do usuário: ")
                cliente = Cliente(nome, cpf, data, profissao)
                armazena._dic_cliente[cpf] = Cliente(nome, cpf, data, profissao)
                print("CLIENTE REGISTRADO COM SUCESSO!")
            else:
                print(    "________________________\nCliente ja cadastrado")

        elif opcao == 3:
            print('---ADICIONAR PRODUTO---')
            marca = input("________________________\nDigite o nome do Produto: ")
            i = verificarProduto(marca)
            if i != 1:
                codigo = gerarcodigo()
                valor = float(input("Digite o Valor do Produto: "))
                quantidade = int(input("Digite a Quantidade do Produto: "))
                produto = Produto(codigo,marca,valor,quantidade)
                armazena._dic_produto[codigo] = Produto(codigo,marca,valor,quantidade)
                print("PRODUTO REGISTRADO COM SUCESSO!")
                calcularImposto()
            else:
                print("Produto ja cadastrado")

        elif opcao == 4:
            print('---REPOR ESTOQUE---')
            marca = marca = input("________________________\nDigite o nome do Produto: ")
            valor = verificarProduto(marca)
            if valor == 1:
                i = procurarCodigo(marca)
                quantidade = int(input("Digite a Quantidade do Produto: "))
                armazena._dic_produto[i].reporEstoque(quantidade)
                calcularImposto()
            else:
                print("Produto não Cadastrado")

        elif opcao == 5:
            print('---REALIZAR COMPRA---')
            marca = input("________________________\nDigite o nome do Produto: ")
            valor = verificarProduto(marca)
            if valor == 1:
                i = procurarCodigo(marca)
                quant = int(input("________________________\nDigite a Quantidade: "))
                opcao2 = int(input("O Cliente possui Cadastro na Loja?\n"
                "1 - Sim\n"
                "2 - Não\n"
                "Opcao: "))
                if opcao2 == 1:
                    cpf = int(input("Digite o CPF: "))
                    verificarcpf = verificar(cpf)
                    if verificarcpf == 1:
                        print("________________________\n Cliente {} possui cadastro".format(armazena._dic_cliente[cpf].nome))
                        desconto = 0.2
                        armazena._dic_produto[i].realizarCompra(marca,quant,desconto)
                    else:
                        print("Cliente não possui cadastro")
                elif opcao2 == 2:
                    desconto = 0
                    armazena._dic_produto[i].realizarCompra(marca,quant,desconto)
            else:
                print("Produto não Cadastrado")

        elif opcao == 6:
            print('---PRATELEIRA---')
            for i in armazena._dic_produto.keys():
                armazena._dic_produto[i].prateleira()

        elif opcao == 7:
            print('---VERIFICAR ESTOQUE---')
            for i in armazena._dic_produto.keys():
                armazena._dic_produto[i].verificaEstoque()

        elif opcao == 8:
            Produto.embalar()

    except ValueError:
        print("ERRO")