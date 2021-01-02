
import string
import numpy as np
import matplotlib.pyplot as plt

f = open("dati_grafici.txt", 'r')

coordinateX = []
coordinateY = []

for riga in f:
    valori = str(f.readline())  
    Nval = len(valori)          
    valori = valori.strip('\n') 
    valori = valori.split(',')  
    valori = list(valori)       
    print(valori)
    coordinateX.append(int(valori[0])) 
    coordinateY.append(int(valori[1])) 

f.close()  

print ("X: ",coordinateX)
print ("Y: ",coordinateY)

coordinateX.sort()
coordinateY.sort()

print("liste ordinate:") 
print ("X: ",coordinateX)
print ("Y: ",coordinateY)

print(type(coordinateX))
print(type(coordinateY))

plt.scatter(coordinateX,coordinateY)
plt.ylabel('some numbers')
plt.show()