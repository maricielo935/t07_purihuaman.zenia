import os
#Declarar variables
base,altura,area=0,0,0

#Pedir las variables via argumentos
base=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
area=base*altura
area_invalida=(area>200 or area==100)

#While
while (area_invalida==True):
    base=int(input("Pedir la base:"))
    altura=int(input("Pedir la altura:"))
    area=base*altura
    area_invalida=(area>200 or area==100)
#fin_del_while
print("Fin del bucle")
print("Area:", area)
