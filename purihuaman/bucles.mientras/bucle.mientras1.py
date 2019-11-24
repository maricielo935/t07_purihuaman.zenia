import os
#Declarar variables
nota_1,nota_2,nota_3,nota_4,promedio=0.0,0.0,0.0,0.0,0.0

#Pedir las variables via argumentos
nota_1=float(os.sys.argv[1])
nota_2=float(os.sys.argv[2])
nota_3=float(os.sys.argv[3])
nota_4=float(os.sys.argv[4])
promedio=(nota_1+nota_2+nota_3+nota_4)/4
promedio_invalido=(promedio>20 or promedio<0)

#While
while (promedio_invalido==True):
    nota_1=float(input("pedir la nota1:"))
    nota_2=float(input("pedir la nota2:"))
    nota_3=float(input("pedir la nota3:"))
    nota_4=float(input("pedir la nota4:"))
    promedio=(nota_1+nota_2+nota_3+nota_4)/4
    promedio_invalido=(promedio>20 or promedio<0)
#fin_del_while
print("Fin del bucle")
print("Promedio final:", promedio)

