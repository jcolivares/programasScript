#!/usr/bin/python3
# Ejemplo de programa para hacer una llama al sistema
import os
import subprocess

comando = "nmap "
#host = "dsc.morelia.tecnm.mx"
host = "dsc.morelia.tecnm.mx"

respuesta = os.popen(comando+" "+host).readlines()

#print(respuesta)

lista = respuesta[6:len(respuesta)-2]

for linea in lista:
    #print(linea, end="")
    campos = linea.split()
    print("Servicio>", campos[0], "X", campos[1], "y", campos[2])    