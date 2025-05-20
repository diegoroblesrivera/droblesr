# otros ejercicos de for

# Perros de caza
# Pida al usuario la cantidad de perros
# Muestre cual es la cuota minima de conejos
# lugo consulte cuantos conejos trajo
# si el perro tran¿jo la cantidad minima
# cumplio la cuota, sino, se queda sin filete
# mostrar resumen de perro que cumplieron y los que no
import random, time

while True:
    try:
        perros=int(input("cuantos perros van a la caza? "))
        while perros<1:
            print("Solo valores enteros positivos")
            perros=int(input("cuantos perros van a la caza? "))
        cuota=3
        pCumplen=0
        for p in range (perros):
            time.sleep(1)
            conejos=random.randint(0,6)
            if conejos>=cuota:
                print(f"El pero {p+1} capturó {conejos} conejos ")
                print("Se ganó un filete")
                pCumplen+=1
            else:
                print(f"El pero {p+1} capturó {conejos} conejos ")
                print("no hay filete para éste perro")
        print(pCumplen," perros llegaron a la cuota")
        print(perros-pCumplen," perros llegaron a la cuota")
        break
    except Exception:
        print("Solo debe poner numeros enteros ")

# Lavado de autos
# Crear un menu para lavar autos
# 1.- Cursar pago del lavado 
# 2.- Ver ventas diarias
# 3.- salir
# El lavado tiene 3 niveles
# 1.- Full $ 15.000, 2- standard 10.000, 3.- Básico $7.000.
# al mostrar las ventas diarias, debe mostar la 
# cantidad de autos que han ingresado y el monto total 
# recaudado. Tambien debe mostrar el monto mas alto pagado  .
    
def pagolavado():
    global ventas, autos, full, standard, basico
    tipodelavado=int(input('''elija su tipo de lavado:
                           1. FUll $15.000
                           2. STANDARD $10.000
                           3. BASICO $7.000
                           '''))
    match tipodelavado:
        case 1:
            ventas+=15000
            autos+=1
            full+=1
            print("selecciono lavado FULL")
        case 2:
            ventas+=10000
            autos+=1
            standard+=1
            print("selecciono lavado STANDARD")
        case 3:
            ventas+=7000
            autos+=1
            basico+=1
            print("selecciono lavado BASICO")
        case _:
            print("opcion invalida")
def ventasdia():
    print(f'''ventas totales ${ventas}
    Num de autos {autos}''')
    if full>=1:
        print("el monto mas alto fue de $15.000")
    elif standard>=1 and full==0:
        print("el monto mas alto fue de $10.000")
    elif basico>=1 and standard==0 and full==0:
        print("el monto mas alto fue de $7.000")
ventas=0
autos=0
full=0
standard=0
basico=0
while True:
    op=int(input(''''elija que quiere hacer:
                1.pago de lavado
                2.ver ventas
                3.salir
                 '''))
    match op:
        case 1:
            pagolavado()
        case 2:
            ventasdia()
            if ventas==0:
                print("usted no ha tenido ningun cliente")
        
        case 3:
            print("hasta la vista")
            break
        case _:
            print("ingrese una opcion valida")