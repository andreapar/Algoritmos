file = open("discharge_s_6893.txt")

#Forma 1
#data = file.read()
#print(data) 

#Forma 2
#for i in range(20):
    #print(file.readline())

#Forma 3
allData = file.readlines()
print(allData)