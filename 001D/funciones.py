https://github.com/diegoroblesrivera/droblesr

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

list_prod=[
    {"nombre":"zapato", 
     "precio":20000, 
     "categoria": "vestuario",
     "tamaño": "mediano",
     "enOferta": False},

    {"nombre":"pelota", 
     "precio":24000}
]

# print(list_prod[0]["nombre"])

# print(list_prod)

# # list_prod.insert(0,{"nombre":"paleta", "precio":14000})

# print(list_prod)




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
                nom=input("Ingrese el nombre del producto: ")
                pre=int(input("Ingrese el precio: "))
                list_prod.insert(0,{"nombre":nom, "precio":pre})
            case 2:
                for p in list_prod:
                    print(p)        
            case 3:
                # for n, p in enumerate(list_prod):
                #     print(n+1, ".- ", p)
                for i in range(len(list_prod)):
                    print(i+1, ".-", list_prod[i])
                opc=int(input("Seleccione el producto a actualizar"))
                print(list_prod[opc-1])
                nn=input("Ingrese nuevo Nombre")
                np=int(input("Ingrese nuevo Precio"))
                list_prod[opc-1]["nombre"]=nn
                list_prod[opc-1]["precio"]=np
                print("Articulo actualizado!")
            case 5:
                break
            case _:
                print("Opcion invalida")
    except Exception:
        print("Solo numeros enteros")







