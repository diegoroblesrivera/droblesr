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
#                 print(carrito)
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

vero=[
                [3,4],
                [8,9]
                 ]
print(vero[1][1])
