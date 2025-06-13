# uso y ejemplo de listas

#        -5 -4 -3  -2  -1
numeros=[10, 5, 9 , 34, 20]
#         0  1  2   3   4

# print(numeros[-1])
# numeros.reverse()
# for numero in numeros:
#     print("numero" ,numero*3)
# numeros.append(64)
# print(numeros)

# frutas=["Durazno", "Naranja", "Manzana", "Pera"]

# for fruta in frutas:
#     print(fruta)

# nombres=["Steven","George"]
# appellidos=["Spilvergo", "Lucrecia"]
#  while True:
#     print('''
#         1.- Ingresa un nombre y apellido
#         2.- Buscar Nombre
#         3.- Mostrar nombres y apellidos
#         4.- Salir
#           ''')
#     op=int(input("seleccione una opcion"))
#     match op:
#         case 1:
#             persona=input("Ingrese un nombre")
#             nombres.append(persona)
#             ape=input("Ingrese un apellido")
#             appellidos.append(ape)
#             print(nombres)
#             print(len(nombres))
#         case 2:
#             n=input("ingrese nombre a buscar")
#             if n in nombres:
#                 print(f"El nombre {n} Existe")
#             else:    
#                 print(f"El nombre {n} NO Existe")
#         case 3:
#             # c=0
#             # for karina in nombres:
#             #     print(nombres[c], appellidos[c])
#             #     c+=1
#             for i in range(len(nombres)):
#                 print(nombres[i], appellidos[i])
#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("Opcion invalida")

'''
Selecciones una opcion
1.- Agregar Productos (nombre del producto y precio)
2.- Comprar (submenu mostrando productos y precios)
3.- Crear Boleta
4.- Salir
productos=[]
precios=[]
carrito[]


'''
# def suma():
#     return 2+6



# for i in range(numeros[-1]):
#     print(i)

# print(numeros[0])

productos=["Shampoo","Jabon","Galleta"]
#               0       1       2
# len(productos)

# for producto in productos:
#     print(producto)

precios=[3500, 2000, 4000]
carrito=[]

# while True:
#     while True:
#         try:
#             print('''
#             1.- Agregar Productos (nombre del producto y precio)
#             2.- Comprar (submenu mostrando productos y precios)
#             3.- Crear Boleta
#             4.- Salir
#             ''')
#             op=int(input("Seleccione una opcion: "))
#             break
#         except Exception:
#             print("Solo numeros enteros")
#     match op:
#         case 1:
#             prod=input("Ingrese un producto: ")
#             productos.append(prod)
#             pre=int(input("Ingrese el precio: "))
#             precios.append(pre)
#         case 2:
#                 for i in range(len(productos)):
#                     print(i+1,productos[i], "$", precios[i])
#                 producto=int(input("Seleccione una opcion: "))  
#                 carrito.append(producto-1)
#                 print(carrito)
#         case 3: 
#             total=0
#             print("-----------------0-----------------")
#             print("Articulos de limpieza Pola")
#             for i in carrito:
#                 print(productos[i], "-----$", precios[i])
#                 total=total+precios[i]
#             print("La cant de articulos que lleva es " , len(carrito))
#             print("El total neto es ", total)
#             print("El total mas IVA es ", total*1.19)
#             print("-----------------0-----------------")
#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("Opcion invalida")




'''
Tarea
Crear programa de manejo de notas
1.- Ingresar nota
2.- Borrar nota
3.- Mostar notas
4.- Sacar promedio, nota mayor y nota menor
5.- Limpiar todas las notas
6.- Salir
'''

lista=[
    [3,4],
    [9,8]


]

print(lista[1][0])


