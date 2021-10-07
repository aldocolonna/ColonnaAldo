'''A = int(input('dammi un intero'))
B = int(input('dammi un intero'))
M = A if A > B else B
print(M)


A = int(input('inserisci un numero: '))
if A > 0:
    print('il numero è maggiore di 0')
elif A < 0:
    print('il numero è minore di 0')
else: 
    print('il numero è 0')


def assoluto(A):
    if A > 0:
        print(A)
    else:
        print(-A)
B = int(input('Inserisci un numero: '))
assoluto(B)

A = int(input('Inserisci un numero intero'))
if A > 0:
    print(A)
else:
    print(-A)
'''
'''
 import math
def cerchio(raggio):
    Area = math.pi * raggio * raggio;

    Circonferenza = raggio * 2 * math.pi
    return Area,Circonferenza
raggio = int(input("inserisci il raggio"))
Area,Circonferenza = cerchio(raggio)
print(Area)
print(Circonferenza)'''

'''
from array import *
def Numeri_primi(Max):
    Cr = array('i',[1 for i in range(Max + 1)])

    Cr[0] = 0
    Cr[1] = 0

    i = 2
    while i*i <= Max:
        if Cr[i] == 1:
            j = i + i
            while j <= Max:
                Cr[j] = 0
                j += i
        i += 1
    return(Cr)

def Conta_primi(Cr,Max):
    print('Numeri primi')
    Cont = 0
    for i in range(0,Max+1):
        if Cr[i] == 1:
            print(i,end='')
            Cont = Cont + 1
    print('\n Ci sono',Cont,'Numeri primi',Max)

Max = int(input('Inserisci un numero: '))
Cr = Numeri_primi(Max)
Conta_primi(Cr,Max)
'''
'''from array import *
Max= 1000
Cr = array('i',[1 for i in range(Max + 1)])

Cr[0] = 0
Cr[1] = 0

i = 2
while i*i <= Max:
    if Cr[i] == 1:
        j = i + i
        while j <= Max:
            Cr[j] = 0
            j += i
    i += 1

for i in range(0,Max+1):
    if Cr[i] == 1:
        print(i)'''
