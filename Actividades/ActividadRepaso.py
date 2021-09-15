import math
from os import system,name

def limpiarPantalla():
    if (name == "nt"):
        _ = system("cls")
    else:
        _ = system("clear")

#Punto 5
nombre = input ("Hola, por favor escriba su nombre: ")
apellido = input ("Digite luego su apellido por favor: ")
print("Hola " + apellido + " " + nombre)

input("\nPresione una tecla para continuar.")
    
limpiarPantalla()

#Punto 6
numeros = input("Hola, por favor digite los números separados por una coma: ")
lista1 = numeros.split(",")
tuple = tuple(lista1)
print("lista: ", lista1)
print("tuple: ", tuple)

input("\nPresione una tecla para continuar.")
    
limpiarPantalla()

#Punto 15
radio = 6
volumen = 4/3 * math.pi * radio**3 
print("El volumen de la esfera es: ",volumen)

input("\nPresione una tecla para continuar.")
    
limpiarPantalla()

#Punto 16
inNumero = float(input("Ingresa un número por favor: "))
if (inNumero > 17 ):
    diferencia =(inNumero - 17 ) * 2
    print("La diferencia es: ", diferencia)
else:
    diferencia2 = 17 - inNumero
    print("La diferencia total es: ", diferencia2)

input("\nPresione una tecla para continuar.")
    
limpiarPantalla()

#Punto 18
def sumarTresNumeros (num1,num2,num3):
    if (num1 == num2 == num3):
        suma = (num1 + num2 + num3) * 3
        return suma
    else:
        suma2 = num1 + num2 + num3
        return suma2

num1 = float(input("Ingrese número 1: "))
num2 = float(input("Ingrese número 2: "))
num3 = float(input("Ingrese número 3: "))

resultado = sumarTresNumeros(num1,num2,num3)
print("La suma de los tres número es: ",resultado)

input("\nPresione una tecla para continuar.")
    
limpiarPantalla()

#Punto 22
def encontrarNumero (lista,numeroBuscar):
    cantidad = 0  
    for i in lista:
        if ( i == numeroBuscar):
            cantidad = cantidad + 1

    return cantidad

listaN = [3,5,4,7,8,4,0,4,4,7,8,9,4]
print("La cantidad de números 4 es:", encontrarNumero(listaN,4))

input("\nPresione una tecla para continuar.")
    
limpiarPantalla()

#Punto 24
def esVocal(letra):
    vocales = 'aeiou'
    return letra in vocales

letra = input("Ingresa la letra que deseas conocer si es una vocal: ")
resultado = esVocal(letra)
if resultado:
    print(f"La letra {letra} es una vocal")
else:
    print(f"La letra {letra} no es una vocal")

input("\nPresione una tecla para continuar.")
    
limpiarPantalla()

#Punto 28
lista2 = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for i in lista2:
    if (i == 237):
        print(i)
        break
    elif (i % 2 == 0):
        print(i)

input("\nPresione una tecla para continuar.")
    
limpiarPantalla()

#Punto 29
listacolores1 = ["Blanco", "Negro","Rojo"]
listacolores2 = ["Rojo","Verde"]
print("Colores originales:")
print(listacolores1)
print(listacolores2)

print("\nDiferencia de la lista1 de colores a la número 2:")
for color1 in range (listacolores1):
    existe = False
    for color2 in range (listacolores2):
        if color1 == color2:
            existe = True
    if existe == False:
        print(color1)
