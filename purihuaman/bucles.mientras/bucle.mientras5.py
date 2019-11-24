import os
#Declarar variables
peso_inicial,peso_final,reduccion_de_peso=0.0,0.0,0.0

#Pedir las variables via argumentos
peso_inicial=float(os.sys.argv[1])
peso_final=float(os.sys.argv[2])
reduccion_de_peso=(peso_inicial-peso_final)
reduccion_de_peso_invalido=(reduccion_de_peso==0 or reduccion_de_peso<5)
#While
while (reduccion_de_peso_invalido==True):
    peso_inicial=float(input("Cantida de peso al inicio:"))
    peso_final=float(input("Cantida de peso al final:"))
    reduccion_de_peso=(peso_inicial-peso_final)
    reduccion_de_peso_invalido=(reduccion_de_peso==0 or reduccion_de_peso<5)
#fin_del_while
print("Fin del bucle")
print("Reduccion de peso:",reduccion_de_peso)
