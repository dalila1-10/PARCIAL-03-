lecturas = []

# Solicitar 5 lecturas
for i in range(5):
    temp = int(input(f"Ingrese la lectura {i+1}: "))
    lecturas.append(temp)

# Evaluar cada lectura con match-case
for temp in lecturas:
    match temp:
        case 0:
            print("Alerta: Punto de Congelación")
        case 100:
            print("Alerta: Punto de Ebullición")
        case _:
            print("Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico")


        