# uso y explicacion de match
import random

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


def calcu():

    while True:
            try:
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
            except ValueError as errorr:
                print("Debe ingreser un numero entero")
                print(f"Error: {errorr}")

# calcu()5


## nuevo menu recursivo
# debe tener 3 programas creados enteriormente
# Los programas deben estar en una funcion
# el menu debe llamar a estos programas 
# y ejecutarlos de manera correcta
# debe tener la opcion de salir 
# y la opcion por defecto



def clave_inf():
    #Clave con intentos infinitos
    clave=3344
    password=int(input("Ingrese su pass :"))
    while clave!=password:
        print ("ERORR, clave invalida")
        password=int(input("Ingrese su pass :"))

    print("Bienvenido al sistema")

def azar():
    
    numeroAadivinar=random.randint(1,50)

    num=int(input("Adivine el número"))

    while num!=numeroAadivinar:
        print(numeroAadivinar)
        if num>numeroAadivinar:
            print("El numero a adivinar es menor")
        else:
            print("El numero a adivinar es mayor")
        num=int(input("Adivine el número"))
    print("Le achuntaste!") 

def ruleta():
    # # Ruleta rusa

    barril=random.randint(1,6)
    rul=int(input("Dispare : "))

    while rul!=barril:
        rul=int(input("Dispare"))
    print("BANG!!!")
    

def menu_nuevo():
    while True:
        op=int(input('''
                Seleccione una opcion
                1.-Clave con intentos infinitos
                2.- NUmero al azar
                3.-Ruleta Rusa
                4.-Salir
                '''))   
        match op:
            case 1:
                clave_inf()
            case 2:
                azar()
            case 3:
                ruleta()
            case 4:
                break
            case _:
                print("Opcion no valida")

# '''
# Crear un menu de carrito con las siguientes opciones
# 1.-Ingresar nombre del usuario
# Sera mostrado en la boleta, con un saludo
# 2.- Comprar, poner productos para poder comprar
# con su precio correspondiente
# 3.- Sacar boleta, calcular el precio neto
# y el precio mas IVA. Mostrar totales
# bonus contar la cantidad de articulos
# 4.- Salir 
# Consideraciones:
# Por lo menos 3 productos disponibles
# No hay limite de compra
# Se puede salir en cualquier momento
# Los montos de los productos son fijos
# Mostrar tb el total de articulos.
# '''
import os
total=0
carrito=0
while True:
    print('''Seleccione una opcion
        1.-Ingresar Nombre
        2.-Comprar
        3.-Mostrar boleta
        4.-Salir
        ''')

    op=int(input())
    os.system('cls')
    match op:
        case 1:
            nombre=input("ingres su nombre: ")
        case 2:
            while True:
                print('''
                1.- Manzana $1200
                2.- Pera $1400
                3.- Platano $1000
                4.- Volver al menu principal
                ''')
                opc=int(input())
                match opc:
                    case 1:
                       total+=1200
                    case 2:
                       total+=1400
                    case 3:
                       total+=1000
                    case 4:
                        break
                    case _:
                        print("Producto no valido")
                print("Su total parcial es ", total)
                carrito+=1        
        case 3:
            print(f'''
                ----------------0-----------------  
                EL TOTAL DE ARTICULOS ES {carrito}
                Su total neto es {total}
                Su total mas IVA es {total*1.19}
                Gracias {nombre} por venir
                Vuelva Pronto
                ----------------0-----------------  
                  ''')
        case 4:
            break
        case _:
            print("opcion invalida")
