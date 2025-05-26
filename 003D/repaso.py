
total=0

while True:
   op=int(input('''
            Seleccione una comida
            1.- Pikachu Roll $4500
            2.- Otaku Roll $5000
            3.- Pulpo Venenoso Roll $5200
            4.- Anguila Eléctrica Roll $4800
            5.- Pagar 
            6.- Salir
            '''))
   match op:
      case 1:
         total+=4500
      case 2:
         total+=5000
      case 3:
         total+=5200
      case 4:
         total+=4800
      case 5:
         print("tiene codigo de descuento? 1.- si, 2.- no")
         desc=int(input())
         if desc==1:
            nu="2"
            while nu!="1":
                cod=input("ingres su codigo de desc")
                if cod =="soyotaku":
                  desc10=total*0.1
                  total=total-desc10
                  print("El Descuento es $",desc10)
                    
                else:
                  print("Codigo caducado o no valido")
                  nu=input("Dese intentar nuevamente?1.- si, 2.- no")
                  # if nu!="1": #            
         print(" EL total es $", total)
         print("Dese a comprar algo mas?")
         algomas=input("1.- si, 2.- no")
         if algomas=="2":
                break
      case 6:
         break
      case _:
         print("Opcion invalida")
   print(f"su total parcial es {total}")




