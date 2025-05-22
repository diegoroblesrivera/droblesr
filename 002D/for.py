# otros ejercicos de for

# Perros de caza
# Pida al usuario la cantidad de perros
# Muestre cual es la cuota minima de conejos
# lugo consulte cauntos conejos trajo
# si el perro trajo la cantidad minima
# cumplio la cuota, sino, se queda sin filete
# mostrar resumen de perro que cumplieron y los que no
import random, time
# while True:
#     try:
#         perros=int(input("Cuantos perros va a la caza?"))
#         break
#     except Exception:
#         print("Solo se permiten nuemros enteros")
        

# psi=0
# cuota=4
# conejosT=0
# for perro in range(perros):
#     time.sleep(1)
#     conejos=random.randint(0,8)
#     conejosT+=conejos
#     print(f"El pero {perro+1} trajo {conejos} conejos")
#     if conejos>=cuota:
#         print("Tiene filete")
#         psi+=1
#     else:
#         print("NO hay filete para este perro")
# print("La cant de perros que cumplio fue ", psi)
# print("La cant de perros que NO cumplio fue ", perros-psi)
# print("La cant de conejos totales fue", conejosT)

# while True:
#     try:
#         op=int(input("Ingrese un numero: "))
#         break
#     except Exception:
#         print("Solo se permiten nuemros enteros")
        

# Quiere pasar el ramo?
# Pregunte la cantidad de rojos en el curso
# Los talleres que hay en el semestre son 4
# Por cada taller asistido obtiene 0.3 decimas
# Si el alumno tiene mas de 1 punto
# tiene la bendicion dlel profesor
# sino, no se le puede ayudar
# ingrese la nota final y sume las decimas acomuladas
# Muestre si aprueba o reprueba .

cantAR=int(input("ingrese la cant de alumno con nota roja"))
talleres=4
decimas=0
for al in range(cantAR):
    decimas=0
    for t in range(talleres):
        
        print(f"l alumno asistio al taller {t+1}?")
        resp=random.randint(1,2)
        if resp==1:
            decimas+=0.3
    if decimas>=1:
        print("Tiene la bendicion del profesor")
    else:
        print("Si no se ayuda , el profe tampoco puede")
    nt=float(input("cual es su nota final?"))
    print("sus decimas totales fueron" , decimas)
    nt+=decimas
    if nt>=4:
        print("EL alumno aprobó")
    else:
        print("EL alumno reprobó")