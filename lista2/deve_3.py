'''3. Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(*num):
    maior = 0
    for n in num:
        if n > maior:
            maior = n
    print(f'O maior número é {maior}')

# exemplos de uso da função maior
maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
maior(100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)
maior() # aqui quando não tem nenhum numero ele retorna 0 é considerado o maior