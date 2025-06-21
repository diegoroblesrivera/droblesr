import random

def clave():
    clave=3344
    password=int(input("Ingrese su pass :"))
    while clave!=password:
        print ("ERORR, clave invalida")
        password=int(input("Ingrese su pass :"))

    print("Bienvenido al sistema")

def ruleta():
    barril=random.randint(1,6)
    rul=int(input("Dispare"))

    while rul!=barril:
        rul=int(input("Dispare"))
    print("BANG!!!")

# funcion sin argumento y sin return
def suma():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(n1+n2)

#con argumento y sin return
def suma_arg(n1, n2):
    print(n1+n2)

#sin argumento y con return
def suma_ret():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    return n1+n2

# con argumento y con return
def suma_ret_arg(n1,n2):
    return n1+n2

# # suma()
# # suma_arg(9,8)
# # nume=suma_ret()
# # print(nume*5)
# print(suma_ret_arg(8,9)*4/16)


'''Realizar un a funcion que calcule el IVA

Realizar otra funcion que al pasarle un pecio 
y un numero como porcentaje( ej 20)
calcule es descuento y muestre el valor final'''

productos=[
    {"nombre":"lapiz", "precio": 400},
    {"nombre":"goma", "precio" : 200},
    {"nombre":"estuche", "precio" : 1600}
]

# print(productos[2]["precio"])


def mostrar_articulos(lista):
    for n,producto in enumerate(lista):
        print(n+1, producto["nombre"], producto["precio"])

def insertar(lista):
    nombre=input("Nombre del articulo: ")
    precio=int(input("Precio del articulo: "))
    lista.append({"nombre":nombre, "precio" : precio})

def borrar(lista):
    mostrar_articulos(lista)
    borrar=int(input("Que articulo desea borrar"))
    lista.pop(borrar-1)

def actualizar(lista):
    mostrar_articulos(lista)
    act=int(input("Que articulo desea actualizar"))
    nombre=input("Nombre del articulo: ")
    precio=int(input("Precio del articulo: "))
    lista[act-1]["nombre"]=nombre
    lista[act-1]["precio"]=precio

art_escolares=[
    {"nombre":"lapiz", "precio": 400},
    {"nombre":"goma", "precio" : 200},
    {"nombre":"estuche", "precio" : 1600}
]

art_aseo=[
    {"nombre":"cloro", "precio": 1400},
    {"nombre":"mopa", "precio" : 3200},
    {"nombre":"paño", "precio" : 1100}
]

# print(art_escolares[2]["nombre"])

# '''El articulo lapiz tiene un precio de 400'''
# for item in art_escolares:
#     print(f"El articulo {item["nombre"]} tiene un precio de {item["precio"]}")

'''
1.- Agregar articulo
2.- Borrar Articulo
3.- Actualizar Articulo
4.- Mostrar listado de articulos
5.- Salir
'''
def menu(lista):
    while True:
        try:

            print('''
                1.- Agregar articulo
                2.- Borrar Articulo
                3.- Actualizar Articulo
                4.- Mostrar listado de articulos
                5.- Salir
                ''')
            op=int(input("Seleccione una opcion"))
            match op:
                case 1:
                    insertar(lista)
                case 2: 
                    borrar(lista)
                case 3:
                    actualizar(lista)
                case 4:
                    mostrar_articulos(lista)
                case 5:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion Invalida")    

        except Exception as n:
            print("El Error es", n)


# menu(art_aseo)

personas={
    1:{"nombre": "Liam Neeson",
       "Telefono": 876765454,
       "EstadoCivil": "Soltero",
       "Ciudadano": True},
    2:{"nombre": "Christian Bale",
       "Telefono": 999765454,
       "EstadoCivil": "Soltero",
       "Ciudadano": False},
    3:{"nombre": "Malcom Noname",
       "Telefono": 988880000,
       "EstadoCivil": "Soltero",
       "Ciudadano": True},
    4:{"nombre": "Alan Grant",
       "Telefono": 999760000,
       "EstadoCivil": "Casado",
       "Ciudadano": True},
}

print(personas[4]["Telefono"])

# while True:
#     try:
#         print('''
#         1.- Ingresar Persona
#         2.- Mostrar listado
#         3.- Actualizar persona
#         4.- Borrar persona
#         5.- Salir
#         ''')
#         op=int(input("Seleccione un a opcion"))
#         match op:
#             case 1:
#                 nom=input("Ingrese su nombre")
#                 tel=int(input("Ingrese el numero de telefono"))
#                 est=int(input("1.- Casado, 2.- Soltero "))
#                 if est==1:
#                     estCivil="Casado"
#                 else:
#                     estCivil="Soltero"
#                 est=int(input("Es Ciudadano 1.- Si, 2.- No "))
#                 if est==1:
#                     ciuda=True
#                 else:
#                     ciuda=False
#                 ld=len(personas)+1
#                 personas[ld]={"nombre": nom,
#                             "Telefono": tel,
#                             "EstadoCivil": estCivil,
#                             "Ciudadano": ciuda}
#             case 2:
#                 for n,persona in personas.items():
#                     print(n, persona)
#             case 5:
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception as e:
#         print("EL error es: ", e)




