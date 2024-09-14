import os

os.system("cls || clear") #Limpa o terminal.

# Entrada.
nota = int(input("Digite uma nota:"))

# Processamento.
if nota >= 7:
    resultado = "Aprovado."
# entre 5 e 7
elif nota >= 5:
     resultado = "Recuperação."
elif nota >= 4:
     resultado = "Conselho de classe."
else:
     Resultado = "Reprovado."

     # Saída.
     print (f"Resultado: (resultado)")