# Crear un diccionario con los nombres de los municipios como
# keys y el área como value. Para probar el resultado pida con input
# un nombre de un municipio e imprima su área
import pandas as pd

df = pd.read_csv("Municipality_Area.csv")

munsearch = input("Indique el nombre del municipio: ")

aux = df[df['Municipio']==munsearch]
print(aux['Area (km2)'])
print(aux.values)
