# Repaso de listas y diccionarios

#listas

#        -5 -4 -3 -2 -1  
milista=[5, 8, 66, 7, 2]
#        0  1   2  3  4

# print(milista)

# milista.sort()

# print(milista)

# milista.reverse()

# print(milista)



# el primer elemento de la lista siempre es indice 0
# el ultimo elemento de la lista siempre es indice -1

# print(milista)
# print(milista[-2])

# # recorrer una lista

# for elem in milista:
#     print(elem)
    
    
# diccionarios
# es un conjunto de pares de datos

# dic={"nombre": "Diego Robles",
#      "numero": 79873432,
#      "casado": True,
#      "empleado": True,
#      "direccion": "Los Claveles #456"
#      }

# print(dic)

# dic["edad"]=64

# print(dic)

# dic["empleado"]=False

# print(dic)


# corredores=["Slatan", "Bombasi", "Lando"]
# tiempos=[10.9, 11.1, 12.5]

# while True:
#     try:
#         print('''
#             1.-Registrar Corredor y tiempo
#             2.- Ver listado de corredores
#             3.- Ver estadisticas (Tiempo menor, timepo mayor, ordenados por mas rapido)
#             4.- Salir
#             ''')
#         op=int(input("Seleccione una opcion: "))
#         match op:
#             case 1:
#                 corre=input("Ingrese el nombre del corredor: ")
#                 corredores.append(corre)
#                 tie=float(input("Registe su mejor tiempo: "))
#                 tiempos.append(tie)
#             case 2:
#                 for i in range(len(corredores)):
#                     print(f"Corredor: {corredores[i]} , Tiempo: {tiempos[i]}")
#             case 3:
#                 print("EL tiempo mas rapido es", min(tiempos) )
#                 print("EL tiempo mas alto es", max(tiempos) )
#                 print("Ordenados de mas rapido a mas lento")
#                 tiempos.sort()
#                 print(tiempos)
#             case 4:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opcion invalida")

#     except Exception as e:
#         print("Error:" , e)
    
productos={
    "lapiz": 100,
    "goma": 100,
    "estuche": 500,
    "plumon":1000
}    

# print(productos)
# productos["goma"]=2000
# print(productos)

    
while True:
    try:
        print('''
            1.- Agregar articulo y precio
            2.- Ver listado
            3.- Borrar Articulo
            4.- Actualizar precio
            5.- Salir
            ''')
        op=int(input("Seleccione un a opcion: "))
        match op:
            case 1:
                art=input("Ingrese el nombre del articulo: ")
                precio=int(input("Ingres el precio del articulo: "))
                productos[art]=precio
            case 2:
                for nom, precio in productos.items():
                    print(nom,"$", precio)
            case 3:
                for nom, precio in productos.items():
                    print(nom,"$", precio)
                borrar=input("Cual es el articulo que desea borrar? ")
                del productos[borrar]
                print(f"El articulo {borrar} fue borrado")
            case 4:
                for nom, precio in productos.items():
                    print(nom,"$", precio)
                art=input("Cual es el articulo cuyo precio desea actualizar? ")
                if art in productos:
                    precio=int(input("Ingrese el precio nuevo: "))
                    productos[art]=precio
                else:
                    print("El articulo no existe")
            case 5:
                print("Saliendo")
                break
            case _:
                print("Opcion invalida")
    except Exception as error:
        print("Error, hiciste algo mal:" , error)
        
 
'''
Hacer un sistema de login con diccionario
Debe verificar si el usuario existe
de existir le pregunta la contaseña
y da solo  3 oportunidades para acertar
El diccionario debe de estar previamente
escrito antes de iniciar el sistema
'''   

listado_usuarios=[
    {"usuario": "pipe", "pass": 3344},
    {},
    {}
]

usuarios={ 
          "pipe": 3344,
          "lola": 6655
          }
    
    