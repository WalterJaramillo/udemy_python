"""
# Operadores lógicos
and = Y
or = O
! = negación
not = NO

"""

print("\n############### OPERADORES COMPARACIÓN ###################")

pais = "Colombia"

if pais == "México" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla Hispana :D")
else:
    print(f"{pais} no es un pais de habla Hispana :/")



print("\n############### OPERADORES COMPARACIÓN 2 ###################")

pais = "Colombia"

if not (pais == "México" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO un pais de habla Hispana :/")
else:
    print(f"{pais} SI es un pais de habla Hispana :D")


print("\n############### OPERADORES COMPARACIÓN 3 ###################")

pais = "USA"

if pais != "México" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO un pais de habla Hispana :/")
else:
    print(f"{pais} SI es un pais de habla Hispana :D")