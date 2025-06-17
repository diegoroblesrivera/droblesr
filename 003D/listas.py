# uso y ejemplos de listas
# que es una lista? 
# es una coleccion de datos

#       -6 -5 -4 -3  -2   -1
numeros=[3, 6, 2, 88, 9]
#        0  1  2  3   4   5

# print(numeros)
# numeros.sort()

# print(numeros)
# numeros.reverse()
# print(numeros)


# print(numeros[4])

# print(numeros.insert(3,1000))
# print(numeros)
# numeros.remove(88)
# print(numeros)
# numeros.sort()
# print(numeros)

# numeros.append(64)
# marcas=["Nike", "Capcom", "Nintendu", "Konami"]

# for marca in marcas:
#     print(marca)

# print(numeros)

# for numero in numeros:
#     print("nota:" ,numero*3)

# num=int(input("Ingrese un num"))

# numeros.append(num)

# print(numeros)

# Shigeuru, Hideki, Hideo

# Miyamoto, Anno, Kojima

# Shigeru Miyamoto
# Hideki Anno
# Hideo Kojima

# nombres=["Crhistopher", "Steven" ]
# apellidos=["Nolan", "Spilvergo"]
# while True:
#     print('''
#         1.- Ingresar nombre
#         2.- Buscar Nombre
#         3.- Mostrar nombres y apellidos
#         4.- Salir
#           ''')
#     op=int(input("selecciones una opcion: "))
#     match op:
#         case 1:
#             nom=input("Ingrese un nombre: ")
#             nombres.append(nom)
#             ape=input("Ingrese un apellido: ")
#             apellidos.append(ape)
#             # print(apellidos)
#         case 2:
#             busca=input("Ingrese el nombre a buscar: ")
#             if busca in nombres:
#                 print(f"El nombre {busca} existe en la lista ")
#             else:
#                 print(f"El nombre {busca} NO existe en la lista ")
#         case 3:
#             # cont=0
#             # for n in nombres:
#             #     print(cont+1,".- ", nombres[cont], apellidos[cont] )
#             #     cont+=1
#             for i in range(len(nombres)):
#                 print(i+1,".- ", nombres[i], apellidos[i] )
#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("Opcion no valida")


'''
Crear carrito 3.0
Tomar el carrito de compras anterior y 
hacerlo con listas
1.- Ingresar productos
2.- Comprar (sub menu)
3.- Crear Boleta
4.- Salir
Que el carrito comience con 3 productos
Hay que hacer 3 listas, prductos, precios y carrito
'''

productos=["Disco SSD 1TB", "Memoria Ram 8GB", "Mouse"]
precios=[70000, 30000, 15000]
carrito=[]

# while True:
#     print('''
#         1.- Ingresar productos a la tienda
#         2.- Comprar
#         3.- Crear Boleta
#         4.- Salir
#           ''')
#     op=int(input("Ingese una opcion: "))
#     match op:
#         case 1:
#             pro=input("Ingrese el nombre del Producto: ")
#             productos.append(pro)
#             pre=int(input("Ingrese el Precio: "))
#             precios.append(pre)
#         case 2:
#                 for i in range(len(productos)):
#                     print(i+1, ".-", productos[i], "$", precios[i] )
#                 pro=int(input("Selecione que quiere comprar: "))
#                 carrito.append(pro-1)
#                 print("Usted seleccionó ", productos[pro-1])
#                 # print(carrito)
#         case 3:
#             total=0
#             print("---------------0----------------")
#             print("Bienvenido a PC House ")
#             for i in carrito:
#                   print( productos[i], "----- $", precios[i] )
#                   total=total+precios[i]
#             print("Es total de articulos es", len(carrito))
#             print("Su total neto es ", total)
#             print("Su total mas iva es ", total*1.19)
#             print("---------------0----------------")

#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("opcion invalida")
    

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
notas=[7.0,4.6,4.9, 7.0,5.6]

# while True:
#     while True:
#         try:
#             print('''   

#                 1.- ingresar notas
#                 2.- borrar nota
#                 3.- ver notas colocadas
#                 4.- promedio de notas, nota mayor y nota menor
#                 5.- borrar toda las notas
#                 6.- salir
#                     ''')
#             op=int(input())
#             break
#         except Exception:
#             print("Debe ingreser un numero entero valido")
    

#     match op:
#         case 1:
#             nota=float(input("ingrese la nota del alumno: "))
#             notas.append(nota)
#         case 2:
#             for num, n in enumerate(notas):
#                 print(num+1,".- ",n)
#             elim=int(input("ingrese cual quiere eliminar: "))
#             notas.pop(elim-1)
#         case 3:
#             print(notas)
#         case 4:
#             if len(notas) == 0:
#                 print("No hay notas para calcular el promedio.")
#             else:
#                 promedio=sum(notas)/len(notas)
#                 print(f"El promedio de las notas es: {round(promedio, 1)}")
#                 print("la nota mayor es", max(notas))
#                 print("la nota menor es", min(notas))
#         case 5:
#             notas.clear()
#         case 6:
#             print("saliendo...")
#             break
#         case _:
#             print("ya wey escoge algo valido")

kilo=[
    [3,4],
    [9,8]
]
print(kilo[1][1])


