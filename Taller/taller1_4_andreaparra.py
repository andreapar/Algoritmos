import csv

file = open("Municipality_Area_mod.csv", encoding="UTF-8")
lines = csv.DictReader(file,delimiter= ",")

def consultarMunicipioMayorA(departamento):
    munAreas = {}
    listaAreas = []
    listaMunicipio = []
    i = 0

    for aux in lines:
        if i == 0:
            depAnt = aux["Departamento"]

        dep = aux["Departamento"]
        mun = aux["Municipio"]
        area = int(aux ["Area (km2)"])
        i = i + 1

        if dep == depAnt:
            listaAreas.append(area)
            listaMunicipio.append(mun)
        else:
            areaMaxima = max(listaAreas)
            posicionMx = listaAreas.index(areaMaxima)
            munAreas[depAnt] = listaMunicipio[posicionMx]
            i = 0                      
            listaAreas = []
            listaMunicipio = []
    return munAreas[departamento]

departamento = input("Digite el nombre del departamento: ")
municipioMayorArea = consultarMunicipioMayorA(departamento)

print(f"El municipio de {departamento} con mayor área es: {municipioMayorArea}")