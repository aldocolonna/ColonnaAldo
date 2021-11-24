# classe calcolo combinatorio
from itertools import permutations
class calcComb():

    def selezione_lingua(self):
        lingua = {"Italiano":"word.italian.txt"}
        lingua["Italiano"]  #in questo punto potrebbe essere integrato un'input per chiedere all'utente la lingua del gioco
        return lingua 
    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self):
        self.__stringa = stringa
        return self.__stringa

    def charRipetuti(self):

        word = self.liststringa  

        carattere = {}

        nCaratteri = 0

        count = 0

        for i in word:

            if (i in carattere):  
                carattere[str(i)] += 1
            else:
                carattere[str(i)] = 1 

        for i in carattere:
            if carattere[i]>1: 
                count+=1 
                nCaratteri += carattere[i] 
  
        Variabili_anagrammi = [count,nCaratteri,carattere]
        
        return Variabili_anagrammi

    def confUtil(self,lingua):
        
        f = open(lingua, 'r')
        
        riga = f.readline()
        Presenza == False
        for riga in f:
            if self.__stringa == riga[:-1]:
                Presenza == True

        return Presenza
    def fattoriale(n):
        n=int(n)
        f = 0 
        if n < 0: 
            print("Non è possibile calcolare il fattoriale di un numero negativo")
        elif n == 0: 
            f= 1
        else: 
            f = 1
            
            while(n > 1): 
                f *= n 
                n -= 1
            
        return f
    def coeffBinom(n, k):
        if k == n:
            cb = 1
        
        elif k == 1:         
            cb = n
        
        elif k > n:          
            cb = 0
        
        else:
            cb = calcComb.fattoriale(n) // (calcComb.fattoriale(n) * calcComb.fattoriale(n-k))
    
        return cb
    # PERMUTAZIONI

    def nPermutSenzaRip(self):

        return calcComb.fattoriale(self.__N)
     

    def nPermutConRip(self):

        return calcComb.fattoriale(self.__N)/calcComb.charRipetuti(self.__count)

    def permutSenzaRip(self):
        listapermutazioni = list(itertools.permutations(self.__stringa))
        temp = ''
        anagrammi = []
        for i in listapermutazioni:
            for carattere in i:
                
                temp += carattere 

            anagrammi.append(temp)
            
            temp = ''
        return anagrammi 

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self,k):
       if self.__N >= k:

        return calcComb.fattoriale(self.__N) / calcComb.fattoriale(self.__N-k)

    def nDispSemplConRip(self,k):

        return self.__N**k

    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        return 0


    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self,k):

        return calcComb.fattoriale(self.__N) / (calcComb.fattoriale(k) * calcComb.fattoriale(self.__N-k))

    def nCombSemplConRip(self,k):
 
        return calcComb.fattoriale(self.__N+k-1) / (calcComb.fattoriale(k) * calcComb.fattoriale(self.__N-1))


    def combSenzaRip(self):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetizione
        '''
        return 0

    def combConRip(self):
        '''
        generare e restituire la lista delle combinazioni CON ripetizione
        '''
        return 0

