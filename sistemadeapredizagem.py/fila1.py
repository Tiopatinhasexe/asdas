import os
os.system ("cls || clear")

# Cria uma fila com tres elementos.
fila =["Banana", "Maçã", "Pera"]
print("Fila: ", fila)

# Adiciona um elemnto ao final da fila.
fila.append ("Uva")
print("Adicionando um elemento: ", fila)

# Remove o primeiro elemento adicionado à fila.
fila.pop(0)
print("Removendo um elemento: ", fila)