"""
Crie uma calculadora que consiga executar as funções destacadas da calculadora
padrão do windows 10.

"""

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def porcentagem(a, percentual):
    return (a * percentual) / 100

def calculadora():
    print("Bem-vindo à calculadora!")
    while True:
        print("\nEscolha a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Porcentagem")
        print("6. Sair")
        
        escolha = input("Digite o número da operação desejada: ")
        
        if escolha == '6':
            print("Obrigado por usar a calculadora!")
            break
        
        num1 = float(input("Digite o primeiro número: "))
        
        if escolha != '5':
            num2 = float(input("Digite o segundo número: "))
        
        if escolha == '1':
            print("Resultado:", soma(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtracao(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicacao(num1, num2))
        elif escolha == '4':
            print("Resultado:", divisao(num1, num2))
        elif escolha == '5':
            percentual = float(input("Digite a porcentagem: "))
            print("Resultado:", porcentagem(num1, percentual))
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

calculadora()