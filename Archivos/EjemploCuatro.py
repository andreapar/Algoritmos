import csv

file = open("Municipality_Area.csv", encoding="UTF-8")

lines = csv.DictReader(file,delimiter= ",")

depmun = {}
listamun = []
i = 0

for aux in lines:
    if i == 0:
        depAnt = aux["Departamento"]
    dep = aux["Departamento"]
    mun = aux["Municipio"]
    i = i +1
    if dep == depAnt:
        listamun.append(mun)
    else:
        depmun[depAnt] = listamun
        i = 0                         #Reinicia el contador
        listamun = []

depearch = input("Indique el nombre del departamento: ")
print(depmun[depearch])
    