# solucion Evalucion formativa experioencia 2
total=0

while True:
   op=int(input('''
            Seleccione una comida
            1. Pikachu Roll $4500
            2. Otaku Roll $5000
            3. Pulpo Venenoso Roll $5200
            4. Anguila Eléctrica Roll $4800
            5.-Pagar y salir
            '''))
   match op:
      case 1:
         total+=4500
      case 2:
         total+=5000
      case 3:
         total+=5200
      case 4:
         total+=4800
      case 5:
        print("tiene codigo de descuento? 1.- si, 2.- no")
        desc=int(input())
        if desc==1:
            while True:
                cod=input("ingres su codigo de desc")
                if cod =="soyotaku":
                    desc10=total*0.1
                    total=total-desc10
                    print("El Descuento es $",desc10)
                    break
                else:
                   print("Codigo caducado o no valido")
                   nu=input("Dese intentar nuevamente?1.- si, 2.- no")
                   if nu!="1":
                      break
        print(" EL total es $", total)
        break
      case _:
         print("Opcion invalida")
   print(f"su total parcial es {total}")


# solucion a la actividad 2.5.3

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
                            total+=monto
                    except ValueError:
                        print("Error: Ingrese un número entero válido.")

                

                if total > deuda:
                    print(f"Error: El total de compras (${total}) excede el saldo disponible (${deuda}).")
                else:
                    deuda += total
                    print(f"Compras simuladas exitosamente. Deuda actual: ${deuda}")

            case 3:
                print("Saliendo del programa...")
                break

            case _:
                print("Opción inválida. Intente de nuevo.")

    except ValueError:
        print("Error: Ingrese un número válido.")