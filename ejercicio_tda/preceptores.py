# preceptores.py

def preceptores_por_año(cursos):
    preceptores = {}
    for curso in cursos:
        año = curso['curso'][0]
        preceptor = curso['preceptor']
        if año not in preceptores:
            preceptores[año] = set()
        preceptores[año].add(preceptor)
    return preceptores

def preceptores_repetidos(cursos):
    preceptores = {}
    repetidos = set()
    for curso in cursos:
        preceptor = curso['preceptor']
        año = curso['curso'][0]
        if preceptor in preceptores and preceptores[preceptor] != año:
            repetidos.add(preceptor)
        preceptores[preceptor] = año
    return repetidos

def preceptores_unicos_por_año(cursos, año_deseado):
    preceptores_año = [curso['preceptor'] for curso in cursos if curso['curso'][0] == año_deseado]
    return set(preceptores_año)
