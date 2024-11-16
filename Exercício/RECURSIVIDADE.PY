import os
import time
os.system("cls || clear")

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
contagem_regressiva(5) #chamada da funcao
print("===fim===")