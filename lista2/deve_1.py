'''1. Crie uma função para calcular as quatro operações da matemática (soma, subtração, divisão e multiplicação)
 sendo fornecidos 2 números e informando o resultado de cada operação'''

def calculadora(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    divisao = num1 / num2
    multiplicacao = num1 * num2
    return soma, subtracao, divisao, multiplicacao

resultado = calculadora(10, 5)
print(resultado)

# Outra forma de  mostrar o resultado ( para visualizar basta descmentar o print abaixo)

# print('-'*10)
# num1 = 10
# num2 = 5
# soma, subtracao, divisao, multiplicacao = calculadora(num1, num2)
# print(f"Soma: {soma}")
# print(f"Subtração: {subtracao}")
# print(f"Divisão: {divisao}")
# print(f"Multiplicação: {multiplicacao}")