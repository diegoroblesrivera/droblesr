#Explicacion y uso de while
# 3344!=1234

# Clave con intentos infinitos
# clave=3344
# password=int(input("Ingrese su pass :"))
# while clave!=password:
#     print ("ERORR, clave invalida")
#     password=int(input("Ingrese su pass :"))

# print("Bienvenido al sistema")

##Clave con solo 3 intentos

# clave=3344
# intentos=1
# password=int(input("Ingrese su pass :"))
# while clave!=password and intentos<=3:
#     print ("ERORR, clave invalida")
#     intentos=intentos+1
#     print(intentos)
#     password=int(input("Ingrese su pass :"))

# if intentos>=3:
#     print("Ya no tiene ma intentos")
# else:
#     print("Bienvenido al sistema")

import random

# numAzar=random.randint(1,30)

# print(numAzar)

# # necesito al menos 20 puntos pra abrir la puerta

# if numAzar>=20:
#     print("Puede pasar")
# else:
#     print("LE falta puntaje")

# Gerenear un numero aleatoreo entre 1 y 50
# Pedir al usuario un numero
# Si ingresa un numero mayor  decirle, 
# " El numero a adivinar es menor".
# Si ingresa un numero menor  decirle,
#  " El numero a adivinar es mayor".
#EJ numeroAadivinar= 20 
# Si ingresa el 15 debe decir, " El numero a adivinar es mayor" .
# Si ingresa el 35 debe decir, " El numero a adivinar es menor" .


# numeroAadivinar=random.randint(1,50)

# num=int(input("Adivine el número"))

# while num!=numeroAadivinar:
#     print(numeroAadivinar)
#     if num>numeroAadivinar:
#         print("El numero a adivinar es menor")
#     else:
#         print("El numero a adivinar es mayor")
#     num=int(input("Adivine el número"))
# print("Le achuntaste!") 

# # Ruleta rusa

# barril=random.randint(1,6)
# rul=int(input("Dispare : "))

# while rul!=barril:
#     rul=int(input("Dispare"))
# print("BANG!!!")
    

# LUDO 

import time


# La Florida 20%, La pintana30%, Puente Alto25%, San Joaquin 15%
# Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%
# Preguntar al usuario en que comuna vive
# Preguntar al usuario con cuantas personas vive
# El arancel actual es de 200.000 por semestre
# Basados en las respuestas del usuario  y en 
# la informacion dada, calcular su descuento
'''
ej :
Ingrese su comuna : La FLorida
Ingrese su grupo familiar( numero entero usted incluido ) : 4
EL total del descuento es 23%
EL total a pagar es $154.000
'''


arancel=200000
descuento=0
print('''
    1.- La Florida 20%
    2.- La Pintana 30%
    3.- Puente Alto 25%
    4.- San Joaquin 15%
      ''')
comuna=int(input("Seleccione una comuna: "))

if comuna==1:
    descuento=20
elif comuna==2:
    descuento=30
elif comuna==3:
    descuento=25
elif comuna==4:
    descuento=15
else:
    print("Seleccion incorrecta")

grupo=int(input("Ingrese su grupo familiar( numero entero usted incluido ) :"))

if grupo==1:
    descuento+=2
elif grupo<=4 and grupo>=2:
    descuento+=3
elif grupo>=5:
    descuento+=4
else:
    print("Seleccion incorrecta")

print("El descuento total es ", descuento)
desc=arancel*descuento/100
total=arancel-desc
print("El total a pagar es $",total)

# # necesito al menos 20 puntos pra abrir la puerta


# puntos=random.randint(1,30)
# print(puntos)
# if puntos>=20:
#     print("Usd logró abrir la puerta")
# else:
#     print("Puntos insuficientes")