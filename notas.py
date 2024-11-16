import os
import time

# Limpar tela
os.system("cls || clear")

notas = 0
quantidade_de_notas = 4

# entrada
for i in range(quantidade_de_notas):
    #iteracao = 2
    # notas = 2
    notas += float(input("Digite uma nota: "))

# processamento
media = notas / quantidade_de_notas

# saida
print(f"Media{media}")