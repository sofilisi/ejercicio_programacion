class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = año_publicacion

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año de publicación: {self.año_publicacion}")
