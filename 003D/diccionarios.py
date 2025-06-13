# son conjuntos de pares de datos

dic={
    "nombre": "David Finch",
    "numero": 978676655,
    "casado" : True
}

# print(dic["numero"])

# for key, value in dic.items():
#     print(key, value)

frutas={
    "manzana": 1500,
    "frutilla": 1600,
    "durazno": 3800

}

print(frutas)

frutas["pera"]=1200


'''
Usando diccionarios, haga este programa
1.- Ingresar fruta y precio
2.- Actulizar precio
3.- Borrar Furta y precio
4.- Mostrar todas las frutas y precios
5.- Comprar
6.- Salir
'''
total=0
while True:
    print('''1.- Ingresar fruta y precio
2.- Actulizar precio
3.- Borrar Furta y precio
4.- Mostrar todas las frutas y precios
5.- Comprar
6.- Salir''')
    op=int(input("Seleccione una opcion"))
    match op:
        case 1:
            fru=input("Ingres la fruta")
            val=input("ingrese el precio")

            frutas[fru]=val
        case 2:
            for key, value in frutas.items():
                print(key, value)
            sel=int(input())
        case 3:
            for key, value in frutas.items():
                print(key,".-", value)
            dell=input("Seleccione la fruta a borrar")
        case 4:
            for key, value in frutas.items():
                print(key,".-", value)
        case 5:
            opc=-1
            while opc!=0:
                for key, value in frutas.items():
                    print(key,".-", value)
                opc=input("Seleccione una opcion")
                if opc==0:
                    break
                else:
                    total=total+frutas[opc]
            print("el total a pagar es ", total)    
        case 6:
            print("Saliendo")
            break
        case _:
            print("opcion invalida")







