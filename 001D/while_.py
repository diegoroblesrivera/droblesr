#Explicacion y uso de while
import time


num=10

# while num<5:
#     print("HOLa")
#     num+=1

# while  num>0:
#     print(num)
#     time.sleep(1)
#     num-=1

# clave=3344
# intentos=3
# password=int(input("Ingres su clave :"))

# while clave!=password or intentos==0:
#     intentos-=1
#     print(f"ERROR, le quedan {intentos} intentos")
#     password=int(input("Ingres su clave :"))
#     if intentos<=1:
#         break
        
    
# if intentos!=0 and clave==password:
#     print("Usted ingresó al sistema")
# else:
#     print("Sistema bloqueado")


# Pedir al usuario  numeros que se vayan sumando
# y mostrar al final la suma de todos
# Salir del programa al poner un cero(0)

# while True:
#     print("hello")

# suma=0
# while True:
#     num=int(input("Ingrese un numero , cero para salir :"))
#     if num==0:
#         break
#     suma+=num
#     print(suma)
# print(f"La suma total es {suma}")

# pida al usuario el limite inferior y superior de un rango
# Despues genere un numero al azar dentro de ese rango
# el segundo numero, no  debe ser menor qu el primero
# pero debe darle la oportunidades infinitas
# al usuario de ingresar otro

import random

# print("Ingrese dos numeros")
# n1=int(input("Ingrese el primer numero"))
# n2=int(input("Ingrese otro numero mayor que el anterior"))

# while n2<=n1:
#     print("El numero debe ser mayor al anterior")
#     n2=int(input("Ingrese otro numero mayor que el anterior"))

# numram=random.randint(n1,n2)

# print(numram)


# numram=random.randint(1,50)

# print("Adivine el numero entre 1 y 50")
# intentos=5
# num=int(input())

# while numram!=num:
#     intentos-=1
#     if intentos==0:
#         break
#     if num>numram:
#         print("El numero a adivinar es menor")
#     else:
#         print("El numero a adivinar es mayor")
#     print(f"te quedan {intentos} intentos")
#     num=int(input())

# if intentos==0:
#     print("Perdiste")
# else:
#     print("SOS UN GENIO, ADIVINASTE EL NUMERO")

# STREET FIGTHER #

# Designe 2 peleadores solicitando sus nombres
# cada peleador tiene 50 HP, debe mostrar la 
# barra de energia. Las peleas son por turnos
# cada turno el peleador ataca entre 3 y 15
# Existe posibilidad de ataque critico del 20% sera atk*2
# gana el que le quita todo el HP al rival

print("Ingrese los nombres de los peleadores")
p1=input("Peleador 1")
p2=input("Peleador 2")
hp1=50
hp2=50
turno=random.randint(1,2)

while hp1>0 and hp2>0 : 
    if turno %2==0:
        print("turno de ",p1)
        atk=random.randint(3,15)
        critical=random.randint(1,5)
        if critical==3:
            atk*2
            print("Ataque critico")
        hp2-=atk
        time.sleep(1)
        print(f"Vida de {p2}")
        print("[]"*hp2)
    else:
        print("turno de ",p2)
        atk=random.randint(3,15)
        critical=random.randint(1,5)
        if critical==3:
            atk*2
            print("Ataque critico")
        hp1-=atk
        time.sleep(1)
        print(f"Vida de {p1}")
        print("[]"*hp1)
    turno+=1

ultra=random.randint(3,10)

if hp1>hp2:
    for i in range(ultra):
        print("Kick")
        time.sleep(1)
    print(f"Ha ganado el {p1}")
    print("UTRAAAAAAAAAA!")
else:
    for i in range(ultra):
        print("Kick")
        time.sleep(1)
    print(f"Ha ganado el {p2}")
    print("UTRAAAAAAAAAA!")
    


# while True:
#     print('''
#           1.-
#           2.-
#           3.-salir

#           ''')
#     op=int(input("Selecciones una opcion"))
#     if op==1:
#         print("Opcion 1 ")
#     elif op==2:
#         print("Opcion 2 ")
#     elif op==3:
#         print("Opcion salir ")
#         break
#     else:
#         print("Seleccione una opcion válida")

# Crear un cajero automatico
# Tener en cuenta cajas de billetes de 5000 , 10000 y 20000
# Cada caja tine 30 billetes. Verificar si el monto solicitado
# Esta disponible en el cajero.Verificar si el monto solicidado
# es posible por el multiplo de los billetes disponibles
# Al terminar cada transaccion, debe mostrar saldo Disponible
# Debe haber 3 usuarios cada uno son su saldo correspondiente
# Usar clave secreta para iniciar y segun la clave 
# asociar el saldo disponible

# intentos=3

# while intentos>0:
#     intentos-=1
#     color=input("Ingrese un color: ")

#     if color.lower()!="negro":
#         print("El color  no es el requerido")
#     else:
#         print("Éste es el color requerido")
#         break
    

# La Florida 20%, La pintana30%, Puente Alto25%, San Joaquin 15%
# Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%
# Preguntar al usuario en que comuna vive
# Preguntar al usuario con cuantas personas vive
# El arancel actual es de 200.000 por semestre
# Basados en las respuestas del usuario  y ebn 
# la informacion dada, calcular su descuento
'''
ej :
Ingrese su comuna : La FLorida
Ingrese su grupo familiar( numero entero) : 4
EL total del descuento es 23%
EL total a pagar es $154.000
'''

# Clasificar segun categoria y precio
# Cat 1 +200, cat 2 +400, cat 3 +600
# Decuento Precios : 1000 y menos;3%, entre 1001 y 5000 
# ;5% , 5001 y mas 6%
# Poner listado de 3 productos por categoria, las cat son 1 ,2 y 3
# Agregar los impuestos al ´precio , segun la cat y luego 
# aplicar descuento al total de la boleta segun el monto
'''
Ej:
Producto 1, cat 2, 1500 + 400
Producto 2 cat 1, 8000 + 200
EL total es 10100 * - 6%
EL total a pagar es: 9494
'''
# total=0
# print('''
#     Selecione una categoria
#       1.- Zpatillas
#       2.- Poleras
#       3.- Pelotas
#       ''')
# cat=int(input())

# if cat==1:
#     print('''
#         1.- Zapatilla runing 2000
#         2.- Zapatilla Futbolito 1500
#         3.- Zapatilla Padel 20      
#           ''')
#     op=int(input())
#     if op==1:
#         total+=2000+200
#     elif op==2:
#         total+=1500+200
#     elif op==3:
#         total+=20+200
#     else:
#         print("Opcion invalida")
# elif cat==2:
#     print('''
#         1.- Polera Runing 3000
#         2.- Camiseta Futbolito 1500
#         3.- Polera Padel 60      
#           ''')
#     op=int(input())
#     if op==1:
#         total+=3000+400
#     elif op==2:
#         total+=1500+400
#     elif op==3:
#         total+=60+400
#     else:
#         print("Opcion invalida")
# elif cat==3:
#     print('''
#         1.- Pelota Voley 1000
#         2.- Pelota Futbolito 2500
#         3.- Pelota Rugby 3500     
#           ''')
#     op=int(input())
#     if op==1:
#         total+=1000+600
#     elif op==2:
#         total+=2500+600
#     elif op==3:
#         total+=3500+600
#     else:
#         print("Opcion invalida")
# else:
#     print("Opcion invalida")

# if total<=1000:
#     total= total*0.97
# elif total<=1001 and total>=5000:
#     total= total*0.95
# elif total>=5001:
#     total= total*0.94

# print(" EL total es ", total)
