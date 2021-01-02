from random import randint

f = open("dati_grafici.txt", 'w')

coppia = ""

for x in range(100):

    for y in range(1):
        coppia = coppia + str(randint(1,100)) + "," + str(randint(1,100))
  
    coppia = coppia + "\n"


print(coppia)

f.write(coppia)

f.close()