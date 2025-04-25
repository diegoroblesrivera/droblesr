# explicacion y uso de for

# for i in range(5):
#     print("hola")

# for i in range(1,6):
#     print(i)

# for i in range(5):
#     print(i+1)

# num=9

# for j in range(1, 51):
#     print(f"La tabla del {j}")
#     for i in range(1,11):
#         print(j ,"x", i ,"=",i*j)

# ## Preguntar la cantidad de notas y promediarlas

# cantN=int(input("Ingres la cantidad de notas"))
# suma=0
# for i in range(cantN):
#     print(f"Ingrese la nota numero {i+1}")
#     nota=float(input())
#     suma=suma+nota
# prom=suma/cantN

# print(f"El promedio es {prom} ")

# if prom >=4:
#     print("Usted aprobo")
# else:
#     print("Usted reprobo")


# # Preguntar al usuario cuantos productos llevará
# #  escribir listado de 3 productos y sus precios
# # mostrar el total neto de la compra
# #  y mostrar el total mas IVA (19%)

# cant=int(input("Ingrese la cantidad de productos"))
# total=0
# for i in range(cant):
#     print('''
#         Que producto llevará?
# 		1.- Diazepam $9000
# 		2.- Metametozona $18500
# 		3.- Oblea China $1000
#     ''')
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
#         print("Error, seleccione una opcion válida")

# print("EL total neto es ", total)
# print("EL total con IVA es ", total*1.19)

# VOTATOON
# Designe 2 cantdidatos. Pregunte cuanto votantes son
# por cada votante , debe peguntar por quin votrá
# cuente la cantidad de votos y muestre los resultados
# definir quien ganó la votacion. Considere empate

c1="Shaggy"
c2="Dexter"
cv1=0
cv2=0

cant=int(input("Ingres la cantidad de votantes"))

for i in range(cant):
    print(f"Seleccione a su candidato: 1.- {c1} , 2.- {c2}")
    voto=int(input)
    if voto==1:
        # cv1=cv1+1
        cv1+=1
    else:
        cv2+=1
print(f"La cantidad de votos de {c1} es {cv1}")
print(f"La cantidad de votos de {c2} es {cv2}")

if cv1>cv2:
    print(f"El ganador es {c1}")
elif cv1<cv2:
    print(f"El ganador es {c2}")
else:
    print("Empate")