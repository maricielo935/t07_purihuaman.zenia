import os
#Declarar variables
Jhossely,Ariana,Milton,Sarai,Maricielo,colecta_para_TELETON=0.0,0.0,0.0,0.0,0.0,0.0

#Pedir las variables via argumentos
Jhossely=float(os.sys.argv[1])
Ariana=float(os.sys.argv[2])
Milton=float(os.sys.argv[3])
Sarai=float(os.sys.argv[4])
Maricielo=float(os.sys.argv[5])
colecta_para_TELETON=(Jhossely+Ariana+Milton+Sarai+Maricielo)
colecta_para_TELETON_no_necesaria=(colecta_para_TELETON<=10000)

#While
while (colecta_para_TELETON_no_necesaria==True):
    Jhossely=float(input("Pedir el dinero dado por Jhossely:"))
    Ariana=float(input("Pedir el dinero dado por Ariana:"))
    Milton=float(input("Pedir el dinero dado por Milton:"))
    Sarai=float(input("Pedir el dinero dado por Sarai:"))
    Maricielo=float(input("Pedir el dinero dado por Maricielo:"))
    colecta_para_TELETON=Jhossely+Ariana+Milton+Sarai+Maricielo
    colecta_para_TELETON_no_necesaria=(colecta_para_TELETON<=10000)
#fin_del_while
print("Fin del bucle")
print("Fondos recaudados:", colecta_para_TELETON)
