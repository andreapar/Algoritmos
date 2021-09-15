import pandas as pd

df = pd.read_csv('Municipality_Area_mod.csv')

departamento = input("Digite el nombre del departamento: ")

aux = df[df["Departamento"] == departamento]
areaMaxima = aux.iloc[aux["Area (km2)"].argmax()]

print(f"El municipio de {departamento} con mayor área es:", areaMaxima["Municipio"])
