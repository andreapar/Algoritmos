import pandas as pd
import numpy as np

df = pd.read_csv('notas.csv')
cols = df.columns #observe esta variable en modo debug
notas_df = df[cols[1:]] #solo las notas hasta lo último

# convertir a ndarray de Numpy forma 1
notas = notas_df.values
# convertir a ndarray de Numpy forma 2
#notas = notas_df.to_numpy()  # Son los quiz

# Calcule la nota final para cada estudiante. El resultado debe ser un
# ndarray con la nota de cada uno.

#Forma 1
notasShape = notas.shape # Saber cuántas columnas y filas
notasNRows = notasShape[0] # Contar los estudiantes, son 35
notaFinal = np.empty(notasNRows)

for i in range (notasNRows):
    nota1 = notas[i,0] * 0.15 # El i recorre la columna
    nota2 = notas[i,1] * 0.15 
    nota3 = notas[i,2] * 0.25 
    nota4 = notas[i,3] * 0.15 
    nota5 = notas[i,4] * 0.30 
    final_aux = nota1 + nota2 + nota3 + nota4 + nota5 
    notaFinal[i] = final_aux 

print(notaFinal)

# Solución nivel 2
notasShape = notas.shape
notasNRows = notasShape[0]
notaFinal = np.empty(notasNRows)
p = [0.15, 0.15, 0.25, 0.15, 0.3] #ponderacion
for i in range(notasNRows):
    notaFinalAux = notas[i,0]*p[0] + notas[i,1]*p[1] +\
            notas[i,2]*p[2]+ notas[i,3]*p[3] +\
            notas[i,4]*p[4]
    notaFinal[i] = notaFinalAux
print(notaFinal)

# Solución nivel 3
p = [0.15, 0.15, 0.25, 0.15, 0.3]  
notafinal = np.empty(notas.shape[0])
for i in range(0,notas.shape[1]):
    notafinal = notafinal + notas[:,i]*p[i]
print(notafinal)

# Solución nivel semi dios
p = [0.15, 0.15, 0.25, 0.15, 0.3]
notafinal = notas[:,0]*p[0] + notas[:,1]*p[1] +\
            notas[:,2]*p[2]+ notas[:,3]*p[3] +\
            notas[:,4]*p[4]
print(notafinal)

# Solución nivel dios
p = [0.15, 0.15, 0.25, 0.15, 0.3]
notafinal = notas.dot(p)
print(notafinal)