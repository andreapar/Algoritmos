#escriba un código que reorganice las letras de una palabra
# empezando por las minusculas y continuando por las 
# mayúsculas.
# ejemplo: AlGoritMos queadría loritosAGM

word = "AlGoritMos"
arrMin = []
arrMay = []

for i in word:
    if i.islower():
        arrMin.append(i)
    else:
        arrMay.append(i)

print("".join(arrMin + arrMay))

