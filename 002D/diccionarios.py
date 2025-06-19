# es un conjunto de pares de datos

# dic={
#     "nombre": "Hideo Kojima",
#     "numero": 978789898,
#     "casado": False
# }

# print(dic)

# dic["ciudad"]="Chiloe"

# print(dic)

# for llave, valor in dic.items():
#     print(llave, valor)

frutas={
    "manazana": 1200,
    "melon": 2000,
    "piña" :3000
}

# frutas["durazno"]=2500

# print(frutas)

# nom=input("ingrese el nombre producto: ")
# valor=int(input("ingrese el valor producto: "))

# frutas[nom]=valor

# print(frutas)



while True:
    try:
        print('''
        1.- Ingresar Fruta
        2.- Mostrar Frutas
        3.- Actualizar Precio
        4.- Eliminar fruta
        5.-Salir
        ''')
        op=int(input("Seleccione una opcion"))
        match op:
            case 1:
                fruta=input("Ingres e nombre de la fruta")
                precio=int(input("Ingrese el precio"))
                frutas[fruta]=precio
            case 2:
                for key,dato in frutas.items():
                    print(key,"$", dato)
            case 3:
                for key,dato in frutas.items():
                    print(key,"$", dato)
                fru=input("Seleccione la fruta cuyo precio actualizara")
                precio=int(input("Ingrese el nuevo precio"))
                frutas[fru]=precio
            case 4:
                for key,dato in frutas.items():
                    print(key,"$", dato)
                borrar=int(input("Ingrese la fruta a borrar"))
                del frutas[borrar]
            case 5:
                print("Saliendo")
                break
            case _:
                        print("Opcion no valida")
    except Exception as e:
        print("El error es ", e)