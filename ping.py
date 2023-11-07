#!/usr/bin/python3
# Ejemplo de programa para hacer una llama al sistema
import os

comando = "ping -c 1"
#host = "dsc.morelia.tecnm.mx"
host = "dsc.morelia.tecnm.mx"

#respuesta = os.execl(comando+" "+host, "-c 1 "+host)
respuesta = os.system(comando+" "+host)

#print(respuesta)
if respuesta==0:
  print("Host existente")
else:
  print("Host no existe el host")

