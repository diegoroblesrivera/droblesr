# Calcular el puntaje de credito
# De bede calcular que tanto credito tiene una persona
# en cierta entidad financiera, debera considerar
# cantidad de ingresos, nivel educacional y nacionalidad
# Cantidad de ingresos
# 500.000 a 1.000.000 : 300.000
# 1.000.000 a 1.500.000: 650.000
# 1.500.001 o mas : 1.000.000
# Nivel Educacional 
# Basico : x1, medio: x1.3 , superior: x1.5
# Nacionalidad |
# Chilena : +300.000, Extranjero: +0


# credito=0

# print("elija su rango de ingresos")
# print('''
#    1.500.000 a 1.000.000
#    2. 1.000.001 a 1.500.000
#    3.1.500.000 o superior
#    ''')

# op=int(input())

# if op==1:
#   credito+=300000
# elif op==2:
#    credito+=650000
# elif op==3:
#    credito+=1000000
# else:
#   print("elija una opcion valida")

# print("El credito disponible para usted es de ", credito)

# print("Elija su nivel educacional")

# print('''
#    1.Basica
#    2.Media
#    3.Superior
#    ''')

# op=int(input())

# if op==1:
#    credito*=1
# elif op==2:
#    credito*=1.3
# elif op==3:
#    credito*=1.5
# else:
#   print("elija una opcion valida")

# print("El credito disponible para usted es de ", credito)


# print("Elija su nacionalidad")
# print('''
#    1.Chilena
#    2.Otra
#    ''')

# op=int(input())

# if op==1:
#    credito+=300000
# else:
#    print("NO tiene mas credito, pobre")

# print(f"Su credito total es {credito}")

# print(f"hol"+"a"*10)


# pida al usuario 2 digitos verificando que
#  el segundo sea mayor
# Genere un numero aleatoreo entre esos digitos
# ► e imprima la candidad de veces el 
# simbolo  ▄ (alt+220)

print("Ingrese 2 digitos")

n1=int(input("INgrese un numero"))
n2=int(input("INgrese un numero"))

while n1>n2:
   print("El segundo numero no puede ser menor")
   n2=int(input("INgrese un numero"))



import random
from random import randint

numAzar=randint(n1,n2)
numAzar=random.randint(n1,n2)
print("▄"*numAzar)


# print("ingrese dos Digitos")
# n1=int(input("numero 1: "))
# n2=int(input("numero 2: "))


# while n1>n2:
#    print("El numero 2 no puede ser menor que el numero 1")
#    n2=int(input("numero 2: "))

# num=randint(n1,n2)
# print("▄"*num)

# for i in range(num):
#    print("▄")


# Crear un programa que pida la candidad de ramos
# Luego pida el promedio de cada materia
# basados en su promedio final, aplicar puntaje 
# de beneficios
# 4.5 y 5: 300, 5.1 y 6.0: 500, 6.1 y 7.0 : 800
# Agregar puntaje segun carrera
# Tecnico :+60, Ingenieria: +40, Diplomado: +20

mat=int(input("Ingrese la cant de materias: "))
suma=0
for i in range(mat):
   notaramo=float(input(f"Ingrese la nota del ramo{i+1}: "))
   suma+=notaramo
prom=suma/mat
print("Su nota final es ", round(prom,1))
if prom>=4.5 and prom<=5.0:
   puntaje=300
   print( f"Su puntaje de beneficios es de {puntaje}")
elif prom>=5.2 and prom<=6.0:
    puntaje=500
    print( f"Su puntaje de beneficios es de {puntaje}")
elif prom>=6.1 and prom<=7.0:
    puntaje=800
    print( f"Su puntaje de beneficios es de {puntaje}")
else:
   print(" Es tan porro que no tiene beneficios")

car=int(input('''
            Ingrese su tipo de grado
              1.- Tecnico
              2.- Ingenieria
              3.- Diplomado
              '''))
if car==1:
   puntaje+=60
elif car==2:
   puntaje+=40
elif car==3:
   puntaje+=20
else:
   print("no es nuemro valido")

print( " El puntaje de beneficios es ", puntaje)