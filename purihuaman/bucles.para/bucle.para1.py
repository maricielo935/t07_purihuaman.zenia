import os
#Decodificar el siguiente mensaje encriptado
# M = Bienvenidos a Cineplanet
# N = Su compra online ha sido hecha
# O = Presentar su boleta en la sala 16
# P = Disfrute de su pelicula
MSG=os.sys.argv[1].upper()

for letra in MSG:
    if letra == "M":
        print("Bienvenidos a Cineplanet")
    if letra == "N":
        print("Su compra online ha sido hecha")
    if letra == "O":
        print("Presentar su boleta en la sala 16")
    if letra == "P":
        print("Disfrute de su pelicula")
#fin_para
print("Fin del bucle")


