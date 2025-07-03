personas={
    1:{"nombre": "luka",
       "tipo_entrada": "V",
       "codigo": "G1ght"},
    2:{"nombre": "Alan Grant",
    "tipo_entrada": "V",
    "codigo": "hhYY6743"},
    3:{"nombre": "Jhon Hamon",
    "tipo_entrada": "G",
    "codigo": "Guu778"},
}

# nombre=input("Ingrese en nombre")

def verifica_nombre(nombre):
    for i , n in personas.items():
        # print(i, n["nombre"] )
        if nombre==n["nombre"]:
            print("El nombre esta en la base de datos")
            return False
    return True

# personas[list(personas.keys())[-1]+1]={"nombre": "Ganon",
#        "tipo_entrada": "G",
#        "codigo": "llG9ogh"}

# for i , n in personas.items():
#     print(i, n)  

# len(personas)
# print(list(personas.keys())[-1])

# for i in personas.key():
#     print(i)

# for k, v in personas.items():
#     print(k, v)

# v=7

# def valora(v):
#     if v>2:
#         return True
#     else:
#         return False
    
def calcula_envio(valor, envi):
    lista=[]
    if valor <=10000:
        envi*=1.05
        lista.append(envi)
    elif valor>=10001 and valor<=50000:
        envi*=1.15
    else:
        envi*=1.25
    return lista

# print(calcula_envio(20000, 9000))

famosos=["Michael Jackson", "50 Cent", "James Dio"]

# famosos.pop(0) # borra a Michael Jackson
# famosos.remove("50 Cent") # borra a 50 Cent

def mostrar(lista):
    for n,i in enumerate(lista):
        print(n+1,i)

# CRUD de una lista
# while True:
#         print('''

#               1.- Agregar Cantante .
#               2.- Mostrar cantantes
#               3.- Buscar cantante
#               4.- Borrar cantante
#               5.- Salir
#         ''')
#         op=int(input())
#         match op:
#             case 1:
#                 nombre=input("Ingrese el nombre del cantante")
#                 famosos.append(nombre)  # agrega al final de la lista
#                 # famosos.insert(0,nombre) # agrega en la posicion del indice seleccionado         
#             case 2:
#                 mostrar(famosos)
#             case 3:
#                 buscar=input("Ingrese el nombre del cantante a buscar")
#                 if buscar in famosos:
#                     print(f"El nombre {buscar} está en la lista")
#                 else:
#                     print(f"El nombre {buscar} NO está en la lista")
#             case 4:
#                 mostrar(famosos)
#                 buscar=int(input("Ingrese el numero del cantante a borrar"))
#                 famosos.pop(buscar-1)
#             case 5:
#                 ("saliendo")
#                 break
#             case _:
#                 print("escoga una opción valida")


