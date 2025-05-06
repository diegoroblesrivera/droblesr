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
# Nacionalidad 
# Chilena : +300.000, Extranjero: +0

# '''desayuno'''
# import random
# import time


# pan=250

# while pan!=0:
#     print("ñam. le queda",pan, "grs de pan" )
#     pan-=50
#     time.sleep(2)

# chocolate=True

# if chocolate:
#     print("Puede comprar")
# else:
#     print("NO Puede comprar")

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


# pida al usuario 2 digitos verificando que
#  el segundo sea mayor
# Genere un numero aleatoreo entre esos digitos
# ► e imprima la candidad de veces el 
# simbolo  ▄ (alt+220)






import random
from random import randint
print("Ingrese 2 digitos")

n1=int(input("INgrese un numero"))
n2=int(input("INgrese un numero"))

while n1>n2:
   print("El segundo numero no puede ser menor")
   n2=int(input("Ingrese el numero 2 nuevamente"))
na=random.randint(n1,n2)
na=randint(n1,n2)
print("▄"*na)
