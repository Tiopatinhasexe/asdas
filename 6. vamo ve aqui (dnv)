import os

#Limpa o terminal.
os.system("cls || clear")

# Constante.
QUANTIDADE_DE_NOTAS = 3

# Função.
def logo_senai ():
    os.system("cls || clear")
    print ("===SENAI===")

def calcular_media(lista_notas):
# Processamento.
    soma = sum(lista_notas)
    media = soma / QUANTIDADE_DE_NOTAS
    return media

# Entrada.
# Vetor
lista_de_notas = []

for i in range(QUANTIDADE_DE_NOTAS):
    logo_senai()
    nota = float(input("Digite a nota: "))
    lista_de_notas.append(nota)

media = calcular_media(lista_de_notas)

# Saída
logo_senai ()
for cada_nota in lista_de_notas:
    print(f"Nota: {cada_nota}")

print(f"Media: {media}")
