"""
SET es un tipo de dato, para tener una colección de valores,
pero no tiene ni índice ni un orden.
"""

personas = {
    "Esperanza",
    "Rebeca",
    "Carolina",
    "Faber",
    "Victoria",
    "Paco"
}

personas.add("Sofia")
personas.remove("Paco")

print(type(personas))
print(personas)
