# alumnos.py

def cargar_alumnos():
    alumnos = []
    while True:
        nombre = input("Ingrese el nombre del alumno (o 'salir' para finalizar): ")
        if nombre == 'salir':
            break
        apellido = input("Ingrese el apellido del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        curso = input("Ingrese el curso (formato: año-división): ").split('-')
        curso = (int(curso[0]), curso[1])
        alumno = {
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad,
            'curso': curso
        }
        alumnos.append(alumno)
    return alumnos

def alumno_mas_joven_y_mas_grande(alumnos):
    if not alumnos:
        return None, None
    mas_joven = min(alumnos, key=lambda a: a['edad'])
    mas_grande = max(alumnos, key=lambda a: a['edad'])
    return mas_joven, mas_grande
