# crud de diccionarios
def mostrar_juegos(dic):
    for j, datos in dic.items():
        print(j, datos)



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

def valida_precio(precio):
    if precio<8000 or precio>100000:
        return False
    else:
        return True
def valida_nombre(frase):
    if " " in frase:
        return True
    else:
        return False
    

def agregar_juego(dic):
    ultima=list(dic.keys())[-1]
    while True:
        nombre=input("ingrese el nombre del juego: ")
        if valida_code(nombre):
            break
        else:
            print("""El nombre del juego deben ser dos palabras""")
    while True:
        precio=int(input("ingrese el precio del juego: "))
        if valida_precio(precio):
            break
        else:
            print("""El nombre del juego deben ser dos palabras""")
    while True:
        code=input("ingrese el codigo del juego: ")
        if valida_code(code):
            dic[ultima+1]={
                    "nombre":nombre,
                    "precio": precio,
                    "code":code
                }
            print("Juego Ingresado con exito")
            break
        else:
            print("""Codigo invalido, debe tener 2 mayusculas
                  ,2 minusculas y 4 numeros""")

def act_juegos(dict):
    mostrar_juegos(dict)
    act=int(input("Seleccione el perro a actulizar?: "))
    while True:
        print('''1.- Nombre
                2.- Precio
                3.- Codigo
                4.- Salir''')
        dato=int(input("que dato va a actualizar?: "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre: ")
                dict[act]["nombre"]=n
            case 2:
                n=input("ingrese el nuevo precio: ")
                dict[act]["precio"]=n
            case 3:
                n=input("ingrese el nuevo codigo")
                if valida_code(n):
                    dict[act]["code"]=n
                else:
                    print("el paramatro del codigo no es correcto")
                    print('''
                    el codigo debe tener, 2 mayusculas, 2 minusculas, 
                    4 numero y un largo exacto de 8''')
            case 4:
                break
            case _:
                    print("Opcion invalida")

def borrar_juego(dict):
    mostrar_juegos(dict)
    borrar=int(input("Seleccione el juego a borrar"))
    if borrar in dict:
        del dict[borrar]
        return True
    else:
        print("El juego no existe")
        return False
   
'''el codigo debe tener 2 mayusculas,
2 minusculas y 4 numeros'''
'''El nombre debe tener al menos 2 palabras'''
'''El precio debe estar en tre 8000 y 100000'''

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
                agregar_juego(juegos)
            case 2:
                mostrar_juegos(juegos)
            case 3:
                act_juegos(juegos)
            case 4:
                borrar_juego(juegos)
            case 5:
                break
            case _:
                 print("Opcion invalida")
    except Exception:
            print("Solo numeros enteros")

