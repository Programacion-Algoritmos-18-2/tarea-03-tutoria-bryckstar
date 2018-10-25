class Docente:
    # Se crea el init para la clase Docente
    def __init__(self, n, x):
        self.nombre = n
        self.ciudad = x

    # Se agregan los nombres
    def agregar_nombre(self, n):
        self.nombre = n

    # Se retorna el nombre
    def obtener_nombre(self):
        return self.nombre

    def agregar_ciudad(self, x):
        self.ciudad = x

    def obtener_ciudad(self):
        return self.ciudad

    def presentar_datos(self):
        cadena = ("%s\n\t%s" % (self.obtener_nombre(), self.obtener_ciudad()))
        return cadena


class Estudiante:
    # Se crea el init para la clase Estudiantes
    def __init__(self, n, lista_docentes):
        self.nombres = n
        self.docentes = lista_docentes

    # Se agregan los nombres
    def agregar_nombre(self, n):
        self.nombres = n

    # Se retorna el nombre
    def obtener_nombre(self):
        return self.nombres

    def agregar_docente(self, lista_docentes):
        self.docentes = lista_docentes

    def obtener_docentes(self):
        return self.docentes

    def presentar_datos(self):
        cadena = "Nombre de el estudiante: %s\n" % (self.obtener_nombre())
        cadena = "%s%s\n" % (cadena, "lista de docentes:")
        for x in range(len(self.docentes)):
            cadena = "%s\n-%s|%s" % (cadena, self.docentes[x].obtener_nombre(), self.docentes[x].obtener_ciudad())
        return cadena
