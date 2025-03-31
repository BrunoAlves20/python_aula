'''Ler uma lista de 10 números reais e mostre-os na ordem inversa.'''

numeros_reais = []

#ler 10 números reais
for i in range(10):
    numero = float(input(f"Número {i+1}: "))
    numeros_reais.append(numero)

#exibe os números na ordem inversa
print("Números na ordem inversa:")
for numero in reversed(numeros_reais):
    print(numero)