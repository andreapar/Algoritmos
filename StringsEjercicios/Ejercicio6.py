# escriba un código que reciba una frase como input conformada por varias
# palabras. Realice un print que diga cuál es la más larga y cuál es
# su número de caracteres.
# ejemplo: "Mi materia favorita es algoritmos y estructura de datos"
# el resultado sera: 
# La palabras más larga es: algoritmos
# su tamaño es: 10.0

palabraEntrada = input("Por favor escriba la frase que desea: ")
var = palabraEntrada.split(" ")
aux = max(var, key=len)
tamaño = len (aux)

print(f"La palabra más larga es: {aux} y su tamaño es {tamaño}")

#Otra forma
wordIn = input("Por favor escriba la frase que desea: ")
list = wordIn.split(" ")
tamaño = []

for i in list:
    tamaño.append(len(i))
wordLarge = tamaño.index(max(tamaño))

print(f"La palabra más larga es: {list[wordLarge]} y su tamaño es {max(tamaño)}")
