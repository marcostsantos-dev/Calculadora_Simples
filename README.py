# Calculadora_Simples
"""
Esta é uma calculadora simples que realiza as operações de adição, subtração, multiplicação e divisão.
O usuário deve inserir dois números e, em seguida, selecionar a operação desejada (+, -, *, /).

"""
#Descrição do App
print('-'*11)
print("CALCULADORA")
print('-'*11)
print(
    """Operadores:
[+]Adição"
[-]Subtração"
[*]Multiplicação"
[/]Divisão"""
)
print('-'*11)
#Entrada de valores e operador no App pelo usuário
numero_1 = float(input("\nDigite um numero: "))
numero_2 = float(input("\nDigite um numero: "))
operacao = input("Digite o operador: ")
match operacao:
    case '+':
        print(numero_1+numero_2)
    case '-':
        print(numero_1-numero_2)
    case '*':
        print(numero_1*numero_2)
    case '_':
        print(numero_1/numero_2)
