import os

menu = [
    {"id": 1, "nombre": "arroz", "precio": 50},
    {"id": 2, "nombre": "habichuelas", "precio": 80},
    {"id": 3, "nombre": "aceite", "precio": 300},
    {"id": 4, "nombre": "pollo", "precio": 85},
    {"id": 5, "nombre": "lechuga", "precio": 80},
]

carrito = []


def ImprimirMenu(menu):
    TamMax = 0
    for item in menu:
        TamActual = (
            len(str(item["id"])) + len(item["nombre"]) + len(str(item["precio"]))
        ) > TamMax
        if TamActual > TamMax:
            TamMax = TamActual
    print("-" * (int(TamMax / 2 + 2)) + " Menu " + "-" * (int(TamMax / 2 + 2)))
    for item in menu:
        print(f"{item['id']}. {item['nombre']}. RD${item['precio']}")


def ImprimirFactura(carrito):
    tamid = 1
    tamnombre = 1
    tamprecio = 1
    tamcantidad = 1
    tamtotal = 1

    subtotal = 0

    for item in carrito:
        total_producto = item["precio"] * item["cantidad"]
        subtotal += total_producto
        tamidact = len(str(item["id"]))
        tamnombreact = len(str(item["nombre"]))
        tamprecioact = len(str(item["precio"]))
        tamcantidadact = len(str(item["cantidad"]))
        tamtotalact = len(str(total_producto))
        if tamidact > tamid:
            tamid = tamidact
        if tamnombreact > tamnombre:
            tamnombre = tamnombreact
        if tamprecioact > tamprecio:
            tamprecio = tamprecioact
        if tamcantidadact > tamcantidad:
            tamcantidad = tamcantidadact
        if tamtotal > tamcantidadact:
            tamtotalact = tamtotal
    if tamid - 2 < 0:
        tamid = 1
    else:
        tamid -= 2
    if tamnombre - 6 < 0:
        tamnombre = 1
    else:
        tamnombre -= 6
    if tamprecio - 6 < 0:
        tamprecio = 1
    else:
        tamprecio -= 6
    if tamcantidad - 2 < 0:
        tamcantidad = 1
    if tamtotal - 6 < 0:
        tamtotal = 1
    print(
        "\n"
        + "id"
        + "   " * (tamid)
        + "nombre"
        + " " * (tamnombre + 1)
        + "precio"
        + " " * (tamprecio)
        + "cantidad"
        + " " * (tamcantidad)
        + "total"
        + " " * (tamtotal)
    )
    print("-" * 50)
    for item in carrito:
        print(
            str(item["id"])
            + " " * (tamid + 4 - len(str(item["id"])))
            + item["nombre"]
            + " " * (tamnombre + 7 - len(item["nombre"]))
            + "RD$"
            + str(item["precio"])
            + " " * (tamprecio + 7 - len(str(item["precio"])))
            + str(item["cantidad"])
            + " " * (tamcantidad + 7 - len(str(item["cantidad"])))
            + "RD$"
            + str(item["precio"] * item["cantidad"])
            + " " * (tamtotal + 7 - len(str(item["precio"] * item["cantidad"])))
        )

    impuestos = subtotal * 0.18
    total = subtotal + impuestos
    print("-" * 50)
    print(f"Subtotal: RD${subtotal}")
    print(f"Impuestos (18%): RD${impuestos:.2f}")
    print(f"Total: RD${total:.2f}")


def agregarProducto(id_producto, cantidad):
    for item in menu:
        if item["id"] == id_producto:
            for producto in carrito:
                if producto["id"] == id_producto:
                    producto["cantidad"] += cantidad
                    return
            carrito.append(
                {
                    "id": item["id"],
                    "nombre": item["nombre"],
                    "precio": item["precio"],
                    "cantidad": cantidad,
                }
            )
            return
    print("ID de producto no válido.")


def main():
    while True:
        ImprimirMenu(menu)
        try:
            id_producto = int(input("Seleccione el ID del producto: "))
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
                continue
            agregarProducto(id_producto, cantidad)
            os.system("clear||cls")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            continue

        continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
        if continuar != "s":
            ImprimirFactura(carrito)
            break


if __name__ == "__main__":
    main()
