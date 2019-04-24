



def soma(x,y):
    soma = x + y
    print(soma)
    texto = "Você somou" + str(x) + " + " + str(y) + " e deu " + str(soma)
    validaPar(soma)

def subtracao(x,y):
    subtracao = x - y
    print(subtracao)
    validaPar(subtracao)

def multiplicacao(x,y):
    multiplicacao = x * y
    print(multiplicacao)
    validaPar(multiplicacao)

def divisao(x,y):
    if x or y == 0:
        print("Não é possível dividir por 0")
    else:
        divisao = x / y
        print(divisao)
        validaPar(divisao)

def validaPar(numero):
    if int(numero) % 2 == 0:
        salvaArquivo()
    else:
        ("Funcao de voltar ao menu aqui")

def salvaArquivo():
    print("Salvando arquivo")