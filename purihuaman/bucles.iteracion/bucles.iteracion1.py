#Sumar los M primeros numeros
import os
#Declaracion de variables
a=0
suma=0
x=int(os.sys.argv[1])
while(a<=x):
    print(a)
    suma += a
    a += 1
#fin_iteracion

print("La suma de los M primeros numeros es:", suma)
print("Fin del bucle")
