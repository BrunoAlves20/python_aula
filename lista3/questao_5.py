class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def aprovado(self):
        return self.media() >= 7


aluno1 = Aluno("Maria", 8.0, 7.5)
print(f"Média de {aluno1.nome}: {aluno1.media():.2f}")
print("Aprovado?" , aluno1.aprovado())  # True

aluno2 = Aluno("Bruno", 5.0, 6.0)
print(f"Média de {aluno2.nome}: {aluno2.media():.2f}")
print("Aprovado?" , aluno2.aprovado())  # False
