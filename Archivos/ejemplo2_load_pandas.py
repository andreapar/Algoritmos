import pandas as pd

df = pd.read_csv("Municipality_Area.csv")

#print(df.describe())
# Exploración
#print(df.head(5))
#print(df.head(8))
#print(df.tail(8))

# Ver columnas
#print(df.columns)

# Ver una columna
#print(df['Municipio'])
#print(df.Municipio)

# Ver por rango (slicing) 
#print(df.iloc[0:3])
#print(df.iloc[0:3,0:2])

# Ver con condición
#print(df[df.Departamento == 'Antioquia'])
#print(df[df.Departamento == 'Antioquia'].head(7))
#print(df[df['Area (km2)'] > 20000].head(7))
