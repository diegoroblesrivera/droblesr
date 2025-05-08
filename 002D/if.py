# Calcular el puntaje de credito
# De bede calcular que tanto credito tiene una persona
# en cierta entidad financiera, debera considerar
# cantidad de ingresos, nivel educacional y nacionalidad
# Cantidad de ingresos
# 500.000 a 1.000.000 : 300.000
# 1.000.001 a 1.500.000: 650.000
# 1.500.001 o mas : 1.000.000
# Nivel Educacional 
# Basico : x1, medio: x1.3 , superior: x1.5
# Nacionalidad 
# Chilena : +300.000, Extranjero: +0


# credito=0
# sueldo=int(input("INGRESE SU SUELDO"))
    
# if sueldo>=500000 and sueldo<=1000000:
#     credito+=300000
# elif sueldo>=1000001 and sueldo<=1500000:
#     credito+=650000
# elif sueldo>=1500001:
#     credito+=1000000
# else:
#     print("Usted es muy pobre")
# print(f"Su credito actual es {credito}")

# ed=int(input(''' Ingrese su nivel educacional
#             1.- Basico
#             2.-Medio
#             3.-Superior
#             '''))

# if ed==1:
#     credito*=1
# elif ed==2:
#     credito*=1.3
# elif ed==3:
#     credito*=1.5
# print(f"Su credito actual es {credito}")

# nacional=input("Ingrese su nacionalidad")

# if nacional.lower()=="chilena":
#     credito+=300000
# else:
#     print("No tiene bono por nacionalidad")

# print(f"Su credito final es {credito}")


# lavar loza
import time
import random
platos_sucios=5

# while platos_sucios!=0:
#     platos_sucios-=1
#     print("Usted ha lavado un plato, quedan", platos_sucios)
#     time.sleep(1)

# for i in range(platos_sucios,-1,-1):
#     print("Usted ha lavado un plato, quedan", i)
#     time.sleep(1)



# pida al usuario 2 digitos verificando que
#  el segundo sea mayor
# Genere un numero aleatoreo entre esos digitos
# ► e imprima la candidad de veces el 
# simbolo  ▄ (alt+220)
import random
from random import randint
# print("Ingrese 2 digitos")

# n1=int(input("Ingrese un numero"))
# n2=int(input("Ingrese un numero"))
# while n1>n2:
#    print("El segundo numero no puede ser menor")
#    n2=int(input("INgrese un numero"))

# numAzar=randint(n1,n2)
# numAzar=random.randint(n1,n2)
# print("▄"*numAzar)

# Crear un programa que pida la candidad de ramos
# Luego pida el promedio de cada materia
# basados en su promedio final, aplicar puntaje 
# de beneficios
# 4.5 y 5: 300, 5.1 y 6.0: 500, 6.1 y 7.0 : 800
# Agregar puntaje segun carrera
# Tecnico :+60, Ingenieria: +40, Diplomado: +20

