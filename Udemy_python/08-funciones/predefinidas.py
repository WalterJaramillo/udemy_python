nombre = "Faber Londono"

# Funciones generales
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre, int)
if comprobar:
    print("Esa variable es un string")
else:
    print("Esa variable NO es un string")

if not isinstance(nombre, float):
    print("La variable no es un número con decimales")

# Limpiar espacios de un string
frase = "         mi cadena de palabras     "
print(frase)
print(frase.strip())

# Eliminar variables
year = 2021
print(year)
del year
#print(year)

# Comprobar variable vacía
texto = "   FF   "

if len(texto) <= 0:
    print("La variable está vacía")
else:
    print("La variable tiene contenido: ", len(texto))

# Encontrar carácteres dentro de un string
frase = "La vida es bella"
print(frase.find("vida"))

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "FE") 
nueva_frase2 = frase.replace("bella", "preciosa")
print(nueva_frase)

# Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())
