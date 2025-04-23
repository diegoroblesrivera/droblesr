#Explicacion y uso de while


# # Clave con intentos infinitos
# clave=3344
# password=int(input("Ingrese su pass :"))
# while clave!=password:
#     print ("ERORR, clave invalida")
#     password=int(input("Ingrese su pass :"))

# print("Bienvenido al sistema")

##Clave con solo 3 intentos

clave=3344
intentos=1
password=int(input("Ingrese su pass :"))
while clave!=password and intentos<=3:
    print ("ERORR, clave invalida")
    intentos=intentos+1
    print(intentos)
    password=int(input("Ingrese su pass :"))

if intentos>=3:
    print("Ya no tiene ma intentos")
else:
    print("Bienvenido al sistema")