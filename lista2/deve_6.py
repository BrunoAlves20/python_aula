'''6. Faça uma função chamada somalmposto. A função possui dois parâmetros:

a) taxImpostolmposto, que é a porcentagem de imposto sobre vendas

b) custo, que é o custo de um item antes do imposto.
A função retorna o valor de custo alterado para incluir o imposto sobre vendas.'''

def somalmposto(taxImpostolmposto, custo):
    return custo + (custo * (taxImpostolmposto / 100))

taxa = 15
custo = 200
print(f"O custo do item é R$ {custo:.2f}, com {taxa}% de imposto o valor final será R$ {somalmposto(taxa, custo):.2f}")

