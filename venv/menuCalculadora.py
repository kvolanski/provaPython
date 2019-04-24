

def Menu():
    print("Bem vindo ao calculadora do Kevin")
    print("O que gostaria de fazer:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    input(int(opcao))
    opcoes(opcao)

def opcoes(opcao):
        if opcao == 1:
            calculadora.Soma()
        elif opcao == 2:
            calculadora.Subtracao()
        elif opcao == 3:
            calculadora.Multiplicacao()
        elif opcao == 4:
            calculadora.Divisao()
        else:
            print("Opção errada, selecione novamente")
            Menu()
