import os

#Limpa o terminal.
os.system("cls || clear")

#Funções
def calcular_soma(n1, n2):
    soma = n1 + n2
    return soma

def calcular_subtracao(n1, n2):
    return n1 - n2

def calcular_multiplicacao(n1, n2):
    return n1 * n2

#Entrada
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

#Processamento
soma = calcular_soma(n1, n2)
subtracao = calcular_subtracao(n1, n2)
multiplicacao = calcular_multiplicacao (n1, n2)

#Saida
print(f"resultado {soma}")
print(f"resultado {subtracao}")
print(f"resultado {multiplicacao}")