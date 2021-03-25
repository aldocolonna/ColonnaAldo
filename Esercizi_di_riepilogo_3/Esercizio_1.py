from numpy import mean
Alunni={
        "Mario":{"Matematica":6,"Italiano":6,"cienze":7,"Inglese":4}, 
        "Giovanni":{"Matematica":4,"Italiano":6,"cienze":5,"Inglese":7}, 
        "Paola":{"Matematica":9,"Italiano":6,"cienze":8,"Inglese":8}
        }
voti_mario=list(Alunni["Mario"].values())
voti_giovanni=list(Alunni["Giovanni"].values())
voti_paola=list(Alunni["Paola"].values())
print("La media di Mario è: " + str(mean(voti_mario)))
print("La media di Giovanni è: " + str(mean(voti_giovanni)))
print("La media di Paola è: " + str(mean(voti_paola)))
