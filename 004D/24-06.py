def muestra_juegos(dict):
    for j, datos in dict.items():
        print(j, datos)

juegos={
    1:{"nombre": "Metroid Dread",
       "precio": 50000,
       "code": "MTdr2023"},
    2:{"nombre": "Luiguis Mansion",
       "precio": 58000,
       "code": "LgMn2020'"}
}


def ingresa_juego(dict):
    while True:
        nombre=input("Ingrese el nombre del juego")
        if valida_nombre(nombre):
            break
        else:
            print("Nombre Invalido, deben ser al menos dos palabras ")
    while True:
        precio=int(input("Ingrese el precio del juego"))
        if valida_precio(precio):
            break
        else:
            print("Precio Invalido, deben ser entre 8000 y 100000 ")
    while True:
        code=input("Ingrese el codigo del juego")
        if valida_code(code):
            print("inicio de ingreeso")
            print(list(dict.keys())[-1])
            dict[list(dict.keys())[-1]+1]={"nombre": nombre,
                "precio": precio,
                "code": code}
            break
        else:
            print("Juego no ingresado")
''' el code debe tenre 2 mayusculas
2 minusculas y 4 numeros'''
'''el nombre del juego debe tener al menos 2 palabras'''
def valida_nombre(nombre):
    if nombre[-1]!=" " and nombre[0]!=" ":
        for l in nombre:
            if l==" ":
                return True
    else:
        return False


'''el precio del juego debe ser entre 8000 y 100000'''

def valida_precio(precio):
    if precio>=8000 and precio<=100000:
        return True
    else:
        return False

def borrar_juego(dict):
    muestra_juegos(dict)
    borrar=int(input("Seleccione el juego a borrar: "))
    del dict[borrar]

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
        print("la clave está mal escrita")
        return False

def act_perros(dict):
    muestra_juegos(dict)
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
                    print("Nombre no valido")
            case 2:
                n=int(input("ingrese el nuevo precio: "))
                if valida_precio(n):
                    dict[act]["precio"]=n
                else:
                    print("Precio no valido")
            case 3:
                n=input("ingrese el nuevo codigo")
                if valida_code(n):
                    dict[act]["codigo"]=n
                else:
                    print("el paramatro del codigo no es correcto")
                    print('''
                    el codigo debe tener, 2 mayusculas, 2 minusculas 
                    y un numero''')
            case 4:
                break
            case _:
                    print("Opcion invalida")



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
                ingresa_juego(juegos)
            case 2:
                muestra_juegos(juegos)
            case 3:
                print("") #act_juegos(juegos)
            case 4 :
                borrar_juego(juegos)
            case 5:
                break
            case _:
                    print("Opcion invalida")
    except Exception as e:
        print("EL error es: ", e)


