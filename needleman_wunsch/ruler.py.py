
import numpy as np

def match(m,n) :
        if m==n :
            return 0
        else : 
            return 1

class Ruler: 

    def __init__ (self,a,b) : 
        self.a = a
        self.b = b
              

#construction de la matrice
    def compute(self,a,b) :
        #transformation en listes
        a = [i for i in a]
        b= [i for i in b] 
        x = len(a) + 1
        y = len(b) + 1
        #initialison la matrice à zéro
        mat = np.zeros((y,x))
        #remplir la première colonne et la première ligne des pénalités du gap, soit 1 multuplié par leur éloignement de l'origine
        for i in range (0,y) : 
            mat[i][0] = i
        for i in range (0,x) : 
            mat[0][i]=  i
        #remplir le reste de la matrice en trouvant le chemin qui minimise la distance en partant de 0 en calculant le score à chaque étape
        mat[0][0]=0
        for i in range (1,y) :
            for j in range (1,x): 
                    dia = mat[j-1][i-1] + match(a[j-1],b[i-1])
                    #déplacement vertical ou horizontal entraine un gap et donc une pénalité de 1
                    hor = mat[i-1][j] + 1 
                    ver = mat[i][j-1] + 1
                    mat[i][j] = min(dia, hor, ver) #on essaie de minimiser la distance 
        return mat
        print(mat)

#calculons maintenant la distance en partant de la fin, en remontant la matrice 
    def distance(self,a,b,mat) :
        #initialisation au coin au bas à gauche 
        i=len(a)
        j=len(b)
        global top, bottom, s1, s2
        top =''
        s1 =''
        bottom =''
        s2 = ''

        while i > 0 and j> 0 : 
            note_act = mat[j][i]
            note_dia = mat[j-1][i-1]
            note_ver = mat[j-1][i]
            note_hor = mat[j][i-1]
            
            if note_act == note_dia + match(a[i-1], b[j-1]) : #on peut remonter par la diagonale 
                s1 = a[i-1]
                s2 = b[j-1]
                i,j = i-1,j-1
                
            elif note_act == note_ver + 1:
                s1 = str(a[i-1])
                s2 = '-'
                i -= 1

            elif note_act == note_hor + 1:
                s1 = '-'
                s2 = str(b[j-1])
                j -= 1
            
            top += s1
            bottom += s2

            #Attention , si jamais j== 0 avant i, on continue à bouger de manière verticale (même chose sur j ensuite)
        while i > 0:
            s1,s2 = a[i-1],'='
            top += s1
            bottom += s2
            i -= 1
        while j > 0:
            s1,s2 = '=',b[j-1]
            top += s1
            bottom += s2
            j -= 1
    
        top = top[::-1]
        bottom = bottom[::-1]
        print(top)
        print(bottom)
        
        dist = 0
        for i in range(len(top)):
            s1 = top[i]
            s2 = bottom[i]
            if not s1 == s2:
                dist += 1
    
        return dist
        print(dist)
        return top
        print(top)
        return bottom
        print(bottom)

ruler = Ruler("TCGCA","TCCA")
print(ruler.compute("TCGCA","TCCA"))
print(ruler.distance("TCGCA","TCCA",ruler.compute("TCGCA","TCCA")))



        

