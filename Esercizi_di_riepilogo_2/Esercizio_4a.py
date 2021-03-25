from guizero import * 
from random import randint
def creafile():
    f = open("testo.txt", 'w')
    numeri=""
    for x in range(100):
        numeri= numeri + str(randint(1,100)) + "," + str(randint(1,100))
        numeri= numeri + "\n"
    f.write(numeri)
    f.close()
interfaccia = App(title="generatore di file", width=300, height=250, bg="#c0c0c0" )
inserisci_nome = Text(interfaccia, text="Premi per generare il file con le coppie", font=("helvetica", 20))
bottone_crea_file = PushButton(interfaccia, text=("Crea file"), command=creafile, width=10, height=2,)
interfaccia.display()