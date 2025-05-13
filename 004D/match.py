# explicacion y uso de match

def suma():
    n1=int(input("Ingrese un numero:  "))
    n2=int(input("Ingrese otro numero:  "))
    print("El resultado de la suma es", n1+n2)
def resta():
    n1=int(input("Ingrese un numero:  "))
    n2=int(input("Ingrese otro numero:  "))
    print("El resultado de la resta es", n1-n2)
def multi():
    n1=int(input("Ingrese un numero:  "))
    n2=int(input("Ingrese otro numero:  "))
    print("El resultado de la multiplicacion es", n1*n2)
def division():
    try:
        n1=int(input("Ingrese un numero:  "))
        n2=int(input("Ingrese otro numero:  "))
        print("El resultado de la division es", n1/n2)
    except ZeroDivisionError as nombre_de_excepcion:
        # Código para manejar la excepción
        print(f"Se produjo una excepción: {nombre_de_excepcion}")



def calcu():
    while True:
        op=int(input('''Seleccione su opcion
                    1.- Suma
                    2.- Resta
                    3.- Multi
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
                print("Multi")
                multi()
            case 4:
                print("Division")
                division()
            case 5:
                print("Saliendo")
                break
            case _:
                print("Opcion Invalida")

calcu()




## nuevo menu recursivo.debe tener
#  3 programas creados enteriormente
# el menú debe llamar a estos programas 
# y ejecutarlos de manera correcta
# debe tener la opcion de salir 
# y la opcion por defecto