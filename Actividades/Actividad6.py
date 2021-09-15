def Vacunar (nombre,edad,covid,comorbilidad):
    if covid.upper() == "SI" or covid.upper() == "S":
        return False
    
    if edad >= 35:
        return True
    
    if (comorbilidad.upper() == "SI" or comorbilidad.upper() == "S") and edad >= 12:
        return True

    return False

nombre = input("Hola, por favor digite su nombre: ")
edad = int(input("Escriba su edad: "))
covid = input("Ha presentado covid-19 en los últimos tres meses: ")
comorbilidad = input("Tiene alguna comorbilidad: ")

puedeVacunarse = Vacunar(nombre,edad,covid,comorbilidad)

if puedeVacunarse:
    print("Se puede vacunar")
else:
    print("No te puedes vacunar")
