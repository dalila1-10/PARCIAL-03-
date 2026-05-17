nombre = input("Ingrese su nombre completo (Nombre Apellido): ")

# Convertir a lista y luego invertir con slicing
lista = nombre.split()
invertida = lista[::-1]

# Bucle anidado para formatear con puntos
for palabra in invertida:
    for letra in palabra:
        print(letra, end=".")
    print()

    