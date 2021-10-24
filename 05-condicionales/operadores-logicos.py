"""
# Operadores lógicos
and = Y
or = O
! = negación
not = NO

"""

print("\n############### OPERADORES LÓGICOS ###################")

edad_min = 18
edad_max = 65
edad_oficial = int(input(f"¿Tienes la edad suficiente para trabajar?, introduce tu edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Estás en edad de trabajar")
else:
    print("No estás10 en edad de trabajar")