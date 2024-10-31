class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: miau")
