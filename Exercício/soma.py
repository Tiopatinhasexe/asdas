import os
import time
os.system("cls || clear")

# implemente um algoritmo que, usando recursividade.
# receba um numero como parametro e some todos os numeros
# de zero ate o numero informado.

# funcao
def contagem_regressiva(numero):
    if numero < 0:
            return
    print(numero)
    time.sleep(2)
    # chamada recursiva.
    contagem_regressiva(numero -1)


# codigo principal.
print("contagem regressiva...")
contagem_regressiva(2) #chamada da funcao

def contagem_regressiva(numero):
    soma = contagem_regressiva(2) + contagem_regressiva(2)
    soma = contagem_regressiva(2)(contagem_regressiva(2))
    return soma
print(f"resultado {contagem_regressiva}")
print("===fim===")