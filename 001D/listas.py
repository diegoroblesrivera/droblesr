#uso y ejemplos de listas

#        -6-5 -4 -3 -2 -1  
numeros=[2,5, 8, 77, 6, 7.9]
#        0 1  2   3  4  5 


# print(round(numeros[5]))

# for numero in numeros:
#     print("Numero x 2", numero*2)

pnombres=["Felipe", "Curly", "Larry", "Moe"]

# print(nombres)

# nombres.append("Luthien")

# print(nombres)
n=["Christopher", "Edward", "John","Hanz"]
a=["Nolan", "Norton", "Williams", "Zimmer"]

# c=0
# for i in a:
#     print(n[c], a[c])
#     c+=1


# nombres=[]
# appellidos=[]
# while True:
#     print('''
#         1.- Ingresar Nombre
#         2.- Mostar nombres y apellidos
#         3.- Buscar Nombre
#         4.-Salir
#           ''')
#     op=int(input())

#     match op:
#         case 1:
#             nom=input("Ingrese su nombre: ")
#             nombres.append(nom)
#             ape=input("Ingrese su apellido: ")
#             appellidos.append(ape)
#         case 2:
#             c=0
#             for i in nombres:
#                 print(nombres[c], appellidos[c])
#                 c+=1
#         case 3:
#             busca=input("Indiuqe que nombre buscará: ")
#             if busca in nombres:
#                 print(f"El nombre {busca} está en la lista")
#             else:
#                 print(f"El nombre {busca} NO está en la lista")

#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("Opcion invalida")



'''
Selecciones una opcion
1.- Agregar Productos (nombre producto y precio)
2.- Comprar (submenu mostrando productos y precios)
3.- Crear Boleta
4.- Salir
'''
productos=["disco SSD", "memoria Ram"]
precios=[70000, 30000]
carrito=[]
while True:
    print('''
        1.- Agregar Productos
        2.- Comprar
        3.- Crear Boleta
        4.-Salir
          ''')
    op=int(input())

    match op:
        case 1:
            nom=input("Ingrese el producto: ")
            productos.append(nom)
            ape=input("Ingrese precio: ")
            precios.append(ape)
        case 2:
            c=0
            for i in productos:
                print(c+1, ".- ", productos[c], precios[c])
                c+=1
            op=int(input())
            carrito.append(op-1)
            print("LOS PRUDUCTOS QUE LLEVA SON")
            for i in carrito:
                print(productos[i])
        case 3:
            busca=input("Indiuqe que nombre buscará: ")
            if busca in productos:
                print(f"El nombre {busca} está en la lista")
            else:
                print(f"El nombre {busca} NO está en la lista")

        case 4:
            print("Saliendo")
            break
        case _:
            print("Opcion invalida")

