import random

palito = 0
piedra = 0
diamantes = 0
espada= 0

while True:
    op = int(input('''Que desea hacer:
                    1.- Minar
                    2.- Consultar recursos
                    3.- Crear espada
                    4.- Salir
                    '''))
    match op:
        case 1:
            print("Comenzando a minar...")
            min = random.randint(1, 4)
            if min <= 2:
                piedra += 1
                print("Has minado 1 piedra.")
            elif min == 3:
                palito += 1
                print("Has minado 1 palito.")
            else:
                diamantes += 1
                print("Has minado 1 diamante!!")   
        case 2:
            print("Consultando recursos...")
            print(f"Piedra: {piedra}")
            print(f"Palitos: {palito}")
            print(f"Diamantes: {diamantes}")
        case 3:
            print("Creando espadas...")
            while diamantes >= 2 and palito >= 1:
                diamantes -= 2
                palito -= 1
                print("¡Has creado una espada de diamantes!")
                espada+=1
                print(f"Tienes {espada} espadas de diamantes")
            else:
                print("No te quedan suficientes recursos para crear una espada. Necesitas mas diamantes y palitos.") 
        case 4:
            print("Saliendo del juego...")
            break
        case _:
            print("Opción no válida, por favor elige una opción correcta.")
