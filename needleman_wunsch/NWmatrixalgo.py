#Ecrire l'algorithme NW avec la matrice  et les scores Match=0, Mismatch=1, Gap=1 --> il faut minimiser la distance 

#os.makedirs(needleman_wunsch)

#from needleman_wunsch import Ruler

import numpy as np

class Ruler: 

    def match(self,m,n) :
        if m==n :
            return 0
        else : 
            return 1
 

#construction de la matrice
    def compute(self,a,b) :
        a = [i for i in a]
        b= [i for i in b] 
        x = len(a) +1
        y = len(b) +1
        #initialison la matrice à zéro
        mat1 = np.zeros(y,x)
        #remplir la prmière colonne et la première ligne des pénalités du gap, soit 1 multuplié par leur éloignement de l'origine
        for i in range (0,x) : 
            mat1[i][0] = i
        for i in range (0,y) : 
            mat1[0][i]=  i
        #remplir le reste de la matrice en trouvant le chemin qui minimise la distance en partant de 0 en calculant le score à chaque étape
        mat1[0][0]=0
        for i in range (1,y) :
            for j in range (1,x): 
                if a[j-1] == b[i-1] : #lors d'un match
                    dia = mat1[i-1][j-1] 
                else :
                    dia =mat1[i-1][j-1] +1 #pénalité du mismatch
                #déplacement vertical ou horizontal entraine un gap et donc une pénalité de 1
                hor = mat1[i-1][j] + 1 
                ver = mat1[i][j-1] + 1
                mat1[i][j] = min(dia, hor, ver) #on essaie de minimiser la distance 
        return mat1

#calculons maintenant la distance en partant de la fin, en remontant la matrice 
    def distance(self,a,b) :
        i=a
        j=b
        while i > 0 and j> 0 : 
            note_act = mat1[i][j]
            note_dia = mat1[i-1][j-1]
            note_ver = mat1[i-1][j]
            note_hor = mat1[i][j-1]


            if note_act == note_dia + match(a[i-1], b[j-1]) : #on peut remonter par la diagonale 
                s1,s2 = a[i-1],b[j-1]
                i,j = i-1,j-1
                
            elif note_act == note_ver + 1:
                s1,s2 = a[i-1],'-'
                i -= 1

            elif note_act == note_hor + 1:
                s1,s2 = '-',b[j-1]
                j -= 1
            
            top += s1
            bottom += s2

            #Attention , si jamais j== 0 avant i, on continue à bouger de manière verticale (même chose sur j ensuite)
        while i > 0:
            s1,s2 = a[i-1],'-'
            top += s1
            bottom += s2
            i -= 1
        while j > 0:
            s1,s2 = '-',b[j-1]
            top += s1
            bottom += s2
            j -= 1
    
        top = top[::-1]
        bottom = bottom[::-1]
        len(top)
        distance = 0
        for i in range(len(top)):
            s1 = top[i]
            s2 = bottom[i]
            if not s1 == s2:
                distance += 1
    
        return distance
        return top
        return bottom

ruler = Ruler("abcdefghi","abcdfghi")




        

