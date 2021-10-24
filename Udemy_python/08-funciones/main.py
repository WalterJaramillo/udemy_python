"""
Funciones:
Una función es un conjunto de instrucciones agrupadas bajo un mismo 
nombre conreto que pueden reutilizarse invocando la función
tantas veces como sea necesario

def nombreDeMiFuncion(parametro):
    # BLOQUE CÓDIGO/ CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)

"""

# # Ejemplo No.1
# print("####### EJEMPLO 1 #######")
# print("\n")
# # Definir función
# def muestraNombre():
#     print("Faber")
#     print("Caro")
#     print("Esperanza")
#     print("Rebeca")
#     print("Mariana")
#     print("Gabriela")
#     print("\n")

# # Invocar a la función
# muestraNombre()
# muestraNombre()


# # Ejemplo No.2: parámetro
# print("####### EJEMPLO 2 #######")
# print("\n")
# def mostrarTuNombre(nombre, edad):
#     print(f"Tu nombre es: {nombre}")

#     if edad >= 18:
#         print("Eres mayor de edad")
            
# nombre = input("Introduce tu nombre: ")
# edad = int(input("Introduce tu edad: "))
# mostrarTuNombre(nombre, edad)


# # Ejemplo No.3
# print("####### EJEMPLO 3 #######")
# print("\n")

# def tabla(numero):
#     print(f"Tabla de multiplicar del número: {numero}")

#     for contador in range(11):
#         operacion = numero * contador
#         print(f"{numero} x {contador} = {operacion}")
    
#     print("\n")

# tabla(3)
# tabla(7)

# # Ejemplo No.3.1
# print("####### EJEMPLO 3 #######")
# print("\n")

# for numero_tabla in range(1, 11):
#     tabla(numero_tabla)


# # Ejemplo No.4
# print("####### EJEMPLO 4 #######")
# print("\n")

# # Parámetros opcionales

# def getEmpleado(nombre, dni = None):
#     print("EMPLEADO")
#     print(f"Nombre: {nombre}")

#     if dni != None:
#         print(f"DNI: {dni}")

# getEmpleado("Faber London" "1097390509")

# Ejemplo No.5. Parámetro opcionales y return o devolver datos
# print("####### EJEMPLO 5 #######")
# print("\n")

# def saludame(nombre):
#     saludo = f"Hola, Saludos! {nombre}"

#     return saludo

# print(saludame("Faber Londono"))

# # Ejemplo No.6. Parámetro opcionales y return o devolver datos
# print("\n####### EJEMPLO 6 #######")

# def calculadora(numero1, numero2, basicas = False):

#     suma = numero1 + numero2
#     resta = numero1 - numero2
#     multiplicacion = numero1 * numero2
#     division = numero1 / numero2

#     cadena = ""

#     if basicas != False:
#         cadena += "Suma: " + str(suma)
#         cadena += "\n"
#         cadena += "Resta: " + str(resta)
#         cadena += "\n"
#     else:
#         cadena += "Multiplicación: " + str(multiplicacion)
#         cadena += "\n"
#         cadena += "División: " + str(division)

#     return cadena

# print(calculadora(56, 5))

# # Ejemplo No.7. Funcion dentro de otra función
# print("\n####### EJEMPLO 7 #######")

# def getNombre(nombre):
#     texto = f"El nombre es: {nombre}"
#     return texto

# def getApellidos(apellidos):
#     texto = f"Los apellidos son: {apellidos}"
#     return texto

# def devuelveTodo(nombre, apellidos):
#     texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
#     return texto

# print(devuelveTodo("Faber", "Londono"))

# # Ejemplo No.8. Funciones Lambda
print("\n####### EJEMPLO 8 #######")

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year("2021"))



