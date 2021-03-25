from guizero import * 
from random import randint
def leggifile():
    f = open("testo.txt", 'r')
    for riga in f:
        valori = str(riga)         
        valori = valori.strip('\n') 
        valori = valori.split(',')  
        valori = list(valori)   
        output.append(valori)  
    f.close()
interfaccia = App(title="lettore di file", width=300, height=250, bg="#c0c0c0" )
inserisci_nome = Text(interfaccia, text="Premi per leggere il file con le coppie", font=("helvetica", 20))
bottone_crea_file = PushButton(interfaccia, text=("leggi file"), command=leggifile, width=10, height=2)
output = TextBox(interfaccia, width=60, height=10, multiline=True)
interfaccia.display()