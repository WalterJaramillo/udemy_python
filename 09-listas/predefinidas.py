cantantes = ['Rebeca', 'Esperanza', 'Carolina']
numeros =[1, 2, 5, 7, 10, 8]

# Ordenas una lista
numeros.sort()
#print(numeros)

# Añadir elementos
cantantes.append("Mariana")
cantantes.insert(1, "Faber")
#print(cantantes)

# Eliminar elementos de una lista
cantantes.pop(1)
cantantes.remove('Mariana')
#print(cantantes)

# Dar la vuelta
#print(numeros)
numeros.reverse()
#print(numeros)

# Buscar dentro de una lista
print('Rebeca' in cantantes)

# Contar elementos
print(len(cantantes))

# cuantas veces aparece un elemento en lista
numeros.append(8)
print(numeros.count(8))

# Conseguir índice
print(cantantes.index("Esperanza"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)

