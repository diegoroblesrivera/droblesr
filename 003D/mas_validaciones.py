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

# recursion al usar una funcion que valida password
# El password debe tener una mayuscula
# una miniscula y un numero , ademas de tener
# largo exacto de 6 caracteres.

while True:
    pwd=input("Ingrese la clave: ")
    if valida_pass(pwd):
        print("clave Registrada")
        break
    else:
        print("Clave no registrada, intenta de nuevo")
