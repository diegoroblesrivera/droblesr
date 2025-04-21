#inicio de estudio con ciclo for

# #pide un numero al usuario y muestra esa cant de repeticiones
# num=int(input("Ingrese un numero ")) 


# for i in range(num):
#     print("Repeticion", i+1)

# # pide un numero al usuario y muestra la 
# # tabla de ese numero hasta el 10

# # Escribir i,"x", j, "=",i*j
# num=int(input("Ingrese un numero ")) 


# for i in range(10):
#     print( num , "x" , i+1, "=", (i+1)*num )

# #generacion automatica de las tablas del 1 al 10
# for j in range(10):
#     for i in range(10):
#         print( j+1 , "x" , i+1, "=", (i+1)*(j+1) )


# # pedir al suario la cantidad de notas 
# # y generar el promedio de estas

# cant=int(input("Ingrese el número de notas "))
# suma=0
# for i in range(cant):
#     print("Ingrese nota ", i+1)
#     nota=float(input())
#     suma+=nota
#     # suma=suma+nota
# prom=suma/cant
# print("El promedio es ", prom)

# pida la cant de alumnos y luego la cantidad de notas por alumno
# nuestra el promedio de cado uno

cantA=int(input("Ingrese el número de alumnos "))

for j in range(cantA):
    print("Ingrese el número de notas del alumno ", j+1)
    cantN=int(input())
    suma=0
    for i in range(cantN):
        print("Ingrese nota ", i+1, "del alumno ",j+1, "(use valores decimales)")
        nota=float(input())
        suma+=nota
        # suma=suma+nota
    prom=suma/cantN
    print("El promedio es ", prom)
    if prom>=4:
        print("Usted aprobó")
    else:
        print("Usted reprobó")