from os import listdir

path = 'archivos_discharge_s'
names = listdir(path)

contadorMujeres = 0
contadorHombres = 0

for i in names:
    file_path = path + "/" + i
    files = open (file_path)
    data = files.read()
    ind = data.index("Sex:")
    aux = data[ind:ind+8]
    if "F" in aux:
        contadorMujeres += 1
    if "M" in aux:
        contadorHombres += 1

print("El número de pacientes hombres es:",contadorHombres)
print("El número de pacientes mujeres es:",contadorMujeres)
