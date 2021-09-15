import csv
import numpy as np

#Forma 1
file = open("Municipality_Area.csv", encoding= "UTF-8")  # El UTf -8 es para que muestre los formatos
# lines = csv.reader(file,delimiter= ",")
# lines = list(lines)
# print(lines)
# print(lines[3][1])  #Lista dentro de una lista

#Forma 2
lines = csv.DictReader(file,delimiter= ",")
for aux in lines:                        # Se utiliza diccionarios
    print(aux)
    print(aux["Municipio"])
