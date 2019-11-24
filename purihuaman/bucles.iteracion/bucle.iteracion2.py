#Sumar los N primeros numeros
import os
#Declaracion de variables
b=0
suma=0
z=int(os.sys.argv[1])
while(b<=z):
    print(b)
    suma += b
    b += 1
#fin_iteracion

print("La suma de los N primeros numeros es:", suma)
print("Fin del bucle")

