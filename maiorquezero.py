import os
import time

# Limpar tela
os.system("cls || clear")

nota = 0

# inicio
while True:
    nota = int(input("Qual a sua nota? "))

    if nota <0 or nota >10:
        continue
    else:
        print(f"Nota: {nota}")
        break


print(nota)
