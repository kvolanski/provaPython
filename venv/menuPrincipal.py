import menuCalculadora
import lojinha


def abreLojinha():
    print("IMPRIMINDO...")
    arq = open("lojinha.txt", "a")
    arq = open("lojinha.txt", "r")
    texto = arq.read()
    print(texto)
    arq.close()


def abreCalculadora():
    print("IMPRIMINDO...")
    arq = open("calculadora.txt", "a")
    arq = open("calculadora.txt", "r")
    texto = arq.read()
    print(texto)
    arq.close()

def relatorios():
    abreLojinha()
    abreCalculadora()
    comecaAqui()


def comecaAqui():
    print("O que quer fazer?")
    print("1 - Calculadora")
    print("2 - Lojinha")
    print("3 - Relatorios")

    opcao = int(input())

    if opcao == 1:
        menuCalculadora.pegaNumeros()
    elif opcao == 2:
        lojinha.menu()
    elif opcao == 3:
        relatorios()
    else:
        comecaAqui()

comecaAqui()



