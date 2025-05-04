# print("Repaso General")

#####LINK DEL TALLER#####
#https://github.com/diegoroblesrivera/droblesr

## Declaracion de variables
# nombre="Diego"
# edad=64

## concatenacion
# print("hola", nombre, "su edad es", edad)
# print(f"hola {nombre} y su edad es {edad}")

## Solicitud de variables
# nombre=input("Ingrese su nombre: ")
# edad=int(input("Ingrese su edad"))


# print(f"hola {nombre} y su edad es {edad}")


# #suma de 2 numeros
# print("ingrese 2 numeros")
# n1=int(input())
# n2=int(input())

# print("La suma de los numeros es", n1+n2)

# explicacion y usa de for

# for i in range(3):
#     print(i+1)
    
# for i in range(3):
#     print("Repeticion",i+1)

# # pedir al suario la cantidad de notas 
# # y generar el promedio de estas

# cant=int(input("Ingrese el número de notas "))
# suma=0
# for i in range(cant):
#     print("Ingrese nota ", i+1)
#     nota=float(input())
#     suma+=nota # suma el valor de nota a la variable suma
#     # suma=suma+nota # tae el valor actual de suma y le suma la nota, actualizando suma
# prom=suma/cant
# print("El promedio es ", round(prom,1))


# Explicacion y uso de librerias

import random
from random import  randint
import time

# num1=random.randint(1,6)
# num2=randint(1,6)
# print(num1,num2)

# for i in range(3):
#     time.sleep(1)
#     print(i+1)

# Explicacion y uso de while
# = es asignacion , vale decir, asigna un valor a un avariable. EJ: numero=19
# == es comparacion, en otras palabras, comparo 2 valores EJ: numero==9

# num=0

# while num<5:
#     print("Hola")
#     num+=1

# # Clave con intentos infinitos
# clave=4455
# # 1234
# # 4455!=1234 //SI, por lo tanto, esta afirmacion es verdadera osea True.
# password=int(input("Ingrese su pssword: "))
# while clave!=password:
#     print("ERROR; intente nuevamente")
#     password=int(input("Ingrese su pssword: "))
# print("Bienvenido al sistema")

# #Clave con solo 3 intentos
# clave=3344
# intentos=3
# password=int(input("Ingres su clave : "))

# while clave!=password or intentos==0:
#     intentos-=1
#     print(f"ERROR, le quedan {intentos} intentos")
#     password=int(input("Ingres su clave : "))
#     if intentos<=1:
#         break
        
    
# if intentos!=0 and clave==password:
#     print("Usted ingresó al sistema")
# else:
#     print("Sistema bloqueado")

# #cerrar as ventanas por la cantidad de eventanas en casa
# num=int(input("Cuentas ventnas tiene: "))

# for i in range(num):
#     print("Cierra la ventana")
    
    
# # Recorrar las letras de una frase con un for
# frase=input("Ingrese una frase")

# for i in frase:
#     print(i)

# Contar los autos que llegan al estacionamiento
# rojos, azules y otro color

# rojos=0
# azules=0
# otro=0
# color=0

# while color!=4:

#     color=int(input('''
#                     Ingrese el color del auto
#                     1.- Rojo
#                     2.- Azul
#                     3.- Otro
#                     4.- Salir
#                     '''))
#     if color==1:
#         print("El color es rojo")
#         rojos+=1
#     elif color==2:
#         print("El color es azul")
#         azules+=1
#     elif color==3:
#         print("El color es azul")
#         otro+=1
#     else:
#         print("Saliendo")
        
# print("Los autos de color rojo son", rojos)
# print("Los autos de color azul son", azules)
# print("Los autos de otro color son", otro)




# Categorizar jugadores 
# En una liga amateour, se paga a lo jugadores de futbol
# Cuando anota mas goles recibe un bono en su paga
# Entre 1-3 goles, 4%; entre 4-6 goles 6%, 7 goles o mas 8%
# Si su equipo queda entre los 3 primeros, +3000 
# Si su equipo queda entre 4-8, +2000 
# Si su equipo queda entre 9 y mas, +1000 
# El pago base por jugador es de 5000

