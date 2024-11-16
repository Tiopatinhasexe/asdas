# implemente um algoritmo que, usando recursividade.
# receba um numero como parametro e some todos os numeros
# de zero ate o numero informado.

import os
os.system("cls || clear")

def somar_numero(numero):
    if numero == 0:
        return 0
    else:
        print(f"{numero} + {numero -1}")
        return numero + somar_numero(numero - 1)
    
print(f"Soma: {somar_numero(5)}")