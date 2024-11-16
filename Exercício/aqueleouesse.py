import os
import time
os.system("cls || clear")

# Entrada

def par_impar(numero):
    if numero % 2 == 0:
        print("par")
    else:
        print("impar")

numero = int(input("Digite um numero: "))

par_impar(numero)