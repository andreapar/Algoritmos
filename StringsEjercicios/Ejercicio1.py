# Escriba un código que transforme una lista de entrada con palabras
# en una variable tipo string con las palabras separadas por espacios.

lista = ["Lorem", "ipsum","dolor","sit","ame"]
var = ""
for i in lista:
    var = var + i +" "
print(var)

#Otra forma
lista = ["Lorem", "ipsum","dolor","sit","ame"]
var1 = " ".join(lista)
print(var1)