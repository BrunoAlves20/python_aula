class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente para saque.")
        elif valor <= 0:
            print("O valor do saque deve ser positivo.")
        else:
            self.__saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')

    def exibir_saldo(self):
        print(f'Saldo atual de {self.__titular}: R${self.__saldo:.2f}')

conta = ContaBancaria("Bruno", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(300)
conta.sacar(1500)  # Deve impedir o saque
conta.exibir_saldo()
