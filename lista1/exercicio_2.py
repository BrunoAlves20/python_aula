'''Escreva um programa que leia e mostre uma lista de 10 elementos inteiros .Em seguida, conte  quantos valores pares existem na lista ,por fim exiba a quantida de tela.'''

#inicializa uma lista vazia para armazenar os números
numeros = []

for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
#conta quantos valores pares existem na lista
pares = sum(1 for numero in numeros if numero % 2 == 0)

#exibe a quantidade de números pares na lista
print(f"A quantidade de números pares na lista é : {pares}")
print(f" Quantidade de números na lista : {numeros}")