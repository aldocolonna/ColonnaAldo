import numpy as np
lista_bidimensionale=np.array([[1,2,3],[4,5,6],[7,8,9]])
utente = int(input("scegli quale delle 3 righe visualizzare: \n")) - 1
print(lista_bidimensionale[utente])