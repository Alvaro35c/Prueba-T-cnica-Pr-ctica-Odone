
Diccionario1 = {
                    "Nombre":"Andres",
                    "Edad":32,
                    "Ciudad":"Cali"
                }


try:
    print(Diccionario1.get["Pais"])
except TypeError:
    print("No se encuentra la clave")

""" Para el control de errores se puede utilizar Try except.
En el bloque Try se escribe el codigo que puede generar un error 
si no se ejecuta de forma esperada, Cuando se genera el error se
ejecuta el codigo en el bloque Except. """