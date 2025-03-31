'''Faça um programa que inicialize um lista vazia e a preencha com 5 nomes diferntes  digitados pelo usuário,
 depois disso solicite um número de 0 até 4 e remova o elemento desta posição.'''

#inicializa uma lista vazia
lista_nomes = []

#preenche a lista com 5 nomes diferentes digitados pelo usuário
for i in range(5):
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)

#solicita um número de 0 a 4
numero = int(input("Digite um número de 0 a 4: "))

if numero >= 0 and numero < 5:
    lista_nomes.pop(numero)
    print("Elemento removido com sucesso!")
else:
    print("Número inválido!")