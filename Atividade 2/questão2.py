lista = [0,1,[2,[3,4]],5] 

def ImpList(lista):
    
    for i in lista:

        if(type(i) == list):
            for j in i:

                print(j)
        else:

            print(i)

def main():
    ImpList(lista)
main()