import os
#Decodificar el siguiente mensaje encriptado
# J = Las estrucuturas de control
# F = Sirven para muchas cosas
# M = Entre ellas:
# A = Permiten que un algoritmo tome decisiones
# K = Permiten que un algoritmo repita instrucciones
# V = Permiten alterar el flujo de control del algoritmo
# P =Asi de importante son las estrcuturas de control en algoritmos
MSG=os.sys.argv[1].upper()

for letra in MSG:
    if letra == "J":
        print("Las estrucuturas de control")
    if letra == "F":
        print("Sirven para muchas cosas")
    if letra == "M":
        print("Entre ellas:")
    if letra == "A":
        print("Permiten que un algoritmo tome decisiones")
    if letra == "K":
        print("Permiten que un algoritmo repita instrucciones")
    if letra == "V":
        print("Permiten alterar el flujo de control del algoritmo")
    if letra == "P":
        print("Asi de importante son las estrcuturas de control en algoritmos")
#fin_para
print("Fin del bucle")

