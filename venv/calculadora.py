def soma(x,y):
    soma = x + y
    texto = "Você somou " + str(x) + " + " + str(y) + " e deu " + str(soma)
    print(texto)
    validaPar(soma)

def subtracao(x,y):
    subtracao = x - y
    texto = "Você subtraiu " + str(x) + " - " + str(y) + " e deu " + str(subtracao)
    print(texto)
    validaPar(subtracao)

def multiplicacao(x,y):
    multiplicacao = x * y
    texto = "Você multiplicou " + str(x) + " * " + str(y) + " e deu " + str(multiplicacao)
    print(texto)
    validaPar(multiplicacao)

def divisao(x,y):
    if x or y == 0:
        print("Não é possível dividir por 0")

    else:
        divisao = x / y
        texto = "Você dividiu " + str(x) + " / " + str(y) + " e deu " + str(divisao)
        print(texto)
        validaPar(divisao)

def validaPar(numero):
    if int(numero) % 2 == 0:
        salvaArquivo()
    else:
        ("Funcao de voltar ao menu aqui")


def salvaArquivo():
    print("Salvando arquivo")