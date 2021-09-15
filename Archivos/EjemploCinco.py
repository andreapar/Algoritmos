import csv
import numpy as np

file = open("Municipality_Area.csv", encoding="UTF-8")
lines = csv.DictReader(file,delimiter= ",")

del lines [0]  #Quitar los headers

areas = np.zeros(len(lines))
dep = []
mun = []

i = 0
for aux in lines:     #Aux cada línea de lines
    dep.append(aux[0])
    mun.append(aux[1])
    try:
        areas[i] = int(aux[2])
    except:
        areas[i] = 0
    i = i + 1

#Solución A
print(np.sum(areas))

#Solución B
indmax = np.argmax(areas)
print(lines[indmax])
print(mun[indmax])

#Solcuión c
uniquedeb = set(dep)  #Se utiliza un set porque hay archivos dieferentes
print(f"El número del departamento son: {len(uniquedeb)}")
print(set(dep))

