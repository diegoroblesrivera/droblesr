dic={
    "nombre": "Alan Grant",
    "numero": 978564533,
    "casado": True
}

print(dic)
dic["nombre"]="Alan Brito"

dic["cuidad"]="Velez"
print(dic)

frutas={
    "Naranja":400,
    "Manzana": 500,
    "Pera":700
}
print(frutas)
frutas["granada"]=1500
print(frutas)

for key, value in frutas.items():
    print(key,"$", value)
