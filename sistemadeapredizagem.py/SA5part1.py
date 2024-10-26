import os
os.system ("cls || clear")

# Adicionando um elemento no topo da pilha.
print("Inserindo um elemento: " )

lista = []
while True:
 print('''\nMenu de opções
      1 Empilhar - Adicionar um elemento no topo da pilha
      2 Desempilhar - Remover e retornar um elemento do topo da pilha
      3 Limpar - Remover todos os elementos da pilha
      4 Listar - Lista todos os elementos armazenados na pilha
      5 Vazia - Retornar ao verdadeiro se a pilha estiver vazia, e falso caso contrário ''')
 x = int(input('Digite a ação tomada: \n'))
print('\n')