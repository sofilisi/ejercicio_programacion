class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def obtener_saldo(self):
        print(f"El saldo actual es: {self.__saldo}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de {cantidad} realizado exitosamente.")
        else:
            print("La cantidad a depositar debe ser mayor a cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro de {cantidad} realizado exitosamente.")
        else:
            print("Fondos insuficientes o cantidad inválida.")
