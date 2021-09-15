listaNombres = ["Camilo", "Andrea", "Marcela","Camil","Andrea","Isabel","Daniel"]

def encontrarNombre (lista,nombres):
    cantidad = 0  
    for i in lista:
        if ( i == nombres):
            cantidad = cantidad + 1

    return cantidad

print("La cantidad de nombres repetidos es:", encontrarNombre(listaNombres,"Andrea"))
print("================================================")

#Otra forma de hacerlo
listaNombres2 = ["Camilo", "Andrea", "Marcela","Camil","Andrea","Isabel","Daniel","Andrea"]
n = 0
x = input("Escriba un nombre por favor: ")
x = x.capitalize()
for i in listaNombres2:
    if i.capitalize() == x:
        n = n + 1
print("La cantidad de veces repetidas es:", n)