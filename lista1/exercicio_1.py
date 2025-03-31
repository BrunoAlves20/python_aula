""" Escreva um programa que receba uma lista de 10 inteiros via teclado, em seguida o progama deve soliciatar um número e informa se o número também está na lista ou não"""

#inicializa uma lista vazia para armazenar os números
numeros = []

for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

# Solicita um número ao usuário para verificar se está na lista
numero_procurado = int(input("Digite um número para verificar se está na lista: "))
if numero_procurado in numeros:
    print(f"O número {numero_procurado} está na lista.")
else:
    print(f"O número {numero_procurado} não está na lista.")