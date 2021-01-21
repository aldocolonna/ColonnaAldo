import tkinter as tk 
import matplotlib as plt 

interfaccia = tk.Tk()
interfaccia.geometry("900x550")
interfaccia.title("Grafici_matplotlib_gui")
interfaccia.grid_columnconfigure(0, weight=1) 

def creafile():
    if box_di_testo.get():
        testo_scritto = box_di_testo.get()
    else:
        testo_scritto = "Inserisci un nome!"
        
inserisci_nome = tk.Label(interfaccia, text="Dai un nome al file con le coppie:", font=("helvetica", 10))
inserisci_nome.grid(row=0, column=0, sticky="N", padx=20, pady=10)

box_di_testo= tk.Entry(width=60)
box_di_testo.grid(row=1, column=0, padx=20)

bottone_crea_file = tk.Button(test=("Crea file"), command=creafile)

interfaccia.mainloop()
