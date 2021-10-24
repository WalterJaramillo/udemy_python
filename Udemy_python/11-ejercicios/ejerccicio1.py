"""
Ejercicio No.1. Hacer un programa que tenga una lista de 8 números
enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer función que recorra listas de números y devuelva un string
- Ordenar la lista y mostrarla
- Mostrar su longitud
- Buscar algún elemento (que el usuario pida por teclado)
"""

# 1. Crear la lista numerica
numeros = [1, 50, 63, 91, 87, 14, 16, 21, 9]

# Crear función que recorra listas de números y devuelva un string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    
    return resultado

# 2. Recorrer y mostrar
print("########### Recorrer y mostrar ###########")

# for numero in numeros:
#     print(numero)

print(mostrarLista(numeros))

# Ordenar y mostrar
print("########### Ordenar y mostrar ###########")
numeros.sort()
print(mostrarLista(numeros))

# Mostrar longitud
print("########### Mostrar longitud ###########")
print(len(numeros))

# Buscar elemento (que el usuario pida por teclado)
print("########### Buscar elemento que el usuario pida por teclado ###########")

busqueda = int(input("Introduce el número que quieras buscar: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el número que quieras buscar: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"##### Buscar en la lista el número {busqueda} #####")

search = numeros.index(busqueda)
print(f"El numero buscado existe en la lista, es el índice: {search}")
