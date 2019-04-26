def soma(x,y):
    soma = x + y
    texto = "Você somou " + str(x) + " + " + str(y) + " e deu " + str(soma)
    print(texto)
    validaPar(soma,texto)

def subtracao(x,y):
    subtracao = x - y
    texto = "Você subtraiu " + str(x) + " - " + str(y) + " e deu " + str(subtracao)
    print(texto)
    validaPar(subtracao,texto)

def multiplicacao(x,y):
    multiplicacao = x * y
    texto = "Você multiplicou " + str(x) + " * " + str(y) + " e deu " + str(multiplicacao)
    print(texto)
    validaPar(multiplicacao,texto)

def divisao(x,y):
    if x == 0 or y == 0:
        print("Não é possível dividir por 0")
    else:
        divisao = x / y
        texto = "Você dividiu " + str(x) + " / " + str(y) + " e deu " + str(divisao)
        print(texto)
        validaPar(divisao,texto)

def validaPar(numero,texto):
    if int(numero) % 2 == 0:
        texto = texto
        salvaArquivo(texto)
    else:
        exit()


def salvaArquivo(texto):
    print("Salvando arquivo")
    arq = open("calculadora.txt", "a")
    arq.write(texto)
    arq.write("\r")