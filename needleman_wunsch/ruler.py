
#from needleman_wunsch import Ruler
import numpy as np
from colorama import Fore, Style




# Deux fonctions préalbles : définir un match (avec possibilité de changer la valeur des bonus/malus) et mettre du texte en rouge 

def match(m,n,bonus=0,malus=1) :
        if m==n :
            return bonus
        else : 
            return malus

def red_text(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}" 


#codage de ma classe Ruler
class Ruler: 

    def __init__ (self,a,b) : 
        self.a = a
        self.b = b           


#1ère étape : construction de ma matrice de taille (y,x) qui tente de minimiser le score. dans notre cas, un écart qui augmente la distance de 1
    def compute(self,a,b,ecart=1) :
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
        #remplir le reste de la matrice en trouvant le chemin qui minimise la distance en partant de 0 et en calculant les différents scores à chaque étape
        mat[0][0]=0
        for i in range (1,y) :
            for j in range (1,x): 
                    dia = mat[i-1][j-1] + match(a[j-1],b[i-1])
                    #déplacement vertical ou horizontal entraine un gap et donc une pénalité de 1
                    hor = mat[i-1][j] + ecart 
                    ver = mat[i][j-1] + ecart
                    mat[i][j] = min(dia, hor, ver) #on essaie de minimiser la distance 
        return mat
        #print(mat)

#calculons maintenant la distance en partant de la fin, en remontant la matrice 
    def distance(self, a, b, mat) :
        #initialisation au coin au bas à gauche 
        i=len(b)
        j=len(a)
        global top, bottom, s1, s2
        top =''
        s1 =''
        bottom =''
        s2 = ''

        while i > 0 and j> 0 : 
            note_act = mat[i][j]
            note_dia = mat[i-1][j-1]
            note_ver = mat[i][j-1]
            note_hor = mat[i-1][j]
            
            if note_act == note_dia + match(a[j-1], b[i-1]) : #on peut remonter par la diagonale 
                s1 = a[j-1]
                s2 = b[i-1]
                i,j = i-1,j-1
                
            elif note_act == note_ver + 1:
                s1 = str(a[j-1])
                s2 = '='
                j -= 1

            elif note_act == note_hor + 1:
                s1 = '='
                s2 = str(b[i-1])
                i -= 1
            
            top += s1
            bottom += s2

            #Attention , si jamais j== 0 avant i, on continue à bouger de manière verticale (même chose sur j ensuite)
        while j > 0:
            s1,s2 = a[j-1],'='
            top += s1
            bottom += s2
            j -= 1
        while i > 0:
            s1,s2 = '=',b[i-1]
            top += s1
            bottom += s2
            i -= 1
    
        top = top[::-1]
        bottom = bottom[::-1]
    #mise en couleur des éléments différents 
        top = list(top)
        bottom = list(bottom)
        
        for i in range (0,max([len(a),len(b)])) : 
            if top[i] != bottom[i] :
                top[i] = red_text(top[i])
                bottom [i]= red_text(bottom[i])
        top =" ".join(top)
        bottom = " ".join(bottom)

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
        return bottom
        



ruler = Ruler("abcdefghi", "abcdfghi")

#print(ruler.distance("abcdefghi", "abcdfghj",ruler.compute("abcdefghi", "abcdfghj")))

ruler.compute("abcdefghi", "abcdfghi")
print(ruler.distance("abcdefghi", "abcdfghi",ruler.compute("abcdefghi", "abcdfghi")))


        

