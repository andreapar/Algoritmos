from datetime import date

file1 = "discharge_s_14237_desordenado.txt"
ETIQUETA_FECHA_NACIMIENTO = "Date of Birth"
ETIQUETA_FECHA_ADMISION = "Admission Date"
ETIQUETA_ALERGIAS = "Allergies"


def obtenerLineaEtiqueta (allData, etiqueta):
    lineaEtiqueta = -1
    contadorLinea = 0

    for line in allData:
        if line.startswith(etiqueta): # Busca si una cadena empieza con otra cadena
            lineaEtiqueta = contadorLinea # Da los números del archivo
            break
        contadorLinea += 1

    return lineaEtiqueta

def calcularEdad (allData, lineaFechaNacimiento, lineaFechaAdmision):
    fechaNacimientoTexto = allData[lineaFechaNacimiento][allData[lineaFechaNacimiento].index("[") + 3 : allData[lineaFechaNacimiento].index("**]")]
    fechaAdmisionTexto = allData[lineaFechaAdmision][allData[lineaFechaAdmision].index("[") + 3 : allData[lineaFechaAdmision].index("**]")]

    fechaAdmision = date(int(fechaAdmisionTexto[0:4]),int(fechaAdmisionTexto[5:6]),int(fechaAdmisionTexto[8:9]))
    fechaNacimiento = date(int(fechaNacimientoTexto[0:4]),int(fechaNacimientoTexto[5:6]),int(fechaNacimientoTexto[8:9]))

    edad = fechaAdmision.year - fechaNacimiento.year -((fechaAdmision.month,fechaAdmision.day) < (fechaNacimiento.month,fechaNacimiento.day))
    return edad

def contarAlergias (allData,lineaAlergias):
    linea = allData[lineaAlergias + 1] + allData[lineaAlergias + 2]
    if "No" in linea:
        n = 0
    else:
        alergias = list(linea.split("/"))
        n = 0
        for x in range(len(alergias)):
            n += 1
    return n

#Código

archivo = open(file1)
allData = archivo.readlines()

lineaFechaNacimiento = obtenerLineaEtiqueta(allData, ETIQUETA_FECHA_NACIMIENTO)
lineaFechaAdmision = obtenerLineaEtiqueta(allData, ETIQUETA_FECHA_ADMISION)

if lineaFechaAdmision == -1:
    print("No se encontró la fecha de admisión en el archivo")

if lineaFechaNacimiento == -1:
    print("No se encontró la fecha de nacimiento en el archivo")

if lineaFechaNacimiento >= 0 and lineaFechaAdmision >= 0:
    edad = calcularEdad(allData, lineaFechaNacimiento, lineaFechaAdmision)
    print("La edad del paciente es:", edad)

#Alergias
lineaAlergias = obtenerLineaEtiqueta(allData, ETIQUETA_ALERGIAS)

if lineaAlergias == -1:
    print("No se encontró las alergias en el archivo")

if lineaAlergias >= 0: 
    cantidadAlergia = contarAlergias(allData, lineaAlergias)
    print("El número de alergias es:", cantidadAlergia)