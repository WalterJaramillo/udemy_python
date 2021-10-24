# condicionales = estructura de control, dependiendo de la entrada de datos y ejecutar. 
"""
# Condicional IF

SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
esle:
    otras instrucciones

# operadores de comparación
== igual
!= diferente
< menor que
< mayor que
<= menor o igual que
>= mayor o igual que

"""

# Ejemplo 1
print("############### EJEMPLO 1 ###################")

color = "verde"
#color = input(f"¿Adivina cuál es mi color favorito?: ")

if color == "azul":
    print("¡Excelente!")
    print("Si, mi color favorito es azul")
else:
    print("Vaya!, sigue intentandolo")
    print("El color es incorrecto")

# Ejemplo 2
print("\n############### EJEMPLO 2 ###################")

year = 2020
#year = int(input("¿En que año estamos?: "))

if year >= 2021:
    print("¡Parece que estás perdido en el espacio!")
else:
    print("Es un año anterior a 2021")

# if anidado
# Ejemplo 3
print("\n############### EJEMPLO 3 ###################")

nombre = (input(f"¿Cómo te llamas?: "))
ciudad = "Bogotá"
continente = "América"
edad = int(input("¿Qué edad tienes?: "))
may_edad = 18


if edad >= may_edad:
    print(f"{nombre} si es mayor de edad")

    if continente != "América":
        print("El usuario NO es Américano")
    else:
        print(f"El usuario es Américano proveniente de {ciudad}")

else:
    print(f"{nombre} No es mayor de edad todavía")








    

