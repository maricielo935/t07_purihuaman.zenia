#Sumar los P primeros numeros
import os
#Declaracion de variables
d=0
suma=0
w=int(os.sys.argv[1])
while(d<=w):
    print(d)
    suma += d
    d += 1
#fin_iteracion

print("La suma de los P primeros numeros es:", suma)
print("Fin del bucle")
