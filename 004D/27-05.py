# # repaso de menus

# while True:
#     try:
#         op=int(input('''
#                     Seleccione una opcion
#                     1.-
#                     2.-
#                     3.- Salir
#                     '''))
#         match op:
#             case 1:
#                 print("1")
#             case 2:
#                 print("2")
#             case 3:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("opcion invalida")
#     except Exception:
#         print("Solo numeros enteros")

usuario1=None
usuario2=None
usuario3=None
contrasena1= None
contrasena2=None
contrasena3= None

if usuario1==None and usuario2==None and usuario3==None:
    print("Debe tener al menos un usuario")
else:
    user=input("Ingrese su usuario")
    passw=input("Ingrese su contraseña")
    if (user==usuario1 and passw==contrasena1) or (user==usuario2 and passw==contrasena2) or (user==usuario3 and passw==contrasena3):
        op=int(input('''
                    1.- Realizar llamada
                    2.- Enviar correo
                    3.- Cerrar sesion
                    '''))