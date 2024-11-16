import os
import time

# Limpar tela
os.system("cls || clear")

# Menu principal
valor = int(input("Qual valor? "))

# Introduçao
desconto = valor * 0.1
valor_com_desconto = valor - desconto

# Saida
print(f"Valor com desconto: {valor_com_desconto}")

