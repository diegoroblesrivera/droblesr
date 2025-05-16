#use y explicacion de while
# num=0

# while num<=5:
#     print(num)
#     num+=1


# import time
# num= 10

# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

# resp="no"

# while resp!="si":
#     resp=input("Desea Salir del sistema? :")

# clave=3344
# intentos=3
# contraseña=int(input("Ingrese su contraseña"))

# while clave!=contraseña :
#     intentos-=1
#     print("Quedan ", intentos, " intentos")
#     print("ERROR; clave invalida")
#     contraseña=int(input("Ingrese su contraseña"))
#     if intentos==1:
#         break


# if clave==contraseña:
#     print(" Clave aceptada")
# else:
#     print("Sistema bloqueado")



# pida al usuaruio una palbra y cuentes sus caracteres

# palabra=input("ingrese una plabra ")



# # caract=0
# # for i in palabra:
# #     print(i)
# #     # caract=caract+1
# #     caract+=1
# print("La cant de caracteres es" , len(palabra))


# pida al usuario numero infinitamente y 
# muestre si son par o impar
# para salir, ponga 0 (cero).
# num=5

# while num!=0:
#     num=int(input("Ingrese un numero( cero para salir)"))
#     if num % 2==0:
#         print(f"El numero {num} es par")
#     else:
#         print(f"El numero {num} es impar")

# ingresar numeros hasta que ponga el cero
# mostrar las suma de todos los numeros 
# pares e impares ingresados

# print("/"*100)

import random
# randy=random.randint(1,10)
# print(randy)
# STREET FIGTHER

# designe 2 peleadores cada uno con 50 HP
# peleas por turnos, casa uno acata entre 2 y 10
# gana quien quita todo el HP al contrincante

# Categorizar jugadores 
# En una liga amateour, se paga a lo jugadores de futbol
# Cuando anota mas goles recibe nu bono en su paga
# Entre 1-3 goles, 4%; entre 4-6 goles 6%, 7 goles o mas 8%
# Si su equipo queda entre los 3 primeros, +3000 
# Si su equipo queda entre 4-8, +2000 
# Si su equipo queda entre 9 y mas, +1000 
# El pago base por 


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


