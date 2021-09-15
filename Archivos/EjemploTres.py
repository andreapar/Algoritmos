import csv

file = open("Municipality_Area.csv", encoding="UTF-8")

munAreas = {}  # Para crear un diccionario vacio

lines = csv.DictReader(file,delimiter=",")
for aux in lines:
    mun = aux["Municipio"]  #Keys
    area = aux["Area (km2)"] #Value
    munAreas[mun] = area


munsearch = input("Indique el nombre del municipio: ")
print(munAreas[munsearch])