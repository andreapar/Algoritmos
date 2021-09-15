import pandas as pd

df = pd.read_csv('Municipality_Area_mod.csv')

departamento = input("Digite el nombre del departamento: ")
area = input("Digite el valor de la área de referencia: ")

aux = df[df["Departamento"] == departamento]
municipiosAreaMayor = aux[aux["Area (km2)"] > int(area)]

print(f"Los municipios de {departamento} con un área mayor a {area} son:")

for municipio in municipiosAreaMayor["Municipio"]:
    print(f"- {municipio}")