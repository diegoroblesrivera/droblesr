palos=0
diamantes=0
espadas=0
carbón=0
import random, time


while True:
    while True:
        try:
            op=int(input('''Qué hará Steve: 
                        1.- Minar
                        2.- Ver invanterio
                        3.- Craftear espadas
                        4.- Salir
                        '''))
            break
        except Exception:
            print("Debe ingresar solo números enteros")
    match op:
        case 1:
            print("Minar")
            while True:
                    while True:
                        try:
                            op_lav=int(input('''¿Qué busacará Steve?
                                            1.- Palos
                                            2.- Diamantes
                                            3.- Salir
                                            '''))
                            break
                        except Exception:
                            print("Debe ingresar solo números enteros")
                    match op_lav:
                        case 1:
                            print("Steve busacara palos en los bloques de hojas de los árboles")
                            prob_palos=random.randint(1,3)
                            time.sleep(3)
                            if prob_palos==1:
                                print("Steve encontró un palo")
                                palos+=1
                            else:
                                print("No dropeó ningún palo")
                        case 2:
                            print("Steve irá a la mina a buscar diamantes")
                            prob_diaman=random.randint(1,7)
                            time.sleep(3)
                            if prob_diaman==1:
                                print("Steve encontró diamantes")
                                diamantes+=1
                            elif prob_diaman>=2 and prob_diaman<=4:
                                print("Steve encontró carbón")
                                carbón+=1
                            else:
                                print("Steve no encontró nada")
                        case 3:
                            print("Volviendo a la base")
                            break
                        case _:
                            print("Steve se bugueó, haz otra cosa")
        case 2:
            print("Viendo inventario")
            print(f"Steve tiene {diamantes} diamantes, {palos} palos y {carbón} de carbón.")
            print(f"Steve tiene {espadas} espadas.")
        case 3:
            print("Crafteo de espadas")
            while diamantes>=2 and palos>=1:
                if diamantes>=2:
                    if palos>=1:
                        print("Crafteando espada")
                        palos-=1
                        diamantes-=2
                        espadas+=1
                        time.sleep(1)
                        if diamantes>=2 and palos>=1:
                            print("Steve puede craftear otra espada")
                    else:
                        print("A Steve le faltan palos para craftear la espada")
                        print(f"Steve tiene {palos} palos")
                else:
                    print("A Steve le faltan diamantes para craftear la espada")
                    print(f"Steve tiene {diamantes} diamantes")
            if diamantes<2 and palos<1:
                print("A Steve le faltan recursos")
                print(f"Tiene {diamantes} diamantes y {palos} palos")
        case 4:
            print("Saliendo del programa")
            break
        case _:
            print("Steve se bugueó, haz otra cosa")