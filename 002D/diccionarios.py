# es un conjunto de pares de datos

dic={
    "nombre": "Hideo Kojima",
    "numero": 978789898,
    "casado": False
}

print(dic)

dic["ciudad"]="Chiloe"

print(dic)

for llave, valor in dic.items():
    print(llave, valor)

productos={
    "mnazana": 1200,
    "melon": 2000,
    "piña" :3000
}

productos["durazno"]=2500

print(productos)

nom=input("ingrese el nombre producto: ")
valor=int(input("ingrese el valor producto: "))

productos[nom]=valor

print(productos)
