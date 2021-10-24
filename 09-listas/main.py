"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un único nombre
Para acceder a esos valores podemos usar un índice númerico.
"""

# pelicula = "Batman"

# # Definir una lista (array)
# peliculas = ["Star Wars", "Avengers", "X-Men", "Han Solo"]
# cantantes = list(('Cantante 1', 'Cantante 2', 'Cantante 3'))
# years = list(range(2020, 2050))
# variada = ["Faber", 30, 50, True, "Texto"]


# # print(peliculas)
# # print(cantantes)
# # print(years)
# # print(variada)



# # Índices
# pelicula = "otro nombre"
# peliculas[1] = "Elisium"
# print(peliculas)

# print(peliculas[0])
# print(cantantes[0:])

# # Añadir elementos a lista
# cantantes.append("Cantante 4")
# cantantes.append("Cantante 5")
# print(cantantes)

# # Recorrer lista


# nueva_pelicula = ""
# while nueva_pelicula != "stop":
#     nueva_pelicula = input("Introduce la nueva pelicula: ")

#     if nueva_pelicula != "stop":
#         peliculas.append(nueva_pelicula)

# print("*******LISTADO PELICULAS*******")
# for pelicula in peliculas:
#     print(f"{peliculas.index(pelicula)+1}. {pelicula}")

# Listas multidimensionales
print("\n********** LISTA DE CONTACTOS ************")

contactos = [
    [
        'Rebeca',
        'rebeca@mail.com'
    ],
    [
        'Esperanza',
        'esperanza@mail.com'
    ],
    [
        'Carolina',
        'carolinalondono.lara@gmail.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")

print(contactos[2])