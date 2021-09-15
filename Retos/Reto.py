#Punto 1
from datetime import date

file1 = "discharge_s_6893.txt"
file2 = "discharge_s_14237.txt"
file3 = "discharge_s_19989.txt"

def calcularEdadDateTime (file):
    archivo = open(file)
    allData = archivo.readlines()
    fechaNacimientoTexto = allData[6][allData[6].index("[") + 3 : allData[6].index("**]")]
    fechaAdmisionTexto = allData[4][allData[4].index("[") + 3 : allData[4].index("**]")]

    fechaAdmision = date(int(fechaAdmisionTexto[0:4]),int(fechaAdmisionTexto[5:6]),int(fechaAdmisionTexto[8:9]))
    fechaNacimiento = date(int(fechaNacimientoTexto[0:4]),int(fechaNacimientoTexto[5:6]),int(fechaNacimientoTexto[8:9]))

    edad = fechaAdmision.year - fechaNacimiento.year -((fechaAdmision.month,fechaAdmision.day) < (fechaNacimiento.month,fechaNacimiento.day))
    return edad

edad = calcularEdadDateTime(file2)

print("El paciente tiene:", edad)

#Nota: con esta función se resta un año si la persona aún no ha cumplido años.
