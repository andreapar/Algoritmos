import numpy as np

# 1. ¿Cuantas personas tienen 18 años?
edades = np.array([18, 18, 17, 18, 20, 21, 23, 20, 18, 18, 19, 21])
ind = edades == 18
out1 = edades[ind]  
print(f"Las personas que tienen 18 es: {len(out1)}")

# 2. ¿Cuantas personas tienen 20 o más años?
ind = edades >= 20
out2 = edades[ind]  
print(f"Las personas que tienen 18 es: {len(out2)}")

# 3. ¿Cuantas personas tienen entre 17 y 19 años?
ind1 = edades >= 17
ind2 = edades <= 19
ind = ind1 & ind2
out3 = edades[ind]
print(f"Las personas que tiene entre 17 y 19 son : {len(out3)}")

# 4. ¿Cuál es la edad promedio de los menores de 23 años?
ind = edades < 23
out4 = edades[ind]
edadPromedio = round(np.mean(out4),2)  
print(f"La edad promedio menor a 23 años es: {edadPromedio}")

# 5. A los mayores de 22 años asignarles edad igual a cero.
ind = edades > 22
edades[ind] = 0
print(f"Nueva variable con ceros: {edades}")

# 6. A los que tengan 18 o 20 años asignarles una edad de 100.
edades = np.array([18, 18, 17, 18, 20, 21, 23, 20, 18, 18, 19, 21])
ind8 = edades == 18
ind9 = edades == 20
indT = ind8 | ind9
edades[indT] = 100
print(f"La nueva variable con la edad de 100 es: {edades}")

# 7. Genere un print que haga la función de tabla de frecuencias así:
#    cantidad 17 años: 1
#    cantidad 18 años: 5
#    cantidad 19 años: 1
#    cantidad 20 años: 2
#    cantidad 21 años: 2
#    cantidad 22 años: 0
#    cantidad 23 años: 1
edades = np.array([18, 18, 17, 18, 20, 21, 23, 20, 18, 18, 19, 21])
for x in range (17,24):
    ind3 = edades == x
    print(f"Cantidad {x} años: {sum(ind3)}")