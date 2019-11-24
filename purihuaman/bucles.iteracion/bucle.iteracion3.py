#Sumar los O primeros numeros
import os
#Declaracion de variables
c=0
suma=0
z=int(os.sys.argv[1])
while(c<=z):
    print(c)
    suma += c
    c += 1
#fin_iteracion

print("La suma de los O primeros numeros es:", suma)
print("Fin del bucle")


