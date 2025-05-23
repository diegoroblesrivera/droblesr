# crear menus con categorias
cantArt=0
total=0
while True:
    while True:
        try:
            print('''
                Seleccione una opcion
                1.-Teclados
                2.-Monitores
                3.-Audifonos
                4.-Pagar
                5.-Salir
                    ''')
            op=int(input())
            break
        except Exception:
            print("Ingrees solo numeros enteros")
    match op:
        case 1:
            while True:
                print('''
                    Seleccione una opcion
                    1.-Teclado de manco $20.000
                    2.-Teclado Gamer $40.000
                    3.-Tacladonormal y aburrido $8.000
                    4.-Volver al menu principal
                        ''')
                op=int(input())
                match op:
                    case 1:
                        total+=20000
                        cantArt+=1
                    case 2:
                        total+=40000
                        cantArt+=1
                    case 3:
                        total+=8000
                        cantArt+=1
                    case 4:
                        break
                    case _:
                        print("Opcion invalida")
                print(f"Articulo agregado al carro, lleva {cantArt} en total")
                print(f"El total parcial es ${total}")
        case 2:
            while True:
                print('''
                    Seleccione una opcion
                    1.-Monitor Xth67cv $200.000
                    2.-Monito3 Exa67jk92 $140.000
                    3.-Monitor VGA $28.000
                    4.-Volver al menu principal
                        ''')
                op=int(input())
                match op:
                    case 1:
                        total+=200000
                        cantArt+=1
                    case 2:
                        total+=140000
                        cantArt+=1
                    case 3:
                        total+=28000
                        cantArt+=1
                    case 4:
                        break
                    case _:
                        print("Opcion invalida")
                print(f"Articulo agregado al carro, lleva {cantArt} en total")
                print(f"El total parcial es ${total}")
        case 3:
            while True:
                print('''
                    Seleccione una opcion
                    1.-Audifono JBL 720 $60.000
                    2.-Audifono Gamer $140.000
                    3.-Audifono normal y aburrido $10.000
                    4.-Volver al menu principal
                        ''')
                op=int(input())
                match op:
                    case 1:
                        total+=60000
                        cantArt+=1
                    case 2:
                        total+=140000
                        cantArt+=1
                    case 3:
                        total+=10000
                        cantArt+=1
                    case 4:
                        break
                    case _:
                        print("Opcion invalida")
                print(f"Articulo agregado al carro, lleva {cantArt} en total")
                print(f"El total parcial es ${total}")
        case 4:
            print("-----------------0--------------------")
            print(f"El total de articulos es {cantArt}")
            print(f"El total  neto es {total}")
            print(f"El total mas IVA es {total*1.19}")
            print("-----------------0--------------------")
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Opcion invalida")

# Menu tarjeta credito

menu = """
--- Menú Principal ---
1. Pago de Tarjeta de Crédito
2. Simulación de Compras
3. Salir
"""

deuda = 100000  # Entero

while True:
    print(menu)
    try:
        opcion = int(input("Seleccione una opción: "))
        
        match opcion:
            case 1:
                print("\n--- Pago de Tarjeta de Crédito ---")
                try:
                    monto_pago = int(input("Ingrese el monto a pagar: $"))

                    if monto_pago <= 0:
                        print("Error: El monto debe ser mayor a cero.")
                    elif monto_pago > deuda:
                        print(f"Error: No puede pagar más que la deuda actual (${deuda}).")
                    else:
                        deuda -= monto_pago
                        print(f"Pago realizado. Deuda actual: ${deuda}")
                except ValueError:
                    print("Error: Ingrese un número entero válido.")

            case 2:
                print("\n--- Simulación de Compras ---")
                compras = []

                while True:
                    try:
                        monto = int(input("Ingrese el monto de la compra (0 para terminar): $"))
                        if monto < 0:
                            print("Error: El monto no puede ser negativo.")
                        elif monto == 0:
                            break
                        else:
                            
                            compras.append(monto)
                    except ValueError:
                        print("Error: Ingrese un número entero válido.")

                total = sum(compras)

                if total > deuda:
                    print(f"Error: El total de compras (${total}) excede el saldo disponible (${deuda}).")
                else:
                    deuda -= total
                    print(f"Compras simuladas exitosamente. Deuda actual: ${deuda}")

            case 3:
                print("Saliendo del programa...")
                break

            case _:
                print("Opción inválida. Intente de nuevo.")

    except ValueError:
        print("Error: Ingrese un número válido.")
