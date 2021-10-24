"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto Json.
"""

persona = {
    "nombre": "Faber",
    "apellidos": "Londono",
    "web": "faberlondonweb.co",
    "Teléfono": "123456789"
}

print(persona["web"])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Faber',
        'email': 'faberlondon@gmail.com',
        'Teléfono': '123456789'
    },
    {
        'nombre': 'Carolina',
        'email': 'carolondon@gmail.com',
        'Teléfono': '123456781'
    },
    {
        'nombre': 'Rebeca',
        'email': 'rebecalondon@gmail.com',
        'Teléfono': '123456782'
    }
]

contactos[0]['nombre'] = "Fabriño"
print(contactos[0]['nombre'])

print("\n Listado de contactos: ")
print("--------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("--------------------------------")

