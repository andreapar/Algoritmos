# Indique con un print cuantos días, horas y minutos faltan para que 
# jueguen Newell's vs River Plate por la fecha 11° del torneo local
# en Argentina.
#15 de septimbre 7

import datetime as dt

iniTime = dt.datetime.now()
matchTime = dt.datetime(2021,9,15,19) #El último es la hora 
timeEsp = matchTime - iniTime
print("Faltan:",timeEsp)