personas={
    1:{"nombre": "luka",
       "tipo_entrada": "V",
       "codigo": "G1ght"}
}
def tipos(tipo):
    if tipo in ["G", "V"]: 
        return True
    else:
        return False
def valida_compra():
    while True:
        nombre=input("Ingrese su nombre")
        if valida_nombre(nombre):
            break
        else:
            print("El nombre ya existe el la DB, elije otro")
    while True:
        tipo=input("Ingrese tipo entrada (V/G)")
        if tipos(tipo):
            break
        else:
            print("El nombre ya existe el la DB, elije otro")
    while True:
        codigo=input("Ingrese el codigo")
        if valid_code(codigo):
            largo=list(personas.keys())[-1]
            personas[largo+1]= {"nombre": nombre,
                        "tipo_entrada": tipo,
                        "codigo": codigo}
            break
        else:
            print("El codigo debe tener una mayuscula, un numero y no debe tener epacios")
    
def valida_nombre(nombre):
    for k, v in personas.items():
        if v["nombre"]==nombre:
            return True
    return False

def valid_code(codigo):
    mayus=0
    space=0
    digitos=0

    for i in codigo:
        if i.isupper():
            mayus+=1
        if i.islower():
            space+=1
        if i.isdigit():
            digitos+=1
    if mayus>=1 and space==0 and digitos>=1 and len(codigo)>=6:

        return True
    else:
        print("codigo invalido")
        return False
def mostrar(lista):
    for i, n in lista.items():
        print(i, n)
def consul(entradas):
    consultar=input("ingrese el nombre")
    for d in entradas:
        if consultar in entradas[d]["nombre"]:
            print("COMPRADOR ENCONTRADO: ")
            print(f"nombre: {entradas[d]['nombre']}, tipo: {entradas[d]['tipo']}, codigo: {entradas[d]['codigo']}")
            return True
    return False
def borrar(lista):
    mostrar(personas)
    cancelar=int(input("ingrese la persona que desea cancelar su compra "))
    if cancelar in lista:
        del lista[cancelar]
        print("compra cancelada correctamente")
    else:
        print("el comprador no existe")

while True:
    try:
        print('''MENU PRINCIPAL
        1.- Comprar entrada.
        2.- Consultar comprador.
        3.- Cancelar compra.
        4.- Salir.''')
        op=int(input("Seleccione una opcion"))
        match op:
            case 1:
                valida_compra()
            case 2:
                consul(personas)
            case 3:
                borrar(personas)
            case 4:
                print("Saliendo")
                break
            case _:
                print("Opcion invalidad")
    except Exception as e:
        print(" algo ha salid mal", e)
