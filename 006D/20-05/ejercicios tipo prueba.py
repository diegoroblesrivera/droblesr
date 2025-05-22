# Perros de caza
# Pida al usuario la cantidad de perros
# Muestre cual es la cuota minima de conejos
# lugo consulte cauntos conejos trajo
# si el perro trajo la cantidad minima
# cumplio la cuota, sino, se queda sin filete
# mostrar resumen de perro que cumplieron y los que no
import random, time
while True:
    try:
        perros=int(input("ingrese los perros que irán a la caza: "))
        while perros<1:
            print("Ingrese un valor entero positivo")
            perros=int(input("ingrese los perros que irán a la caza: "))
        cuota=3
        cumple=0
        print("Comienza la caza")
        for p in range(perros):
            conejos=random.randint(0,6)
            if conejos>=cuota:
                print(f"El perro {p+1} trajo {conejos} conejos")
                print("Hay Flete!")
                cumple+=1
            else:
                print(f"El perro {p+1} trajo {conejos} conejos")
                print("no hay filete")
        print(f" La cant de perro que cumplio fue {cumple}")
        print(f" La cant de perro que NO cumplio fue {perros-cumple}")
        break
    except Exception:
        print("Ingrese solo numeros enteros")

# Quiere pasar el ramo?
# Pregunte la cantidad de rojos en el curso
# Los talleres hay en el semestre son 4
# Por cada taller asistido obtiene 0.3 decimas
# Si el alumno tiene mas de 1 punto
# tiene la bendicion dlel profesor
# sino, no se le puede ayudar
# ingrese la nota final y sume las decimas acomuladas
# Muestre si aprueba o reprueba .

rojos=int(input("Diga la cant de rojos: "))
talleres=5
tDecimas=0

for r in range(rojos):
    for t in range(talleres):
        asist=input(f"Asistio al taller numero {t+1}? si/no: ")
        if asist.lower()=="si":
            tDecimas+=0.3
    if tDecimas>=1:
        print(" Tiene la bendicion del profe")
    else:
        print("Nada mas que hacer ")
    nf=float(input("Ingrese su nota final"))
    nf+=tDecimas
    print(f"su nota final es {nf}")
    if nf>=4:
        print("El alumno aprobó")
    else:
        print("El alumno reprobó")
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
