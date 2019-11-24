import os
#Decodificar el siguiente mensaje encriptado
# J = Hola profesor
# A = Feliz cumpleanios
# S = Espero la pase con su familia y amigos
# M = Bendiciones
MSG=os.sys.argv[1].upper()

for letra in MSG:
    if letra == "J":
        print("Hola profesor")
    if letra == "A":
        print("Feliz cumpleanios")
    if letra == "S":
        print("Espero la pase con su familia y amigos")
    if letra == "M":
        print("Bendiciones")
#fin_para
print("Fin del bucle")
