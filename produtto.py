import os
import time

# Limpar tela
os.system("cls || clear")

# Entrada
valor = int(input("Qual valor? "))

# Introduçao
if valor < 100:
    desconto = valor * 1.1
    valor_inflado = valor + desconto
else:
    desconto = valor * 1.2
    valor_inflado = valor + desconto

# Saida
print(f"Valor com desconto: {valor_inflado}")