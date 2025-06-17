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
        

def suma():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print(n1+n2)

def suma_arg(n1, n2):
    print(n1+n2)

def suma_ret():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    return n1+n2

def suma_arg_ret(n1, n2):
    return n1+n2


def resta_arg(n1, n2):
    print(n2-n1)

# suma()
# suma_arg(7, 9)
# resta_arg(10,6)
# nume=suma_ret()
# print(nume)
# print(suma_arg_ret(10, 40))


'''Realizar un a funcion que calcule el IVA

Realizar otra funcion que al pasarle un pecio 
y un numero como porcentaje( ej 20)
calcule es descuento y muestre el valor final'''


def cal_iva(n):
    return n*0.19

def cal_desc(precio, porc):
    return precio*(porc/100)

# neto=1500

# print("El IVA es ", cal_iva(neto))
# print("El precio total es ", cal_iva(neto)+neto) 


articulos_escolares=[
    {"nombre":"lapiz", "precio": 400},
    {"nombre":"goma", "precio" : 200},
    {"nombre":"estuche", "precio" : 1600}
]

articulos_aseo=[
    {"nombre":"cloro", "precio": 1600},
    {"nombre":"quick", "precio" : 1500},
    {"nombre":"mopa", "precio" : 2500}
]


# for producto in articulos_escolares:
#     print("El precio del articulo ", producto["nombre"], "es ", producto["precio"])


def muestra_lista(lista):
    for n,producto in enumerate(lista):
        print(n+1, producto["nombre"], producto["precio"])

def agregar(lista):
    nombre=input("ingrese el nombre del articulo")
    precio=int(input("ingrese el nombre del precio"))
    lista.append({"nombre":nombre, "precio":precio})

def borrar(lista):
    muestra_lista(lista)
    borrar=int(input("Seleccione cual desea borrar"))
    lista.pop(borrar-1)

def actualizar(lista):
    muestra_lista(lista)
    act=int(input("Seleccione cual desea actualizar"))
    nombre=input("ingrese el nombre del articulo")
    precio=int(input("ingrese el nombre del precio"))
    lista[act-1]["nombre"]=nombre
    lista[act-1]["precio"]=precio

# print(cal_desc(1000, 20))


'''
1.- Agregar articulo
2.- Borrar Articulo
3.- Actualizar Articulo
4.- Mostrar listado de articulos
5.- Salir
'''
def menu_compra(lista):
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
                    agregar(lista)
                case 2:
                    borrar(lista)
                case 3:
                    actualizar(lista)
                case 4:
                    muestra_lista(lista)
                case 5:
                    break
                case _:
                    print("Opcion Invalida")
        except Exception as error:
            print("El Error es : ", error)

# menu_compra(articulos_escolares)


personas={
    1:{"nombre": "Liam Neeson",
       "Telefono": 876765454,
       "EstadoCivil": "Soltero",
       "Cuidadano": True},
    2:{"nombre": "Christian Bale",
       "Telefono": 999765454,
       "EstadoCivil": "Soltero",
       "Cuidadano": False},
    3:{"nombre": "Alan Grant",
       "Telefono": 999760000,
       "EstadoCivil": "Casado",
       "Cuidadano": True},
    4:{"nombre": "Alan Grant",
       "Telefono": 999760000,
       "EstadoCivil": "Casado",
       "Cuidadano": True},
}
print(personas[2]["Telefono"])

