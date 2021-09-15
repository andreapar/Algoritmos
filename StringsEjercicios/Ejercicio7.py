from os import listdir

path = 'archivos_discharge_s'
names = listdir(path)

contadorProcedimiento = 0

for i in names:
    file = open(path + "/" + i)
    data = file.read().lower()
    contador1 = data.count("tracheotomy")
    contador2 = data.count("tracheostomy")

    if(contador1 + contador2) > 0:
        contadorProcedimiento = contadorProcedimiento + 1

print(f"Contiene la palabra clave: {contadorProcedimiento} archivos")