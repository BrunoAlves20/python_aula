class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def vender(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
            print(f"Venda realizada: {qtd} unidades de {self.nome}")
        else:
            print(f"Estoque insuficiente. Disponível: {self.quantidade}")

    def repor(self, qtd):
        self.quantidade += qtd
        print(f"Estoque reposto: {qtd} unidades de {self.nome}")

    def exibir_estoque(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade}")

p1 = Produto("Notebook", 3500.00, 10)

p1.exibir_estoque()
p1.vender(3)
p1.exibir_estoque()
p1.repor(5)
p1.exibir_estoque()
