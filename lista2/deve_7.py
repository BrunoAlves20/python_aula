'''7. Criar uma função para gerar uma matriz 10x10 (array) de forma aleatória.'''

import random

def criar_matriz():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(random.randint(0, 50))
        matriz.append(linha)
    return matriz
matriz = criar_matriz()
for linha in matriz:
    print(linha)
