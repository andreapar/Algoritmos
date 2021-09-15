# Punto 2
def contarAlergias (file):
    archivo = open(file)
    allData = archivo.readlines()
    
    linea = allData[11] + allData[12]
    if "No" in linea:
        n = 0
    else:
        alergias = list(linea.split("/"))
        n = 0
        for x in range(len(alergias)):
            n += 1
    return n

file1 = "discharge_s_6893.txt"
file2 = "discharge_s_14237.txt"
file3 = "discharge_s_19989.txt"

cantidadAlergia = contarAlergias(file3)
print("El paciente tiene",cantidadAlergia,"alergias")