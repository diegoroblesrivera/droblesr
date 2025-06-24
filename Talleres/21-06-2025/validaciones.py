# valicaciones de datos

# email=input("Ingrese su email: ")

#verifico si el caracter @ existe en mi variable

# if "@" in email:
#     print("La variable tiene formato mail")
# else:
#     print("La variable NO tiene formato mail")

#validar una clave solo de nuemros enteros
# while True:
#     try:
#         clave=int(input("Ingrese su clave"))
#         break
#     except Exception:
#         print("Error, solo ingrese numeros")

# validar una clave por su largo , por lo menos 5
# clave=input("Ingrese su clave: ")

# verifico que tenga al menos 5 caracteres
# la funcion len() verifica el largo de un objeto
# en este caso la variabble clave    
# if len(clave)>=5:
#     print("La clave tiene el largo correcto")
# else:
#     print("La clave debe tener el menos 5 caracteres")

# ahora verifica que tenga al menos 5 y menor o igual a 12
# if len(clave)>=5 and len(clave)<=12:
#     print("La clave tiene el largo correcto")
# else:
#     print("La clave debe tener el menos 5 caracteres y menos de 12")
  
# verifico si tengo mayusclas y/o minisculas
# y tiene por lo menos un numero

# tieneMayus=False
# tieneMinus=False
# tieneNumero=False

# #hacemos un recorrido de cada letra en mi clave
# for letra in clave:
#     # verifico si la letra es mayuscula
#     if letra.isupper():
#         tieneMayus=True
#     # verifico que la letra es minuscula
#     if letra.islower():
#         tieneMinus=True
#     # verifico si tiene por lo meno un numero
#     if letra.isdigit():
#         tieneNumero=True
        
        
# if tieneMayus:
#     print("Tiene por lo menos una mayuscula")
# else:
#     print("NO Tiene por lo menos una mayuscula")
# if tieneMinus:
#     print("Tiene por lo menos una minuscula")
# else:
#     print("NO Tiene por lo menos una miniscula")
# if tieneNumero:
#     print("Tiene por lo menos un numero")
# else:
#     print("NO Tiene por lo menos un numero")

# if tieneMayus and tieneMinus and tieneNumero:
#     print("La clave esta ok")
# else:
#     print("Debe intentar nuevamente")

# specials="!#$%&/()=?*{}[]"
# clave="visa#"

# for caracter in clave:
#     if caracter in specials:
#         print("Si es un cracter especial")
  
     
def valida_pass(clave):
    Mayuscula=False
    Minuscula=False
    Numero=False
    for palabra in clave:
        if palabra.isupper():
            Mayuscula=True
        if palabra.islower():
            Minuscula=True
        if palabra.isdigit():
            Numero=True
    if Mayuscula and Minuscula and Numero and len(clave)==6:
        # print("la clave está bien escrita")
        return True
    else:
        # print("la clave está mal escrita")
        return False

# print(valida_pass("Tredf9"))

# while True:
#     pwd=input("Ingrese la clave: ")
#     if valida_pass(pwd):
#         print("clave Registrada")
#         break
#     else:
#         print("Clave no registrada, intenta de nuevo")

# clave="tingo*#"
# grupo="!#$%&*¨[]"
# for c in grupo:
#     if c in clave:
#         print("Si existe")
#     else:
#         print("NO existe")




