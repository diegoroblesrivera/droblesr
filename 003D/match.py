# uso y explicacion de match
import random

def suma():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado de la suma es", n1+n2)
def resta():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado de la resta es", n1-n2)
def multi():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado de la suma es", n1*n2)
def division():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado de la division es", n1/n2)


def calcu():
    while True:
        op=int(input('''Ingrese una peracion
                    1.-Suma
                    2.-Resta
                    3.-Mutltiplicacion
                    4.-Division
                    5.-Salir
                    '''))
        match op:
            case 1:
                print("Suma")
                suma()
            case 2:
                print("Resta")
                resta()
            case 3:
                print("Mutltiplicacion")
                multi()
            case 4:
                print("Division")
                division()
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opcion INVALIDA")

# calcu()

def azarN():
    num=random.randint(1,5)
    return num
print(azarN()*10)
