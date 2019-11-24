import os
#Decodificar el siguiente mensaje encriptado
# D = Jeimmar Spa
# J = Ubicado en Lambayeque
# F = En la calle Andres Avelivo Caceres
# A = Y se ofrecen los siguientes servicios:
# K = Masajes relajantes
# V = Masajes descontracturantes
# P = Reduccion de medidas para hombres y mujeres
# O = Los esperamos!
MSG=os.sys.argv[1].upper()

for letra in MSG:
    if letra == "D":
        print("Jeimmar Spa")
    if letra == "J":
        print("Ubicado en Lambayeque")
    if letra == "F":
        print("En la calle Andres Avelivo Caceres")
    if letra == "A":
        print("Y se ofrecen los siguientes servicios:")
    if letra == "K":
        print("Masajes relajantes")
    if letra == "V":
        print("Masajes descontracturantes")
    if letra == "P":
        print("Reduccion de medidas para hombres y mujeres")
    if letra == "O":
        print("Los esperamos!")
#fin_para
print("Fin del bucle")
