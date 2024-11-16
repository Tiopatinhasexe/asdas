import os
import time

# Limpar tela
os.system("cls || clear")

# Constante.
quantidade_notas = 4

# Função.
def logo_senai ():
    os.system("cls || clear")
    print ("===SENAI===")

def calcular_media(lista_notas):
# Processamento.
    soma = sum(lista_notas)
    media = soma / quantidade_notas
    return media

# Entrada.
# Vetor
lista_de_notas = []

for i in range(quantidade_notas):
    logo_senai()
    nota = float(input("Digite a nota: "))
    lista_de_notas.append(nota)

media = calcular_media(lista_de_notas)

# Saída
logo_senai ()
for cada_nota in lista_de_notas:
    print(f"Nota: {cada_nota}")

print(f"Media: {media}")