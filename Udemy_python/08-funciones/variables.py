"""
Variables locales: Se definen dentro de la función y no 
se puede usar fuera de ella, solo están disponibles dentro.
A no ser que hagamos un return.

Variables Globales: Son las que se declaran fuera de una función
y están disponibles dentro y fuera de ellas.
"""

# Variable global

frase = "Jesucristo es el mismo ayer, y hoy, y por los siglos"

print(frase)

def holaMundo():
    frase = "Hola Mundo!!!"
    print("DENTRO de la función: ")
    print(frase)

    year = 2021
    print(year)

    global website
    website = "faberlondonweb.co"
    print("DENTRO: ", website)


    return "Dato devuelto: " + str(year)

print(holaMundo())
print("FUERA: ", website)