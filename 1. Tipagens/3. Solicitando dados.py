import os

os.system("cls || clear") #Limpa o terminal.

# Entrada.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade "))
peso = float (input("Digite seu peso "))

# Saída.
print("Seu nome é {} tem {} anos e pesa {}kg".format(nome, idade, peso))