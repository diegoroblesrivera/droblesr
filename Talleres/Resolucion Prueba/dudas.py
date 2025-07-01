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

len(personas)
print(list(personas.keys())[-1])

# for i in personas.key():
#     print(i)

# for k, v in personas.items():
#     print(k, v)

v=7

def valora(v):
    if v>2:
        return True
    else:
        return False
    
def calcula_envio(valor, envi):
    lista=[]
    if valor <=10000:
        envi*=1.05
        lista.append(envi)
    elif valor>=10001 and valor<=50000:
        envi*=1.15
    else:
        envi*=1.25
    return lista

print(calcula_envio(20000, 9000))


