import random 
def pi_greco(N):
    dentro = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            dentro = dentro + 1
    Pg = (4*dentro/N)
    return Pg

N = int(input("inserisci un numero di punti"))
prova = pi_greco(N)
print(prova)
