import os
import time

# Limpar tela
os.system("cls || clear")

# Introduçao

# Menu principal
print("\n1 – Menos de uma dúzia de maças - R$1,30\n2 – Dúzia de maças - R$1,00")
    
#    
opcao = float(input("Quantas maças gostaria de comprar?: "))

# Escolha
if opcao  < 12:
    resultado = 1.3 * opcao
    print((f"Preço - {resultado} "))

else:
    resultado = 1.0 * opcao
print((f"Preço - {resultado} "))