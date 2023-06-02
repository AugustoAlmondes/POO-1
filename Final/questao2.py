
class Livro:
    def __init__(self,titulo, autor, data, preco):
        self._titulo = titulo
        self._autor = autor
        self._data = data
        self._preco = preco
    
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self,titulo):
        self._titulo = titulo

    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self,autor):
        self._autor = autor
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self,data):
        self._data = data
    
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self,preco):
        self._preco = preco

class Biblioteca:
    def __init__(self):
        self.dic_biblioteca = {}

    def adicionar(self,livro,titulo):
        self.dic_biblioteca[titulo] = livro
    
    def procurar(self,livro):
        if livro in self.dic_biblioteca.keys():
            return True
        else:
            return False
    
    def verificar(self, titulo):
        if not titulo in self.dic_biblioteca.keys():
            return True
        else:
            return False

    def exibir(self,titulo):
            print("Titulo: {}".format(self.dic_biblioteca[titulo].titulo))
            print("Autor: {}".format(self.dic_biblioteca[titulo].autor))
            print("Data de Criação: {}".format(self.dic_biblioteca[titulo].data))
            print("Preço: {:.2f}".format(self.dic_biblioteca[titulo].preco))
            print("_________________________")

    def exibirT(self):
        for i in self.dic_biblioteca.keys():
            print("Titulo: {}".format(self.dic_biblioteca[i].titulo))
            print("Autor: {}".format(self.dic_biblioteca[i].autor))
            print("Data de Criação: {}".format(self.dic_biblioteca[i].data))
            print("Preço: {:.2f}".format(self.dic_biblioteca[i].preco))
            print("_________________________")

biblioteca = Biblioteca()
while True:
    try:
        opcao = int(input("Digite a opcao: \n"
        "0 - Sair\n"
        "1 - Adicionar Livro\n"
        "2 - Exibir Livro\n"
        "3 - Exixbir Todos\n"
        "opcao: "))
        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 0:
            print("_____________________")
            print("Valor Incorreto")
            print("_____________________")
        else:
            if opcao == 1:
                quant = int(input("Digite a Quantidade de Livros: "))

                for i in range (quant):
                    print("______________________")
                    titulo = input("Titulo: ")
                    if biblioteca.verificar(titulo):
                        autor = input("Autor: ")
                        data = input("Data de Criação: ")
                        preco = float(input("Preço: "))
                        print("_____________________")

                        livro = Livro(titulo, autor,data,preco)
                        biblioteca.adicionar(livro,titulo)
                    else:
                        print("_____________________")
                        print("Livro ja está cadastrado")
            elif opcao == 2:
                livro = input("Digite o Livro a ser exibido: ")
                
                if biblioteca.procurar(livro):
                    biblioteca.exibir(livro)
                else:
                    print("Esse livro não está cadastrado")
                    print("_____________________")
            
            elif opcao == 3:
                biblioteca.exibirT()
            
            elif opcao == 0:
                break
    except ValueError:
        print("_____________________")
        print("Mensagem Incorreta")
        print("_____________________")