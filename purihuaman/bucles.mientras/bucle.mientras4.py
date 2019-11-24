import os
#Declarar variables
angulo1,angulo2,angulo3,angulo4,suma_angulos_internos=0,0,0,0,0

#Pedir las variables via argumentos
angulo1=int(os.sys.argv[1])
angulo2=int(os.sys.argv[2])
angulo3=int(os.sys.argv[3])
angulo4=int(os.sys.argv[4])
suma_angulos_internos=(angulo1+angulo2+angulo3+angulo4)
suma_invalida=(suma_angulos_internos<360 or suma_angulos_internos==0)

#While
while (suma_invalida==True):
    angulo1=int(input("Medida del primer angulo:"))
    angulo2=int(input("Medida del segundo angulo:"))
    angulo3=int(input("Medida del tercer angulo:"))
    angulo4=int(input("Medida del cuarto angulo:"))
    suma_angulos_internos=(angulo1+angulo2+angulo3+angulo4)
    suma_invalida=(suma_angulos_internos<360 or suma_angulos_internos==0)
#fin_del_while
print("Fin del bucle")
print("Suma de los angulos interiores:",suma_angulos_internos)

