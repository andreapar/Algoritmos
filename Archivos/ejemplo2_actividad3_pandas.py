# Separar los datos del archivo Municipality_Area.csv
# en tres arreglos, uno por columna. Para texto usar
# listas y para número ndarray de numpy. Luego:
# a. ¿cuál es el área total de Colombia?
# b. ¿cúal es el municipio de mayor área en Colombia?
# c. ¿cuántos departamentos tiene Colombia?
import pandas as pd

df = pd.read_csv("Municipality_Area.csv")

# a 
print(df["Area (km2)"].sum())

# b
ind = df["Area (km2)"].argmax()
print(df.iloc[ind])
#print(df.iloc[df["Area (km2)"].idxmax()])

# c
print(len(df['Departamento'].unique()))

# Bonus: cantidad de municipios por departamento
print(df['Departamento'].value_counts())
print(df[df['Departamento']=="Antioquia"]['Departamento'].value_counts())
