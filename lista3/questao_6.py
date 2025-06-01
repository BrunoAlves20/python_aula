class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Departamento: {self.departamento}")

f1 = Funcionario("Bruno", 3000)
f1.exibir_dados()

print()

g1 = Gerente("Ana", 5000, "Recursos Humanos")
g1.exibir_dados()
