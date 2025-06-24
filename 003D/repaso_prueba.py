#  nuevos dicionarios y manipulacion de datos


juegos={
    1:{
        "nombre":"Metroid Dread",
        "precio": 50000,
        "code":"MMdd2023"
    },
    2:{
        "nombre":"Pikmin 4",
        "precio": 55000,
        "code":"pKMn2022"
    }
}

# for j, datos in juegos.items():
#     print(j, datos)

# nombre=input("Ingrese el nombre del juego")
# precio=int(input("Ingrese el precio"))
# code=input("Ingres el codigo")

# juegos[4]={
#         "nombre":nombre,
#         "precio": precio,
#         "code":code
#     }

# for j, datos in juegos.items():
#     print(j, datos)

'''
el codigo debe tener 2 mayusculas,
2 minusculas y 4 numeros
'''

def mostrar_juegos(dic):
    for j, datos in dic.items():
        print(j, datos)

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
        print("El codigo está bien escrito")
        return True
    else:
        print("El codigo está mal escrito")
        return False

def act_juegos(dic):
    mostrar_juegos(dic)
    act=int(input("Seleccione el juego a actulizar: "))
    while True:
        print('''1.- Nombre
                2.- Precio
                3.- Codigo
                4.- Salir''')
        dato=int(input("que dato va a actualizar?: "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre")
                dic[act]["nombre"]=n
            case 2:
                n=int(input("ingrese la nueva raza"))
                dic[act]["precio"]=n
            case 3:
                n=input("ingrese el nuevo codigo")
                if valida_code(n):
                    dic[act]["codigo"]=n
                else:
                    print("el parametro del codigo no es correcto")
                    print('''
                    el codigo debe tener, 2 mayusculas, 
                    2 minusculas y 4 numeros ''')
            case 4:
                break
            case _:
                    print("Opcion invalida")

def borrar_juegos(dic):
    mostrar_juegos(dic)
    borrar=int(input("Cual juego desea borrar? "))
    del dic[borrar]

# El nombre del juego debe tener al menos 2 palabras
def valida_nombre(n):
    esp=0
    pala=0
    for l in n:
        if l==" ":
            esp+=1
        if l!=" ":
            pala+=1
    if esp>=1 and pala>1:
        return True
    else:
        return False

def ingresar_juego(dic):
    while True:
        nombre=input("Ingrese el nombre del juego: ")
        if valida_nombre(nombre):
            break
        else:
            print("nombre invalido, intenta nuevamente")
            nombre=input("Ingrese el nombre del juego: ")
    precio=int(input("Ingrese el precio: "))
    code=input("Ingres el codigo: ")
    if valida_code(code):
        largo=list(dic.keys())[-1]
        dic[largo+1]={
                "nombre":nombre,
                "precio": precio,
                "code":code
            }
    else:
        print("el codigo es invalido, intenta de nuevo")

while True:
    try:
        print('''
            1.- Agregar juego
            2.- Mostrar juegos
            3.- Actualizar juego
            4.- Borrar juego
            5.- Salir
            ''')
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                ingresar_juego(juegos)
            case 2:
                mostrar_juegos(juegos)
            case 3:
                act_juegos(juegos)
            case 4:
                borrar_juegos(juegos)
            case 5:
                break
            case _:
                 print("Opcion invalida")
    except Exception:
            print("Solo numeros enteros")