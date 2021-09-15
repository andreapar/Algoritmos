import numpy as np

data = np.array([1, 2]) 
ones = np.ones(2, dtype=int)  # Se suma 1, 1

# suma
print("Suma",data + ones)

# resta
print("Resta",data - ones)  # 1,2 - 1,1

# mult
print("Multiplicación",data * ones) # 1,2 * 1,1

# div
print("División",data / ones) # 1,2 % 1,1

# se puede multiplicar todos y cada uno de los elementos por un entero o flotante

print("Entero",data * 8) # 1,2 * 8s

print("Flotante",data * 4.8) # inicialmente el array era de enteros, con esta operación se hace un casting y genera un array de flotantes

# operadores max, min y sum

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652], [0.54627315, 0.05093587, 0.40067661, 0.55645993], [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print("max",a.max()) # encuentra el máximo de los elementos
print("min",a.min()) # encuentra el mínimo de los elementos
print("sum",a.sum()) # encuentra la sumatoria de los elementos
print("media",a.mean()) # encuentra la media de los elementos