# goles=randint(1,10)
# print("Los goles anotados en la temporada fueron", goles)
# time.sleep(1)
# pos=randint(1,16)
# print("La posicion final en la temporada fue", pos)
# time.sleep(1)
# # goles=int(input("Cuantos goles anotó?"))
# sueldo=5000

# if goles>=1 and goles<=3:
#     sueldo=sueldo*1.04
# elif goles>=4 and goles<=6:
#     sueldo=sueldo*1.06
# else:
#     sueldo=sueldo*1.08
# print("El sueldo aumentado es", sueldo)
# if pos>=1 and pos<=3:
#     sueldo+=3000
# elif pos>=4 and pos<=8:
#     sueldo+=2000
# else:
#     sueldo+=1000
# print("El total del sueldo del jugador al final de temporada es", sueldo)



# Calcular el araccel a pagar segun grupo familiar y comuna en la que reside
# A continuacion , los descuentos por cumuna:
# La Florida 20%, La pintana 30%, Puente Alto 25%, San Joaquin 15%
# Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%
# Preguntar al usuario en que comuna vive
# Preguntar al usuario con cuantas personas vive
# El arancel actual es de 200.000 por semestre
# Basados en las respuestas del usuario  y en 
# la informacion dada, calcular su descuento
'''
ej :
Ingrese su comuna : La Florida
Ingrese su grupo familiar( numero entero usted incluido ) : 4
EL total del descuento es 23%
EL total a pagar es $154.000
'''

# arancel=200000
# descuento=0
# print('''
#     1.- La Florida 20%
#     2.- La Pintana 30%
#     3.- Puente Alto 25%
#     4.- San Joaquin 15%
#       ''')
# comuna=int(input("Seleccione una comuna: "))

# if comuna==1:
#     descuento=20
# elif comuna==2:
#     descuento=30
# elif comuna==3:
#     descuento=25
# elif comuna==4:
#     descuento=15
# else:
#     print("Seleccion incorrecta")

# grupo=int(input("Ingrese su grupo familiar( numero entero usted incluido ) :"))

# if grupo==1:
#     descuento+=2
# elif grupo<=4 and grupo>=2:
#     descuento+=3
# elif grupo>=5:
#     descuento+=4
# else:
#     print("Seleccion incorrecta")

# print("El descuento total es ", descuento)
# desc=arancel*descuento/100
# total=arancel-desc
# print("El total a pagar es $",total)


###PROGRAMA EN PSINT#####
'''
Algoritmo adivina_numero
	Definir num_adivinar, intentos, num Como Entero
	//dado=Aleatorio(1,50)
	//Escribir dado
	num_adivinar=Aleatorio(1,50)
	intentos=6
	Repetir
		Escribir num_adivinar
		Escribir "Ingrese el numero a adividar"
		Leer num
		Si num>num_adivinar Entonces
			Escribir "Usted se pas�"
		SiNo
			Escribir "El numero es mayor"
		Fin Si
		c=c+1
	Hasta Que num==num_adivinar o c==intentos
	Si num==num_adivinar Entonces
		Escribir "Felicidades "
	SiNo
		Escribir "Se le acabaron los intentos"
	Fin Si
	
FinAlgoritmo
'''

###TRASPASO A PYTHON####

# num_adivinar=randint(1,50)
# intentos=6
# # num=int(input("Ingrese el numero a adividar"))
# num=0
# c=0
# while num!=num_adivinar and c<=intentos:
#     print(num_adivinar)
#     num=int(input("Ingrese el numero a adividar"))
#     if num>num_adivinar:
#         print("El numero a adivinar es menor")
#     else:
#         print("El numero a adivinar es mayor")
#     c+=1
# if num==num_adivinar:
#     print("Adivinó!!")
# else:
#     print("NO Adivinó!!")