#use y explicacion de while
# num=0

# while num<=5:
#     print(num)
#     num+=1
# import time
# num= 10

# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

# resp="no"

# while resp!="si":
#     resp=input("Desea Salir del sistema? :")

clave=3344

contraseña=int(input("Ingrese su contraseña"))

while clave!=contraseña:
    print("ERROR; clave invalida")
    contraseña=int(input("Ingrese su contraseña"))
print(" Clave aceptada")
