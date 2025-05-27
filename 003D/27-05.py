# menus de la tarjeta de credito
import os
while True:
    while True:
        try:
            op=int(input('''
                    Seleccione una opcion
                    1.-
                    2.-
                    3.-
                    '''))
            break
        except Exception:
            print("Solo numeros enteros")
    
    match op:
        case 1:
            os.system("cls")
            print("1")
        case 2:
            print("2")
        case 3:
            print("Saliendo...")
            break
        case _:
            print("Opcion invalida")