# repasamos listas y diccionarios

# perros de caza

perros={
    1:{"nombre": "Droopy",
       "raza": "Dog Hount",
       "codigo": "Dphh06"},
    2:{"nombre": "Spike",
       "raza": "Bultierrer",
       "codigo": "BDil77"}
}
# #                  -1
# perros.keys() # [1, 4]
# #                   
# list(perros.keys())[-1]

def mostrar_perros(dict):
    for key, perro in dict.items():
        print(key , perro)
def valida_pass(clave):
    Mayuscula=False
    Minuscula=False
    Numero=False
    for palabra in clave:
        if palabra.isupper():
            Mayuscula=True
        if palabra.islower():
            Minuscula=True
        if palabra.isdigit():
            Numero=True
    if Mayuscula and Minuscula and Numero and len(clave)==6:
        print("la clave está bien escrita")
        return True
    else:
        print("la clave está mal escrita")
        return False

def ingrese_perro(dict):
    nombre=input("Ingrese un nombre: ")
    raza=input("Ingrese la raza: ")
    codigo=input("Ingrese su codigo: ")
    if valida_pass(codigo):
        largo=list(dict.keys())[-1]
        dict[largo+1]={"nombre": nombre,
                    "raza": raza,
                    "codigo": codigo}
    else:
                    print("el paramatro de la clave no es correcto")
                    print('''
                    el codigo debe tener, una mayuscula, una minuscula, 
                    un numero y un largo exacto de 6''')

def act_perros(dict):
    mostrar_perros(dict)
    act=int(input("Seleccione el perro a actulizar?: "))
    while True:
        print('''1.- Nombre
                2.- Raza
                3.- Codigo
                4.- Salir''')
        dato=int(input("que dato va a actualizar?: "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre")
                dict[act]["nombre"]=n
            case 2:
                n=input("ingrese la nueva raza")
                dict[act]["raza"]=n
            case 3:
                n=input("ingrese el nuevo codigo")
                if valida_pass(n):
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

def borrar_perros(dict):
    mostrar_perros(dict)
    borrar=int(input("Seleccione el perro a borrar: "))
    del dict[borrar]

while True:
    try:
        print('''
              1.- Registrar un perro
              2.- Mostrar perros
              3.- Actualizar Perro
              4.- Borrar Perro
              5.- Salir
              ''')
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                ingrese_perro(perros)
            case 2:
                mostrar_perros(perros)
            case 3:
                act_perros(perros)
            case 4 :
                borrar_perros(perros)
            case 5:
                break
            case _:
                    print("Opcion invalida")
    except Exception as e:
        print("EL error es: ", e)


'''
Crear gestion de vehiculos
Crear programa para un parking de autos
se debe ingresar
Marca, año, patente, Tipo

Marca: tipo string, se debe tipear la marca
año: tipo int , solo de 4 digitos enteros
patente: debe tener 4 letras minusculas y 2 digitos
tipo: S= sedan, C= Camioneta, M= moto

Se deve validar cada aspecto y tener un mantenedor para 
todos los vehiculos motorizados

1.- Ingresar Vehiculo
2.- Mostrar Vehiculos
3.- Actualizar Vehiculo
4.- Marcar salida de Vehiculo con hora*
5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
6.- Salir

Usar dunciones con argumentos para poder validar
y para poder llamar las acciones dentro del menu
'''




