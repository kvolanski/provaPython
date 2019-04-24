import calculadora

def Menu(x,y):

    print("O que gostaria de fazer:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    opcao = input()
    x = x
    y = y
    opcoes(int(opcao),x,y)

def opcoes(opcao,x,y):
        if opcao == 1:
            calculadora.soma(x,y)
        elif opcao == 2:
            calculadora.subtracao(x,y)
        elif opcao == 3:
            calculadora.multiplicacao(x,y)
        elif opcao == 4:
            calculadora.divisao(x,y)
        else:
            print("Opção errada, selecione novamente")
            pegaNumeros()

def pegaNumeros():
    print("Bem vindo ao calculadora do Kevin")
    x = int(input("Digite o primeiro numero"))
    y = int(input("Digite o segundo numero"))
    Menu(x,y)
