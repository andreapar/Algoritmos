# convierta la siguiente frase en un diccionario:

words = "Biomédica:35-Medicina:14-Nutrición:22-Derecho:2"
d = dict((l.split(":") for l in words.split("-")))
print(d)

#Otra forma
dic = {}
wordslist = words.split("-")
#print(wordlist)
for i in wordslist:
    key, value = i.split(":")
    dic[key] = int(value)
print(dic)