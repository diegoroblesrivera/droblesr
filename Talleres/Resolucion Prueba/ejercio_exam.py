dinosaurios={
    "Trex":{"peso":10,
            "tipo":"terrestre",
            "alimentacion":"carnivoro"},
    "Triceratop":{"peso":6,
                  "tipo":"terrestre",
                  "alimentacion":"hervivoro"},
    "Espinosaurio":{"peso":16,
                  "tipo":"anfibio",
                  "alimentacion":"carnivoro"}
}

def crear():
    nombre=input("Ingrese el nombre del dino")
    peso=input("Ingrese el peso del dino")
    tipo=input("Ingrese el tipo del dino Terrestre , aereo, marino, anfibio")
    ali=input("Ingrese la alimentacion del dino")
    dinosaurios[nombre]={"peso":peso,
                  "tipo":tipo,
                  "alimentacion":ali}
def mostrar():
    for i,n in dinosaurios.items():
        print(f'''Nombre: {i}
                Peso: {n["peso"]}
                Tipo: {n["tipo"]}
                Alimentacion:{n["alimentacion"]}''')
def actualizar():
    mostrar()
    act=input("Ingrese el dinosaurio a actualizar")
    dato=int(input("Cual es el dato que va a actualizar \n1.- Peso, \n2.- Tipo \n3.- Alientacion"))
    match dato:
        case 1:
            d=float(input("Ingrese el peso"))
            dinosaurios[act]["peso"]=d
        case 2:
            d=input("Ingrese el tipo")
            dinosaurios[act]["tipo"]=d
        case 3:
            d=input("Ingrese el alimentacion")
            dinosaurios[act]["alimentacion"]=d
        case _:
             print("Debe ingresar una opcion valida")  
def borrar():
    mostrar()
    borrar=input("Ingrese el dinosaurio a borrar")
    del dinosaurios[borrar]

def estadisticas():
    lista_peso=[] 
    for i,n in dinosaurios.items():
        lista_peso.append(n["peso"])
    print(f"El peso maximo es {max(lista_peso)}")
    print(f"La cantidad de dinos es {len(dinosaurios)}")


while True:
    try:
        op=int(input('''
                     1.- Ingresar Dinosaurio
                     2.- Consultar Dinosaurio
                     3.- Actualizar Dinosauro
                     4.- Borrar Dinosaurio
                     5.- Ver estadisticas( mayor peso, y cantidad de dinos)
                     6.- Salir
                     '''))
        match op:
            case 1:
                crear()
            case 2:
                mostrar()
            case 3:
                actualizar()
            case 4:
                borrar()
            case 5:
                estadisticas()
            case 6:
                print("Terminando Programa ...")
                break
            case _:
                print("Debe ingresar una opcion valida")                
    except Exception as e:
        print("elija una opción valida", e)            
             