import os
import time

# Limpar tela
os.system("cls || clear")

login_cadastrado = "marta"
senha_cadastrado = "123"
tentativas = 0

# Entrada
while True:
    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")
    tentativas += 1

    # Processamento
    if login == login_cadastrado and senha == senha_cadastrado:
        print("Acesso ao sistema!")
        break
    
    if tentativas >= 3:
        print("Limite de 3 tentativas excedido!")
        break

