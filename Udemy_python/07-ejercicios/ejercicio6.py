"""
Ejercicio No.6: Hacer un programa Mostrar todas las tablas de multiplicar
del 1 al 10. Mostrando el título de la tabla y luego las multiplicaciones.
"""

for cabecera in range(10, 21):
    print("#########################")
    print(f"###### TABLA DEL {cabecera} ######")
    print("#########################")

    for numero in range(10, 21):
        print(f"{numero} x {cabecera} = {numero*cabecera}")
    
    print("\n")