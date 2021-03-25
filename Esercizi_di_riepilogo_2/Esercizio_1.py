import numpy as np
a=(input("inserisci 5 numeri separati da una virgola: \n"))
delimita=','
lista=a.split(delimita)
Vettore=np.array(lista)
print(lista)
lista.sort()
print(lista)
lista.reverse()
print(lista)
