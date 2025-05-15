# uso y explicacion de match

def suma():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("EL resultado de la suma es", n1+n2)
def resta():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("EL resultado de la resta es", n1-n2)
def multi():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("EL resultado de la multiplicacion es", n1*n2)
def division(): 
    try:
        n1=int(input("Ingrese un numero: "))
        n2=int(input("Ingrese otro numero: "))
        print("EL resultado de la resdivisionta es", n1/n2)
    except ZeroDivisionError as nombre_de_excepcion:
        # Código para manejar la excepción
        print(f"Se produjo una excepción: {nombre_de_excepcion}")



while True:
    print('''
        1.- Suma
        2.- Resta
        3.- Multiplicacion
        4.- Division
        5.-Salir
        ''')
    op=int(input("Seleccione un a opcion"))

    match op:
        case 1:
            print("Suma")
            suma()
        case 2:
            print("Resta")
            resta()
        case 3:
            print("Multiplicacion")
            multi()
        case 4:
            print("Division")
            division()
        case 5:
            print("Saliendo")
            break
        case _:
            print("Opcion no valida")

