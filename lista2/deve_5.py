'''5. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado pelo usuário.'''

def conta_digitos(numero):
    return len(str(numero))
numero = int(input("Digite um número inteiro: "))
print("O número", numero, "possui", conta_digitos(numero), "dígitos.")
