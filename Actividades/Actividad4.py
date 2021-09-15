print("Hola, hoy podrás escribir una palabra la cual hallaré cuantas veces se repite")
palabra = input("Ingrese una palabra: ")

letraRepetida = input("Ingrese la leltra que quisiera ver cuántas veces está repetida: ")
n = 0
for i in range(len(palabra)):
    if letraRepetida == palabra[i]:
        n +=1
print(n)
print(f"La letra {letraRepetida} se repite {n} veces")