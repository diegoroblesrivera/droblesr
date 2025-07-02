personas={
    1:{"nombre": "luka",
       "tipo_entrada": "V",
       "codigo": "G1ght"},
    2:{"nombre": "Alan Grant",
    "tipo_entrada": "V",
    "codigo": "hhYY6743"},
    3:{"nombre": "Jhan Hamon",
    "tipo_entrada": "G",
    "codigo": "Guu778"},
}

# len(personas)
# print(list(personas.keys())[-1])

# for i in personas.key():
#     print(i)

# for k, v in personas.items():
#     print(k, v)

# v=7

# def valora(v):
#     if v>2:
#         return True
#     else:
#         return False
    
# def calcula_envio(valor, envi):
#     lista=[]
#     if valor <=10000:
#         envi*=1.05
#         lista.append(envi)
#     elif valor>=10001 and valor<=50000:
#         envi*=1.15
#     else:
#         envi*=1.25
#     return lista

# print(calcula_envio(20000, 9000))

famosos=["Michael Jackson", "50 Cent", "James Dio"]

def mostrar(lista):
    for n,i in enumerate(lista):
        print(n+1,i)


while True:
        print('''

              1.- Agregar Cantante .
              2.- Mostrar cantantes
              3.- Buscar cantante
              4.- Borrar cantante
              5.- Salir
        ''')
        op=int(input())
        match op:
            case 1:
                nombre=input("Ingrese el nombre del cantante")
                famosos.append(nombre)            
            case 2:
                mostrar(famosos)
            case 3:
                buscar=input("Ingrese el nombre del cantante a buscar")
                if buscar in famosos:
                    print(f"El nombre {buscar} está en la lista")
                else:
                    print(f"El nombre {buscar} NO está en la lista")
            case 4:
                mostrar(famosos)
                buscar=int(input("Ingrese el nombre del cantante a borrar"))
                famosos.pop(buscar-1)
            case 5:
                ("saliendo")
                break
            case _:
                print("escoga una opción valida")


