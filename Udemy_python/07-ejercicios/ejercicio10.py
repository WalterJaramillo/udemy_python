"""
Ejercicio No.10. El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuantos alumnos han aprobado y cuantos han suspendido.
"""

contador = 1
aprobados = 0
reprobados = 0

numero_alumnos = int(input("Cuántos alumnos tienes a cargo?: "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Cuál es la calificación del \"alumno {contador}\"?"))

    if nota >= 5:
        aprobados +=1
    else:
        reprobados += 1

    contador += 1

print(f"Número de Alumnos aprobados: {aprobados}")
print(f"Número de Alumnos reprobados: {reprobados}")
