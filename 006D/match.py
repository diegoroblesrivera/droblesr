# uso y ecplicacion de match
import random


def suma2(n1,n2,n3):
    print("El resultado de la suma es", n1+n2*n3)

def suma():
    n1=int(input("ingrese un numero:  "))
    n2=int(input("ingrese otro numero:  "))
    print("El resultado de la suma es", n1+n2)
def resta():
    n1=int(input("ingrese un numero:  "))
    n2=int(input("ingrese otro numero:  "))
    print("El resultado de la resta es", n1-n2)
def multi():
    n1=int(input("ingrese un numero:  "))
    n2=int(input("ingrese otro numero:  "))
    print("El resultado de la multiplicacion es", n1*n2)
def divi():
    n1=int(input("ingrese un numero:  "))
    n2=int(input("ingrese otro numero:  "))
    print("El resultado de la division es", n1/n2)

def calcu():
    while True:
        op=int(input('''Seleccione una opcion
                    1.- Suma
                    2.- Resta
                    3.- Multiplicacion
                    4.- Division
                    5.- Salir
                    '''))

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
                divi()
            case 5:
                print("Salir")
                break
            case _:
                print("Opcion invalida")

# calcu()

## nuevo menu recursivo
# debe tener 3 programas creados enteriormente
# el menu debe llamar a estos programas 
# y ejecutarlos de manera correcta
# debe tener la opcion de salir 
# y la opcion por defecto

def adivina_num():
    numeroAadivinar=random.randint(1,50)
    num=int(input("Adivine el número: "))

    while num!=numeroAadivinar:
        print(numeroAadivinar)
        if num>numeroAadivinar:
            print("El numero a adivinar es menor")
        else:
            print("El numero a adivinar es mayor")
        num=int(input("Adivine el número: "))
    print("Le achuntaste!") 

