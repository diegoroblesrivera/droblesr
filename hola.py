###TIPOS DE DATOS###
'''
Caracter : String # Variables tipo texto EJ: "Mariano"
Entero  : Integer (int) # Variable tipo numero entero EJ: 18
Real    : float # numeros con decimas 
Logico  : boolean # permite solo 2 valora, posibles True o False

'''


# nombre="Diego"
# edad=64

# print("hola", nombre, "su edad es", edad)
# print(f"hola {nombre} y su edad es {edad}")

# # solicitud de datos
# print("Ingrese su nombre")
# nombre=input()
# print("Ingrese su edad")
# edad=input()
# # Ejemplo de concatenacion
# print("hola", nombre, "su edad es", edad)

# #suma de 2 numeros
# print("ingrese 2 numeros")
# n1=int(input())
# n2=int(input())

# print("La suma de los numeros es", n1+n2)

# #ingresar 3 numeros y sacar el promedio
# print("ingrese 2 numeros")
# n1=int(input())
# n2=int(input())
# n3=int(input())
# prom=(n1+n2+n3)/3
# print("El promedio  es", prom )

# if prom>=40:
#     print("el alumno aprobó")    
# else:
#     print("el alumno reprobó")

#pedir edad al usuario y determinar si es mayor de edad

# edad=int(input("Ingrese su edad "))

# if edad>=18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted NO es mayor de edad")


# # mostrar segun criterio
# # menos de 12 años es niños
# # entre 12 y 17 es adolescente
# # entre 18 y 64 es adulto
# # 65 y mas , es adulto mayor
# edad=int(input("Ingrese su edad "))

# if edad<12:
#     print("Usted es un niño")
# elif edad>=12 and edad<18:          # else if
#     print("Usted es adolescente")
# elif edad>=18 and edad<65: 
#     print("Usted es adulto")
# else:
#     print("Usted es un tatita")

# #ingresar 3 numeros y mostrar el mayor de los 3
# print("Ingrese 3 numeros")
# n1=int(input())
# n2=int(input())
# n3=int(input())

# if n1>n2 and n1>n3:
#     print("El mayor es el numero " , n1)
# elif n2>n3:
#     print("El mayor es el numero " , n2)
# else:
#     print("El mayor es el numero " , n3)


# #programa de clave
# clave=3344

# pas=int(input("Ingrese su clave "))

# if pas==clave:
#     print("Bienvenido al sistema")
# else:
#     print("Clave invalida")


# cant=int(input("Ingrese la cant de  numeros :"))

# for i in range(cant):
#     num=int(input("Ingrese un numero :"))
#     if num %2==0:
#         print("El numero es par ")
#     else:
#         print("El numero es impar ")

# Pedir u numero y mostrear todos los 
# pares e impares desde el 1 hasta ese numero

# num=int(input("Ingrese un numero :"))

# # for i in range(num):
# #     if (i+1) %2==0:
# #         print(f"El numero {i+1} es par ")
# #     else:
# #         print(f"El numero {i+1} es impar ")

# for i in range(1,num+1):
#     if (i) %2==0:
#         print(f"El numero {i} es par ")
#     else:
#         print(f"El numero {i} es impar ")


## Ingresar 3 numeros y ver el mayor de ellos

# n1=int(input("ingrese un numero :"))
# n2=int(input("ingrese un numero :"))
# n3=int(input("ingrese un numero :"))

# m= max(n1,n2,n3)
# print(f" El mayor es {m}")

# if n1>n2 and n1>n3:
#     print(f"El numero mayor es {n1}")
#     # print("El numero mayor es", n1)
# elif n2>n3:
#     print(f"El numero mayor es {n2}")
# else:
#     print(f"El numero mayor es {n3}")



# ## Ingresar 3 numero y promediarlos

# n1=int(input("ingrese un numero :"))
# n2=int(input("ingrese un numero :"))
# n3=int(input("ingrese un numero :"))

# prom=(n1+n2+n3)/3

# print("El promedio es ", round( prom, 2))


# ## pares impares
# n1=int(input("ingrese un numero :"))

# if n1 %2==0:
#     print(f"El numero {n1} es par ")
# else:
#     print(f"El numero {n1} es impar ")

