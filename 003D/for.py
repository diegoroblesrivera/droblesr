# otros ejercicos de for

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
        perros=int(input("Ingrese la cantidad de perros: "))
        while perros<1:
            print("Debe ingresr 1 o mas perros")
            perros=int(input("Ingrese la cantidad de perros: "))
        cuota=4
        cumplen=0
        print("Los perros salieron de caza!!!")
        for p in range(perros):
            conejos=random.randint(0,8)
            time.sleep(1)
            if conejos>=cuota:
                print(f"El perro {p+1} trajo {conejos} conejos, cumplio la cuota")
                cumplen+=1
            else:
                print(f"El perro {p+1} trajo {conejos} conejos, se queda sin filete")
        print(f" El total de perros que cumplio la cuota fue {cumplen} ")
        print(f" El total de perros que no cumplio la cuota fue {perros-cumplen} ")
        break
    except Exception:
        print("Solo debes poner numeros enteros")


# Quiere pasar el ramo?
# Pregunte la cantidad de rojos en el curso
# Los talleres hay en el semestre son 4
# Por cada taller asistido obtiene 0.3 decimas
# Si el alumno tiene mas de 1 punto
# tiene la bendicion dlel profesor
# sino, no se le puede ayudar
# ingrese la nota final y sume las decimas acomuladas
# Muestre si aprueba o reprueba .
# try:
#     n1=int(input("Ingrese un num: "))
#     n2=int(input("Ingrese un num: "))
#     print("La division es ",n1/n2 )
# except ZeroDivisionError as nombre_de_excepcion:
# 	# Código para manejar la excepción
# 	print(f"Se produjo una excepción: {nombre_de_excepcion}")


while True:
    try:
        op=float(input("Ingres un num: "))
        break
    except Exception:
        print("Debe ingresar solo numeros ")
        