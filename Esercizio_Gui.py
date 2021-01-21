import tkinter as tk 
import matplotlib as plt 
from Moduli_interfaccia import scrittore 
from Moduli_interfaccia import grafici 

interfaccia = tk.Tk()
interfaccia.geometry("900x550")
interfaccia.title("Grafici_matplotlib_gui")
interfaccia.grid_columnconfigure(0, weight=1) 

def creafile():
    if box_di_testo.get():
        scrittore(box_di_testo)
        grafici(box_di_testo)
    else:
        testo_scritto = "Inserisci un nome!"

inserisci_nome = tk.Label(interfaccia, text="Dai un nome al file con le coppie:", font=("helvetica", 20))
inserisci_nome.grid(row=0, column=0, sticky="N", padx=20, pady=10)

box_di_testo= tk.Entry(width=60)
box_di_testo.grid(row=1, column=0, padx=20)

bottone_crea_file = tk.Button(text=("Crea file"), command=creafile)
bottone_crea_file.grid(row=2, coulmn=0, padx=20)

interfaccia.mainloop()
