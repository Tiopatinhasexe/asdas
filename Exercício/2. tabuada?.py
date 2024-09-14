import os

os.system("cls || clear") #Limpa o terminal.

# Entrada de dados.
numero = int(input("Digite um número: "))

for i in range (1,11):
    print(f"{numero} x {i} = {numero * i}")

# for i in range (5)
# print(f"{numero} x {i+1} = {numero * (i1)})