import numpy as np
from random import randint
lista=[[randint(1,100),randint(1,100),randint(1,100)],
        [randint(1,100),randint(1,100),randint(1,100)],
        [randint(1,100),randint(1,100),randint(1,100)]]
lista_bidimensionale=np.array(lista)
print(lista_bidimensionale)
utente = int(input("scegli quale delle 3 righe visualizzare: \n")) - 1
print(lista_bidimensionale[utente])