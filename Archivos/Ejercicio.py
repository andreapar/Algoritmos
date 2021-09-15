# Imprima en pantalla la fecha de nacimiento del paciente

file1 = "discharge_s_14237.txt"
file2 = "discharge_s_6893.txt"
file3 = "discharge_s_19989.txt"

#Forma 1
file = open(file1)
allData = file.readlines()
print(allData[6][19:27]) # posición del primer corchete y luego del segundo

#Forma 2
substring = allData[6]  #Esta en la linea 6
pos1 = substring.index("[") #Posción del corchete
pos2 = substring.index("]")

print(allData[6][pos1 + 3:pos2 -2])  #Para quitar los corchetes y *