def mostrar_juegos(dict):
    for j, dato in dict.items():
        print(j, dato)
def valida_code(clave):
    Mayuscula=0
    Minuscula=0
    Numero=0
    for palabra in clave:
        if palabra.isupper():
            Mayuscula+=1
        if palabra.islower():
            Minuscula+=1
        if palabra.isdigit():
            Numero+=1
    if Mayuscula==2 and Minuscula==2 and Numero==4 :
        print("la clave está bien escrita")
        return True
    else:
        print('''El codigo del juego debe tener 2 mayusculas, 2 minisculas
                    y 4 numeros ''')
        return False
def valida_precio(p):
    if p>=8000 and p<=100000:
        return True
    else:
        return False
def valida_nombre(nombre):
    for l in nombre:
        if " " ==l:
            return True   
def insertar_juego(dict):
    while True:
        nombre=input("Ingrese el nombre: ")
        if valida_nombre(nombre):
            break
        else:
            print("EL nombre del juego debe tener al menos 2 palabras")
    while True:
        precio=int(input("Ingrese el precio: "))
        if valida_precio(precio):
            break
        else:
            print("EL precio debe estar entre $8.000 y $100.000")
    while True:
        codigo=input("Ingrese el codigo: ")
        if valida_code(codigo):
            pos=list(dict.keys())[-1]
            dict[pos+1]={"nombre":nombre, "precio":precio,"code": codigo}
            break
        else:
            print("No se agregó el juego")

''' El nombre debe tener por lo menos 2 palabras'''
'''El precio debe estar entre $8.000 y $100.000'''
'''El codigo del juego debe tener 2 mayusculas, 2 minisculas
y 4 numeros '''


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
                n=input("ingrese el nuevo nombre")
                if valida_nombre(n):
                    dict[act]["nombre"]=n
                else:
                    print("EL nombre del juego debe tener al menos 2 palabras")
            case 2:
                n=input("ingrese la nueva precio")
                if valida_precio(n):    
                    dict[act]["precio"]=n
                else:
                    print("EL precio debe estar entre $8.000 y $100.000")
            case 3:
                n=input("ingrese el nuevo codigo")
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


def borrar_juegos(dict):
    mostrar_juegos(dict)
    borrar=int(input("Que juego desea borrar?"))
    del juegos[borrar]
juegos={
    1:{"nombre":"Metroid Dread",
       "precio": 55000,
       "code": "MtDr2022"
       },
    2:{"nombre":"Zelda TOTK",
       "precio": 65000,
       "code": "zdTK2025"
       }
}



# mostrar_juegos(juegos)

# insertar_juego(juegos)

# mostrar_juegos(juegos)


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
                insertar_juego(juegos)
            case 2:
                mostrar_juegos(juegos)
            case 4:
                borrar_juegos(juegos)
            case 5:
                break
            case _:
                    print("Opcion invalida")
    except Exception as e:
        print("EL error es: ", e)

