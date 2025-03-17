''' Faça um programa que incialize uma lista com vários númreros diferentes, depois disso, solicite ao usuário um número,
 verifique se o número está ou não na lista e exiba uma mensagem notificando o usuário do resultado.'''

#inicializa uma lista com vários números diferentes
num_diferentes = [9,4,7,2,1,4,10]

#solicita ao usuário um número
for i in range(5):
    numero = int(input("Digite um número: "))
    num_diferentes.append(numero)

#se o número está ou não na lista
if numero in num_diferentes:
    print(f'o número{numero} está na lista')
else:
    print(f'o número{numero} não está na lista')
