"""
Ejercicio No.8. ¿Cuánto es el X % de X #?
                                20% de 150
"""

numero =int(input("Introduce el numero: "))
porcentaje = int(input(f"Qué porcentaje quieres sacar de {numero}?: "))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje} % de {numero} es: {operacion}")
