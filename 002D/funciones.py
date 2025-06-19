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

def suma_arg(n1,n2):
    print(n1+n2)

def suma_ret():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    return n1+n2

def suma_ret_arg(n1,n2):
    return n1+n2



# suma()
# suma_arg(9,8)
# print(suma_ret()*3)
# print(suma_ret_arg(6,9))

def suma_3000(num):
    return num-3000

# result=suma_3000(4000)
# print(result)

# def cal_iva(num):
#     return num*1.19
# result=cal_iva(4000)
# print(result)

def cal_desc(precio,desc):
    return precio-(precio*desc/100)

#        -5 -4 -3  -2  -1
numeros=[10, 5, 9 , 34, 20]
#         0  1  2   3   4
#                       0                                          1                            2
productos=[{"nombre":"lapiz", "precio": 400}, {"nombre":"goma", "precio" : 200}, {"nombre":"estuche", "precio" : 1600} ]

productos=[
    {"nombre":"lapiz", "precio": 400},
    {"nombre":"goma", "precio" : 200},
    {"nombre":"estuche", "precio" : 1600}
]


# print(productos[2]["precio"])

print(productos)
nombre=input("Nombre del producto")
precio=int(input("precio del producto"))
productos.append({"nombre":nombre, "precio": precio})
print(productos)

'''
1.- Agregar articulo
2.- Borrar Articulo
3.- Actualizar Articulo
4.- Mostrar listado de articulos
5.- Salir
'''

