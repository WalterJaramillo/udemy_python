# Elif
# Ejemplo 
print("\n############### EJEMPLO 4 ###################")
"""
dia = int(input("Introduce el número del día de la semana: "))

if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miércoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana!!!")

"""
# elif es lo que en otros lenguajes se conoce como 'elseif'
# Esta es una mejor práctica de escribir código en Python

dia = int(input("Introduce el número del día de la semana: "))

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miércoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana!!!")

