# utilidades.py

def mostrar_menu():
    print("Menú de opciones:")
    print("1 - Cargar lista de alumnos")
    print("2 - Cargar lista de cursos")
    print("3 - Generar set de preceptores por año")
    print("4 - Obtener promedio de edad de un curso")
    print("5 - Buscar preceptores repetidos en distintos años")
    print("6 - Buscar preceptores únicos en un año")
    print("7 - Mostrar alumno más joven y más grande")
    print("8 - Salir")
    
def obtener_opcion():
    try:
        return int(input("Seleccione una opción: "))
    except ValueError:
        print("Opción inválida. Intente de nuevo.")
        return None
