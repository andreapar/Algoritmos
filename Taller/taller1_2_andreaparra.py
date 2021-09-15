from os import listdir

def existeProcedimiento (data, procedimiento):
    return data.upper().find(procedimiento.upper()) != -1

path = 'archivos_discharge_s'
names = listdir(path)

contadorProcedimiento = 0

for i in names:
    file_path = path + "/" + i
    file = open (file_path)
    data = file.read()

    existe = existeProcedimiento(data, "tracheotomy")
    if existe:
        contadorProcedimiento += 1
    else:
        existe = existeProcedimiento(data, "tracheostomy")
        if existe:
            contadorProcedimiento += 1

print("El número de pacientes que tuvieron una traqueotomía es:",contadorProcedimiento)