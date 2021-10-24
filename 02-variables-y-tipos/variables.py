"""
Una variable es un contenedor de información 
que guardará dentro un dato, se pueden crear
muchasa variables y que cada una tenga un dato distinto.
"""

#crar variables y asignarles un valor
texto = "Máster en Python"
texto2 = "Esto es de paciencia"
numero = 77
decimal = 7.5

#mostrar variable
print(texto)
print(texto2)
print(numero)

#concatenación
nombre = "Faber"
apellidos = "Londoño"
web = "faberlondon.io"

#forma dummy de escribir código en Py
print(nombre + " " + apellidos + " - " + web)

#mejor así:
print(f"{nombre} {apellidos} - {web}")

#otra forma:
print("Hola mi nombre es {} {} y te invito a ver mi sitio {}".format(nombre, apellidos, web))