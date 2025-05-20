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