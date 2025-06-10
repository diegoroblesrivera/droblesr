# uso y ejemplos de listas
# que es una lista? 
# es una coleccion de datos

#       -6 -5 -4 -3 -2 -1
numeros=[3, 6, 2,88,"lol",9]
#        0  1  2  3  4  5

print(numeros[4])

print(numeros.insert(3,1000))
print(numeros)
numeros.remove(88)
print(numeros)
numeros.sort()
print(numeros)

# numeros.append(64)

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
