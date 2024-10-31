# cursos.py

def cargar_cursos():
    cursos = []
    while True:
        curso_info = input("Ingrese curso (formato: año-división o 'salir' para finalizar): ")
        if curso_info == 'salir':
            break
        curso = curso_info.split('-')
        curso = (int(curso[0]), curso[1])
        cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))
        preceptor = input("Ingrese el nombre del preceptor a cargo: ")
        curso_data = {
            'curso': curso,
            'cantidad_alumnos': cant_alumnos,
            'preceptor': preceptor
        }
        cursos.append(curso_data)
    return cursos

def promedio_edad(alumnos, curso):
    alumnos_del_curso = [alumno for alumno in alumnos if alumno['curso'] == curso]
    if not alumnos_del_curso:
        return 0
    total_edad = sum(alumno['edad'] for alumno in alumnos_del_curso)
    return total_edad / len(alumnos_del_curso)
