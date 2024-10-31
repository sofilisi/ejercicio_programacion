from libro import Libro
from rectangulo import Rectangulo
from calculadora import Calculadora
from animal import Perro, Gato
from cuenta_bancaria import CuentaBancaria

# Ejemplo de uso de la clase Libro
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
libro1.mostrar_informacion()

# Ejemplo de uso de la clase Rectangulo
rectangulo1 = Rectangulo(5, 3)
print(f"Área: {rectangulo1.calcular_area()}")
print(f"Perímetro: {rectangulo1.calcular_perimetro()}")

# Ejemplo de uso de la clase Calculadora
calc = Calculadora()
print(f"Suma: {calc.sumar(5, 3)}")
print(f"Resta: {calc.restar(5, 3)}")
print(f"Multiplicación: {calc.multiplicar(5, 3)}")
print(f"División: {calc.dividir(5, 3)}")

# Ejemplo de uso de las clases Animal, Perro y Gato
perro1 = Perro("Rex")
gato1 = Gato("Felix")
perro1.hacer_sonido()
gato1.hacer_sonido()

# Ejemplo de uso de la clase CuentaBancaria
cuenta1 = CuentaBancaria("Juan", 1000)
cuenta1.obtener_saldo()
cuenta1.depositar(500)
cuenta1.obtener_saldo()
cuenta1.retirar(200)
cuenta1.obtener_saldo()
