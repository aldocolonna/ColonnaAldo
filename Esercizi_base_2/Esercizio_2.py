import numpy as np
from random import randint
numeri=""
for x in range(8):
    numeri= numeri + "," + str(randint(1,8)) 
lista=numeri.split(",")
lista.pop(0)
Vettore=np.array(lista)
print(lista)
numero_scelto=input("scegli un numero: \n")
volte=lista.count(numero_scelto)
print(volte)