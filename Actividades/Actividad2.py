#Ejercicio 2
numeros = [3,5,7,9,12,14,15,78,2,]
a = 0
for i in numeros:
    if i % 2 == 0:
        a = a + 1
print(f"Total número de pares: {a}")