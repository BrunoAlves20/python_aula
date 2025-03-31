'''ler uma lista de 5 números inteiros mostre cada número jutamente com a sua posição na lista.'''

numeros_inteiro = []

#ler 5 números inteiros
for i in range(5):
    numero = int(input(f"Número {i+1}: "))
    numeros_inteiro.append(numero)

#exibe cada número juntamente com a sua posição na lista
for i, numero in enumerate(numeros_inteiro):
    print(f"Posição {i}: {numero}")