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
        try:
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
        except Exception:
            print("Solo numeros enteros son permitidos")

## nuevo menu recursivo.debe tener
#  3 programas creados enteriormente
# el menú debe llamar a estos programas 
# y ejecutarlos de manera correcta
# debe tener la opcion de salir 
# y la opcion por defecto


# while True:
#     try:
#         num=int(input("Ingrese un numero mayor que 3: "))
#         if num>3:
#             break
#     except Exception:
#         print("Solo debe ingreser numero, no texto")

# '''
# Crear un menu de carrito con las siguientes opciones
# 1.-Ingresar nombre del usuario
# Sera mostrado en la boleta, con un saludo
# 2.- Comprar, poner productos para poder comprar
# con su precio correspondiente
# 3.- Generar boleta, calcular el precio neto
# y el precio mas IVA. Mostrar totales
# 4.- Salir 
# Consideraciones:
# Por lo menos 3 productos
# No hay limite de compra
# Se puede salir en cualquier momento
# Los montos de los productos son fijos
# Mostrar tb el total de articulos.
# '''

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
                       carrito+=1 
                    case 2:
                       total+=1400
                       carrito+=1 
                    case 3:
                       total+=1000
                       carrito+=1 
                    case 4:
                        break
                    case _:
                        print("Producto no valido")
                print("Su total parcial es ", total)
                       
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
            print("Opcion invalida")
