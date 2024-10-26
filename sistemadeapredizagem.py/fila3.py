import os
os.system("cls || clear")

fila = []

for i in range (3):
    texto = input("Digite uma string: ")
    fila.append(texto)
print(fila) # Saída: [str1, str2, str 3]

# Removendo o elemento mais antigo da fila
primeiro_elemento = fila.pop(0)
print(primeiro_elemento) # Saída: str1
print(fila) # Saída: [str2, str3]