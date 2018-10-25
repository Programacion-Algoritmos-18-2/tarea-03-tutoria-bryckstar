# Se importan los metodos
from paquete1.Metodos import *

# Se agregan los docentes a los metodos
d = Docente("Docente B.D", "Loja")
d2 = Docente("Docente Pray", "Quito")
# Se crea la lista de los docentes
listado = [d, d2]
# Se agrega al estudiante por el metodo
e = Estudiante("Jose", listado)
# Se presentan los resultados
print(e.presentar_datos())
