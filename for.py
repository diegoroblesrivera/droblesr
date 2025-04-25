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

# # pida la cant de alumnos y luego la cantidad de notas por alumno
# # nuestra el promedio de cado uno

# cantA=int(input("Ingrese el número de alumnos "))

# for j in range(cantA):
#     print("Ingrese el número de notas del alumno ", j+1)
#     cantN=int(input())
#     suma=0
#     for i in range(cantN):
#         print("Ingrese nota ", i+1, "del alumno ",j+1, "(use valores decimales)")
#         nota=float(input())
#         suma+=nota
#         # suma=suma+nota
#     prom=suma/cantN
#     print("El promedio es ", prom)
#     if prom>=4:
#         print("Usted aprobó")
#     else:
#         print("Usted reprobó")


# # Definir 2 candidatos. Preguntar la cantidad de votantes
# # Preguntar a cada votante por quien votará mostrando 
# # las alternativas. Contar los votos y mostrar resultados.
# # Definir el ganador y considerar un empate.

# c1="Aqua"
# c2="KOKU"
# cv1=0
# cv2=0

# cantV=int(input("Cuantos votantes son? :"))

# for i in range(cantV):
#     print(f"por quien votará? 1.- {c1}, 2.- {c2}")
#     voto=int(input())
#     if voto==1:
#         cv1=cv1+1
#         # cv1+=1
#     else:
#         cv2=cv2+1
# print(f"La cantidad de votos de {c1} es {cv1}")
# print(f"La cantidad de votos de {c2} es {cv2}")
# if cv1>cv2:
#     print(f"Ganó {c1}")
# elif cv1<cv2:
#     print(f"Ganó {c2}")
# else:
#     print("Es un empate!")

# frase=input("Ingrese una frase :")
# c=0
# cons=0
# v=0
# espacio=" "
# for i in frase:
#     # print(i)
#     if i.lower() in "aeiou":
#         v=v+1
#     elif i.lower() ==" ":
#         cons=cons+1
#     else:
        
#     c=c+1
# print("La cantidad de vocales es", v)
# print("La cantidad de consonantes es", cons)
# print("La cantidad de caracteres es", c)


## SUPERMERCADO 
# Preguntar al usuario cunatos productos llevra.´
# escribir listado de 3 productos y sus precios
# mostrar el total neto de la compra
# y mostrar el total mas IVA (19%)

# cant=int(input("Cuantos productos llevará? :"))
# total=0
# for i in range(cant):
#     print('''
#         Que producto llevará?
# 	    1.- Diazepam $9000
# 	    2.- Metametozona $18500
# 	    3.- Oblea China $1000
#         ''')
#     op=int(input())
#     if op==1:
#         print("Usted lleva Diazepam")
#         total=total+9000
#     elif op==2:
#         print("Usted lleva Metametozona")
#         total=total+18500
#     elif op==3:
#         print("Usted lleva Oblea China")
#         total=total+1000
#     else:
#         print("Seleccione suna opcion valida")

# print ("EL total neto es ", total)
# print ("EL total mas IVA es ", total*1.19)

# variable=input()

# frase=input("Ingrese una frase")
# cantcar=0
# v=0
# cons=0
# e=0
# for i in frase:
#     print(i)
#     cantcar+=1
#     if i.lower() in "aeiouáéíóú":
#         v+=1
#         # v=v+1
#     elif i==" ":
#         e+=1
#     else:
#         cons+=1 
    




# print(f"El total de caracteres es {cantcar}")
# print(f"El total de vocales es {v}")
# print(f"El total de consonantes es {cons}")



# Preguntar al usuario cuantos productos llevará
# escribir listado de 3 productos y sus precios
# mostrar el total neto de la compra
# y mostrar el total mas IVA (19%)


cant=int(input("Cuantos productos llevará"))
total=0
for i in range (cant):
        print('''
        Que producto llevará?
		1.- Diazepam $9000
		2.- Metametozona $18500
		3.- Oblea China $1000 ''')
        op=int(input())
        if op==1:
            print("Usted lleva Diazepam")
            total=total+9000
        elif op==2:
            print("Usted lleva Metametozona")
            total=total+18500
        elif op==3:
            print("Usted lleva Oblea China")
            total=total+1000
        else:
             print("Opcion no valida")
print("EL total neto es ", total)
print("EL total mas IVA es ", total*1.19)

            
        
	    






