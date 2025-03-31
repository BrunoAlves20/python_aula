'''2. Criar uma função para retornar se um número se é par ou impar'''

def par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = int(input("Digite um número: "))
resultado = par_impar(numero)
print(f"O número {numero} é {resultado}")