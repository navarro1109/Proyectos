class Libro:
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas
        numero_paginas = int(numero_paginas)
        anio_publicacion = int(anio_publicacion)
        
    def mostrar_informacion (self):
        print("Libro: ", self.titulo, "\nAño de publicacion :", self.anio_publicacion, "\nAutor: ", self.autor, "\nPaginas: ", self.numero_paginas)
        

      
      #self significa una instancia que accede a cada dato

titulo = "Red Rising"
autor = "Pierce Brown"
numero_paginas = 416
anio_publicacion = 2014

sinfo = Libro(titulo, autor, anio_publicacion, numero_paginas)

sinfo.mostrar_informacion()

