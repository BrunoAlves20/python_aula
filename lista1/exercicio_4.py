''' Faça um programa que inicialize um lista vazia e solicite ao usuário 3 nomes de cidades, um por vez, 
cada vez que o usuário digitar um nome,o programa deve incluir este nome na lista de cidades'''

#inicializa uma lista vazia para armazenar as cidades
cidades = []

#solicita ao usuário 3 nomes de cidades, um por vez
for i in range(3):
    nome_cidade = input("Digite o nome da cidade: ")
    cidades.append(nome_cidade)

#exibe a lista de cidades
print("Lista de cidades:")
for cidade in cidades:
    print('>',cidade)