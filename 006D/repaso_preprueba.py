# validaciones

# validar si un texto tiene
#  por lo menos 3 numeros

texto="DarkLink64"
# cant_numeros=0
# for p in texto:
#     print(p)
#     if p.isdigit():
#         print("Es digito")
#         cant_numeros+=1
# if cant_numeros>=3:
#     print("la cantidad de numeros es", cant_numeros)
#     print("La palabra cumple con el parametro")
# else:
#     print("la cantidad de numeros es", cant_numeros)
#     print("La palabra NO cumple con el parametro")

# anio=1985

# print(len(str(anio)))

# if len(str(anio)) ==4:
#     print("tiene largo de 4")

# creacion de contraseña 
# Debe tener, tres mayusculas, una miniscula ,
# un # y 3 numeros.
# def valida_pass(password):
#         cMayus=0
#         cMinusculas=0
#         cNumeros=0
#         tine_gato=False

#         for l in password:
#             if l.isupper():
#                 cMayus+=1
#             if l.islower():
#                 cMinusculas+=1
#             if l.isdigit():
#                 cNumeros+=1
#             if l =="#":
#                 tine_gato=True
#         if cMayus<3:
#             print("Debe tener el menos 3 letras en mayusculas")
#         elif cMinusculas<1:
#             print("Debe tener el menos 1 letra1 en minuscula")
#         elif cNumeros<3:
#             print("Debe tener el menos 3 numeros")
#         elif tine_gato==False:
#             print("Debe incuir el caracter '#' ")
#         else:
#             print("Contraseña creada")
#             return True

# pp=False
# while pp!=True:
#     clave=input("Ingrese su contraseña")

#     pp=valida_pass(clave)

# ingreso de productos 

# diccionario para productos

prods={
    1:{"nombre":"Zelda TOTK",
            "precio": 80000,
            "code": "ZZkk1985"},
    2:{"nombre":"Eldel Ring",
        "precio": 45000,
        "code": "EErr2021"}
}

# ll=[1,2]
# #    -1
def valida_code(password):
        cMayus=0
        cMinusculas=0
        cNumeros=0
        for l in password:
            if l.isupper():
                cMayus+=1
            if l.islower():
                cMinusculas+=1
            if l.isdigit():
                cNumeros+=1
        if cMayus!=2:
            print("Debe tener 2 letras en mayusculas")
        elif cMinusculas!=2:
            print("Debe tener el menos 2 letra1 en minuscula")
        elif cNumeros!=4:
            print("Debe tener el menos 4 numeros")
        else:
            print("Contraseña creada")
            return True

# valida_code("AAii2020")
# Code Debe tener, 2 mayusculas, 2 minisculas ,
# y 4 numeros. 
# Nombre debe tener 2 palabras
# precio debe ser entre 8000 y 100000

def valida_nombre(nombre):
    if " " not in nombre:
        print("Debe tener 2 palabras")
        return False
    else:
        return True
    
def valida_precio(precio):
    if precio<8000 and precio>100000:
        print("Precio fuera de rango")
        return False
    else:
        return True

def mostrar_juegos(dict):
    for key, perro in dict.items():
        print(key , perro)

def act_perros(dict):
    mostrar_juegos(dict)
    act=int(input("Seleccione el juego a actulizar?: "))
    while True:
        print('''1.- Nombre
                2.- Precio
                3.- Codigo
                4.- Salir''')
        dato=int(input("que dato va a actualizar?: "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre: ")
                if valida_nombre(n):
                    dict[act]["nombre"]=n
                else:
                    print("El nombre debe tener 2 palabras")
            case 2:
                n=int(input("ingrese el nuevo precio: "))
                if valida_precio(n):
                    dict[act]["precio"]=  n
                else:
                    print("El precio debe se mayor a 8.000 y menor a 100.000")
            case 3:
                n=input("ingrese el nuevo codigo: ")
                if valida_code(n):
                    dict[act]["codigo"]=n
                else:
                    print("el paramatro del codigo no es correcto")
                    print('''
                    el codigo debe tener, una mayuscula, una minuscula, 
                    un numero y un largo exacto de 6''')
            case 4:
                break
            case _:
                    print("Opcion invalida")

def ingresar_juego(dict):
    dict=prods
    nombre=input("Ingrese un nombre: ")
    while True:
        if valida_nombre(nombre):
            print("Nombre correcto")
            break
        else:
            print("EL nombre debe tener  2 palabras")
    precio=int(input("Ingrese el precio: "))
    while True:
        if valida_precio(precio):
            print("Precio dentro del rango")
            break
        else:
            print("El precio debe se mayor a 8.000 y menor a 100.000")
    codigo=input("Ingrese su codigo: ")
    while True:
        if valida_code(codigo) :
            largo=list(dict.keys())[-1]
            dict[largo+1]={"nombre": nombre,
                        "precio": precio,
                        "code": codigo}
            break
        else:
            print("el paramatro de la clave no es correcto")
            print('''
            el codigo debe tener, dos mayusculas, dos minusculas, 
            4 numeros y un largo exacto de 8''')

def borrar_juegos(dict):
    mostrar_juegos(dict)
    borrar=int(input("Seleccione el juego a borrar: "))
    del dict[borrar]

while True:
    try:
        print('''
              1.- Registrar un juego
              2.- Mostrar juegos
              3.- Actualizar juego
              4.- Borrar juego
              5.- Salir
              ''')
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                ingresar_juego(prods)
            case 2:
                mostrar_juegos(prods)
            case 3:
                act_perros(prods)
            case 4 :
                borrar_juegos(prods)
            case 5:
                break
            case _:
                    print("Opcion invalida")
    except Exception as e:
        print("EL error es: ", e)


