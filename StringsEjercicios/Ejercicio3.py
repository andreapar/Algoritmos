# Escriba un código que reciba un string como input y cambie por $
# todas las ocurrencias de su primera letra, excepto ella misma
# que no debe cambiar.Primero pruebe que funcione con todas minusculas.

palabra = input("Por favor escriba la palabra que desea: ")
char = palabra.capitalize()
p = char[0]
print(char.replace(p.lower(),"$"))

#Otra forma útil
str = input('Ingrese la palabra que quiera usar: ')
str1 = []
str2 = ""
n=0
for i in str:
    if n == 0:
        str1.append(i)
        n+=1
    elif n!=0:
        i1= i.casefold()
        str1.append(i1.replace(str[0].casefold(),'$'))
print(str2.join(str1))