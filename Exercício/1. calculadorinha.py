import os

os.system("cls || clear") #Limpa o terminal.

resultado = 0

# Entrada.
n1 = int(input("Digite um número: "))
operacao = input("Escolha sua operação: ")
n2 = int(input("Digite outro número: "))

# Processamento.
match operacao:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "/":
        resultado = n1 / n2
    case "*":
        resultado = n1 * n2
    
# Saída.
print(f"Resultado: {resultado}")