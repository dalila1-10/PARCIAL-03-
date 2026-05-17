from decimal import Decimal

total = Decimal("0")

while True:
    try:
        precio = Decimal(input("Ingrese el precio: "))
        if precio == 0:
            break
        total += precio
    except:
        print("Error: Ingrese solo números.")

print(f"Total a pagar: {total}")

