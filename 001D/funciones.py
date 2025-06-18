# https://github.com/diegoroblesrivera/droblesr

# uso y ejemplos de funciones




# def suma(n1,n2):
#     print(n1+n2)
# def resta(n1,n2):
#     print(n1-n2)
# def multi(n1,n2):
#     print(n1*n2)
# def division(n1,n2):
#     print(n1/n2)


# # suma()
# num1=int(input("ingrese un numero"))
# num2=int(input("ingrese otro numero"))
# suma(num1,num2)
# resta(num1,num2)
# multi(num1,num2)
# division(num1,num2)
def suma_print():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print(n1+n2)

def suma_return():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    return n1+n2

# suma_print()
# veri=suma_return()
# print(veri)


# def promedio(x,y,z):
#     return (x+y+z)/3
# print(promedio(40, 17,22))
# if promedio(40, 17,22) >=40:
#     print("El alumno aprobó")
# else:
#     print("El alumno reprobó")


'''Crear un programa para calcular un porcetaje descuento
Pedir al usuario  el precio , y el descuento 
a aplicar. Mostar los resultados

Hacer otro para calcular el IVA

'''
#               1000   20%
# def calc_desc(precio, desc):
#     return precio*(desc/100)

# p=int(input("Ingrese el precio: "))
# d=int(input("Ingrese el descuento: "))
# midesc=calc_desc(p,d)
# print( "El descuento es de ", midesc)
# print("El precio a pagar es ", p-midesc )



# productos=["Zapato"]
# precio=[20000]



# print(prod_sport[0]["nombre"])

# print(prod_sport)

# # prod_sport.insert(0,{"nombre":"paleta", "precio":14000})

# print(prod_sport)

prod_college=[
    {"nombre":"lapiz", 
     "precio":400},

    {"nombre":"goma", 
     "precio":300} ,
     
    {"nombre":"estuche", 
     "precio":2000} 
]
prod_sport=[
    {"nombre":"zapato", 
     "precio":20000},

    {"nombre":"pelota", 
     "precio":24000} ,
     
    {"nombre":"raqueta", 
     "precio":74000} 
]
prod_sport[0]["nombre"]

def mostrar_art(lista):
    for n, p in enumerate(lista):
        print(n+1, ".- ", p["nombre"], "$", p["precio"] )
def insertar(lista):
    nom=input("Ingrese el nombre del producto: ")
    pre=int(input("Ingrese el precio: "))
    lista.insert(0,{"nombre":nom, "precio":pre})
def actualizar(lista):
    mostrar_art(lista) 
    opc=int(input("Seleccione el producto a actualizar"))
    print(lista[opc-1])
    nn=input("Ingrese nuevo Nombre")
    np=int(input("Ingrese nuevo Precio"))
    lista[opc-1]["nombre"]=nn
    lista[opc-1]["precio"]=np
    print("Articulo actualizado!")
def borrar(lista):
    mostrar_art(lista) 
    opc=int(input("Seleccione el producto a borrar"))
    lista.pop(opc-1)
def menu(lista):
    while True:
        try:
            print('''
                1.- Agregar producto
                2.- Mostrar Productos
                3.- Actualizar producto
                4.- Borrar Producto
                5.- Salir
                ''')
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    insertar(lista)
                case 2:
                    mostrar_art(lista)      
                case 3:
                    actualizar(lista)
                case 4:
                    borrar(lista)
                case 5:
                    break
                case _:
                    print("Opcion invalida")
        except Exception:
            print("Solo numeros enteros")

# menu(prod_college)


'''
crear programa CRUD del siguiente 
diccionario
'''

personas={
    1:{"nombre": " Diego Rivera",
       "numeros":[7565434,97834231],
       "estadoCivil": "Casado",
       "trabajando": True,
       "edad": 64},
    2:{"nombre": " Diego Rivera",
       "numeros":[7565434,97834231],
       "estadoCivil": "Casado",
       "trabajando": True,
       "edad": 64},
    3:{"nombre": " Diego Rivera",
       "numeros":[7565434,97834231],
       "estadoCivil": "Casado",
       "trabajando": True,
       "edad": 64}
}


while True:
    try:
        print('''
        1.- Ingresar Persona
        2.- Mostrar listado
        3.- Actualizar persona
        4.- Borrar persona
        5.- Salir
        ''')
        op=int(input("Seleccione una opcion"))
        match op:
            case 1:
                nombre=input("Ingrese el nombre: ")
                numero=int(input("Ingrese el numero: "))
                est=int(input("estado Civil 1.- Casado, 2.- Soltero: "))
                if est==1:
                    estCivil="Casado"
                else:
                    estCivil="Soltero"
                edad=int(input("Ingrese la edad: "))
                nextkey=len(personas)
                personas[nextkey+1]={"nombre": nombre,
                "numeros":[numero],
                "estadoCivil": estCivil,
                "trabajando": True,
                "edad": edad}
                print("Persona ingresada con exito")
            case 2:
                for persona, val in personas.items():
                    print(persona, val)
            case 4:
                for persona, val in personas.items():
                    print(persona, val)
                dell=int(input("Seleccione cual desea borrar"))
                del personas[dell]
            case 5:
                break
            case _:
                print("Opcion invalida")
    except Exception as e:
        print("EL error es: ", e)




