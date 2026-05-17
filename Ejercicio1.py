# Solicitar etiqueta al usuario
etiqueta = input("Ingrese la etiqueta de rastreo (formato AÑO-CATEGORÍA-PAÍS): ")

# Validación de seguridad: entrada vacía o None
if not etiqueta:
    print("Error: La etiqueta de rastreo no puede estar vacía.")
else:
    # Extraer categoría con slicing puro usando find() para ubicar los guiones
    guion1 = etiqueta.find("-")
    guion2 = etiqueta.find("-", guion1 + 1)
    categoria = etiqueta[guion1 + 1:guion2]
    print(f"Categoría: {categoria}")

    # Operador ternario: Ruta Local si termina en SV, sino Ruta Internacional
    ruta = "Ruta Local" if etiqueta[-2:] == "SV" else "Ruta Internacional"
    print(ruta)
    