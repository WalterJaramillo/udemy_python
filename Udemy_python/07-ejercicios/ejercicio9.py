"""
Ejercicio No.9. Hacer un programa que pida numeros al usuario
indefinidamente hasta introducir el número 111
"""

contador = 1
while contador < 100:
    numero = int(input("Introduce un numero: "))

    if numero == 111:
        break
    else:
        print=(f"Has introducido el : {numero}")