#Explicacion y uso de while
import time


# num=10

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


suma=0
while True:
    num=int(input("Ingrese un numero , cero para salir :"))
    if num==0:
        break
    suma+=num
    print(suma)
print(F"La suma total es {suma}")


