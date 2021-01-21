from random import randint
import string
import numpy as np
import matplotlib.pyplot as plt
def Scrittore(nome):
    f = open(nome, 'w')
    coppia = ""
    for x in range(100):
        for y in range(1):
            coppia = coppia + str(randint(1,100)) + "," + str(randint(1,100))
        coppia = coppia + "\n"
    print(coppia)
    f.write(coppia)
    f.close()

def grafici(nome):
    f = open(nome, 'r')
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
    plt.plot(coordinateX,coordinateY)
    plt.ylabel('some numbers')
    plt.show()


