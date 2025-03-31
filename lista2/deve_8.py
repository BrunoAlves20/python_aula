'''8. Faça um programa que tenha uma lista pronta chamada números e duas funções chamadas sorteia() e somaPar(). 
A A primeira função vai sortear 5 números da lista e vai colocá-los em outra lista e
 a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior. 
 (Utilize o import Random e a função sorteados ficará parcialmente: sorteados = random.sample(lista,5))'''

import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sorteia(lista):
    sorteados = random.sample(lista, 5)
    print(f"Números sorteados: {sorteados}")
    return sorteados

def somaPar(lista):
    soma = sum(num for num in lista if num % 2 == 0)
    print(f"A soma dos números pares é: {soma}")
    return soma

sorteados = sorteia(numeros)
somaPar(sorteados)
