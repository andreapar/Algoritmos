s = 'comunicaciones'
letra = ['a', 'e', 'i', 'o', 'u']

for j in letra:
    n = 0
    for i in range(len(s)):
        if s[i]==j:
            n+=1
    print(f"la letra {j} está {n} veces")

# Otra forma de hacerlo
palabra = input("Ingrese una palabra por favor: ")

valorA = 0
valorE = 0
valorI = 0
valorO = 0
valorU = 0

for i in palabra:
    if ( i == "a"):
        valorA += 1
    elif (i == "e"):
        valorE += 1
    elif (i == "i"):
        valorI += 1
    elif (i == "o"):
        valorO += 1
    elif (i == "u"):
        valorU += 1

print(f"La vocal a se repite {valorA} veces")
print(f"La vocal e se repite {valorE} veces")
print(f"La vocal i se repite {valorI} veces")
print(f"La vocal o se repite {valorO} veces")
print(f"La vocal u se repite {valorU} veces")