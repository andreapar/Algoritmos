import csv

file = open("Municipality_Area_mod.csv", encoding="UTF-8")

lines = csv.DictReader(file,delimiter= ",")

depAreas = {}
listaAreas = []
i = 0

for aux in lines:
    if i == 0:
        depAnt = aux["Departamento"]
    dep = aux["Departamento"]
    area = int(aux ["Area (km2)"])
    i = i + 1
    if dep == depAnt:
        listaAreas.append(area)
        sumatoriaAreas = sum(listaAreas)
    else:
        depAreas[depAnt] = sumatoriaAreas
        i = 0                      
        listaAreas = []

depsearch = input("Indique el nombre del departamento: ")
print(f"El área total es {depAreas[depsearch]} km2")