#Sumar los Q primeros numeros
import os
#Declaracion de variables
e=0
suma=0
v=int(os.sys.argv[1])
while(e<=v):
    print(e)
    suma += e
    e += 1
#fin_iteracion

print("La suma de los Q primeros numeros es:", suma)
print("Fin del bucle")

