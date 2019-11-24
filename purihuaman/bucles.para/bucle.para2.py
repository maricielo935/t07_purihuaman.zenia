import os
#Decodificar el siguiente mensaje encriptado
# F = Muy buenos dias
# A = Mi nombre es Maricielo
# C = Tengo 17 anios
# F = Naci en Lima
# Y = Actualmente vivo en la ciudad de Lambayeque
# M = Y me gusta hacer deporte, gracias.
MSG=os.sys.argv[1].upper()

for letra in MSG:
    if letra == "F":
        print("Muy buenos dias")
    if letra == "A":
        print("Mi nombre es Maricielo")
    if letra == "C":
        print("Tengo 17 anios")
    if letra == "F":
        print("Naci en Lima")
    if letra == "Y":
        print("Actualmente vivo en la ciudad de Lambayeque")
    if letra == "M":
        print("Y me gusta hacer deporte, gracias.")
#fin_para
print("Fin del bucle")

