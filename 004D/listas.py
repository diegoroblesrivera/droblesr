# uso y ejemplos de listas
# que es una lista? 
# es una coleccion de datos

#     -5 -4  -3 -2 -1
numeros=[7, 5, 33,24, 9]
#      0  1  2  3   4

# print(numeros[-1])

# for numero in numeros:
#     print("numero", numero*5)

# print(numeros)

# numeros.append(64)

# print(numeros)

# numeros.insert(3,100)

# print(numeros)

# frutas=["Manzana", "Mango", "Membrillo"]

# for fruta in frutas:
#     print(fruta)

# Shigeuru, Hideki, Hideo //lista de nombres
# Miyamoto, Anno, Kojima //lista apellidos

# Shigeru Miyamoto
# Hideki Anno
# Hideo Kojima

nombres=[]
apellidos=[]
while True:
    print('''
        1.- Insertar Nombre y apellido
        2.- Mostrar Nombres y apellidos
        3.- Buscar nombre
        4.-Salir
          ''')
    op=int(input("Seleccione una opcion: "))
    match op:
        case 1:
            nom=input("Ingrese un nombre: ")
            nombres.append(nom)
            ape=input("Ingrese un nombre: ")
            apellidos.append(ape)
            print(apellidos)
        case 2:
            # c=0
            # for n in nombres:
            #     print(nombres[c], apellidos[c])
            #     c+=1
            for i in range(len(nombres)):
                print(nombres[i], apellidos[i])
        case 3:
            nom=input("Ingrese un nombre")
            if nom in nombres:
                print(f"El nombre {nom} existe")
            else:
                print(f"El nombre {nom} NO existe")
        case 4:
            print("Saliendo")
            break
        case _:
            print("Opcion Invalida")


