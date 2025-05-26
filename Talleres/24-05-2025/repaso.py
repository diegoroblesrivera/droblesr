# Respaso de toda la unida 2 incluye,
# if, if else, if elif, while, for, match try except

# # Uso y manejo de try except dentro de un bucle while
# while True:
#     try:
#         num=int(input("ingrese un numero: "))
#         break
#     except Exception:
#         print("Solo puede ingresar numeros enteros")
# print("su numero es ", num)    

# # Ejemplo de sintaxis de try except independiente de un bucle
# try:
#     num=int(input("ingrese un numero: "))
# except Exception:
#     print("Solo puede ingresar numeros enteros")
# else: # 98% no se usa
#     print("Si es que no hay excepcion")
# finally: # 99% de las veces no se usa
#     print("Este bloque se ejecutara si o si, sin importar si hay excepcion o no")

# # Menu simple de opciones con numeros enteros
# while True:
#     try:
#         opcion=int(input('''
#                         Seleccione una opcion con un numero entero
#                         1.- Opcion 1
#                         2.- Opcion 2
#                         3.- Opcion 3
#                         4.- Salir
#                             '''))
#         match opcion:
#             case 1:
#                 print("Has seleccionado la opcion 1")
#             case 2:
#                 print("Has seleccionado la opcion 2")
#             case 3:
#                 print("Has seleccionado la opcion 3")
#             case 4:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception:
#         print("Solo puede ingresar numeros enteros")     
    
  
# # Ejemplo de carrito con categorias  
# total=0
# cantArt=0    

# while True:
#     try:
#         opcion=int(input(''' Carrito de compras
#                         Seleccione una opcion con un numero entero
#                         1.- Comprar Frutas
#                         2.- Comprar Verduras
#                         3.- Pagar
#                         4.- Salir
#                             '''))
#         match opcion:
#             case 1:
#                 while True:
#                     try:
#                         opcion=int(input('''
#                                         Seleccione una opcion con un numero entero
#                                         1.- Frutilla $1500
#                                         2.- Pera $1200
#                                         3.- Manzana $ 1300
#                                         4.- Volver al menu principal
#                                             '''))
#                         match opcion:
#                             case 1:
#                                 print("Has seleccionado Frutilla")
#                                 total+=1500
#                                 cantArt+=1
#                             case 2:
#                                 print("Has seleccionado Pera")
#                                 total+=1200
#                                 cantArt+=1
#                             case 3:
#                                 print("Has seleccionado Manzana")
#                                 total+=1300
#                                 cantArt+=1
#                             case 4:
#                                 print("Volviendo...")
#                                 break
#                             case _:
#                                 print("Opcion invalida")
#                     except Exception:
#                         print("Solo puede ingresar numeros enteros")   
#                     print(" TU total hasta ahora es ", total)
#             case 2:
#                 while True:
#                     try:
#                         opcion=int(input('''
#                                         Seleccione una opcion con un numero entero
#                                         1.- Papa $1500
#                                         2.- Lechuga $1200
#                                         3.- Cebolla $ 1300
#                                         4.- Volver al menu principal
#                                             '''))
#                         match opcion:
#                             case 1:
#                                 print("Has seleccionado Papa")
#                                 cant=int(input("Cuantas papas llevara?"))
#                                 total+=cant*1500
#                                 cantArt+=cant
#                             case 2:
#                                 print("Has seleccionado Lechuga")
#                                 total+=1200
#                                 cantArt+=1
#                             case 3:
#                                 print("Has seleccionado Cebolla")
#                                 total+=1300
#                                 cantArt+=1
#                             case 4:
#                                 print("Volviendo...")
#                                 break
#                             case _:
#                                 print("Opcion invalida")
#                     except Exception:
#                         print("Solo puede ingresar numeros enteros")   
#                     print(" TU total hasta ahora es ", total)
#             case 3:
#                 print("Has seleccionado pagar")
#                 print(f"El total de articulos es {cantArt}")
#                 print(f"El total a pagar es {total}")
#                 print(f"El total a pagar mas IVA es {round(total*1.19)}")
#             case 4:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception:
#         print("Solo puede ingresar numeros enteros")  

# ## Domingo de pascua ####
# Preguntar la Cantidad de niños de niños que buscan huevitos de chocolates
# Cuando se termine la busqueda , preguntar cantos huevos encontró cada uno
# y clasificarlos de la siguiente forma
# Menos de una docena : NOOB
# Entre una docena a 24: Master
# 25 huevos o mas :Legend
# Mostrar resumen, y mostrar la mayor cantidad de huevitos encontrados por un solo niño
import random
while True:
    try:
        cantNiños=int(input("Cuantos niños van a buscar huevitos?  ")) 
        while cantNiños<0:
            print("Error, solo ingres numeros positivos")
            cantNiños=int(input("Cuantos niños van a buscar huevitos?  ")) 
        noob=0
        master=0
        legend=0
        top=0
        for n in range(cantNiños):
            cantHuevos=random.randint(5,30)
            if cantHuevos>top:
                top=cantHuevos    
            print(f"El niño numero {n+1} encontró {cantHuevos} huevos")
            if cantHuevos<12:
                noob+=1
            elif cantHuevos>=12 and cantHuevos<=24:
                master+=1
            else:
                legend+=1
        print("La cant del grupo noob es ", noob)
        print("La cant del grupo master es ", master)
        print("La cant del grupo legend es ", legend)
        print("La mayor cant de huevos encontrada por un niño fue", top)
        break
    except Exception:
        print("Solo numeros enteros")



