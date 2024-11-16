import os
import time

# Limpar tela
os.system("cls || clear")

# Receber quantidade de usuários
n1 = int(input("Quantos usuários serão cadastrados? "))

# Criar lista para armazenar usuários
usuarios = []

# Menu principal
while True:
    print("\n1 – Cadastrar novo usuário\n2 – Listar todos os usuários cadastrados\n3 – Sair do sistema")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Cadastrar novo usuário
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        usuarios.append({"nome": nome, "idade": idade})
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        # Listar todos os usuários cadastrados
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            for i, usuario in enumerate(usuarios):
                print(f"Usuário {i+1}: {usuario['nome']}, {usuario['idade']} anos")

    elif opcao == "3":
        # Sair do sistema
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")