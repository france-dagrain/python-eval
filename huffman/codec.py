import sys, string


text =  "a dead dad ceded a bad babe a beaded abaca bed"
codes   = {}

class TreeBuilder : 

    def __init__(self, text): 
        self.text = text

#création d'un dictionnaire des fréquences

    def frequence (self,text) :
        freq = {}
        for i in text :
            freq[i] = freq.get(i,0) + 1
        return freq
#on améliore ce dictionnaire avec en rangeant les lettres et leurs fréquences dans un tuple
    
    def frequence_rangee(self, text) :
        dic = self.frequence(text)
        lettre = dic.keys()
        tuples = []
        for i in lettre :
            tuples.append((dic[i],i))
        tuples.sort(key=lambda t: t[0])
        return tuples
# on peut maintenant construire l'arbre en combinant les noeuds qui ont les plus petites fréquences
    def construction_arbre(self, text) :
        global trees
        tuples = self.frequence_rangee(text)
        while len(tuples) > 1 :
            deux_petites_freq = tuple(tuples[0:2])                 
            le_reste  = tuples[2:]                          
            combinaison = deux_petites_freq[0][0] + deux_petites_freq[1][0]    
            tuples   = le_reste + [(combinaison,deux_petites_freq)]     
            tuples.sort(key=lambda t: t[0])
            trees =tuples[0]
        return trees
        

# Notre arbre est maintenant construit : on peut en extraire le code. 

class Codec : 

    def __init__ (self, binary_tree) : 
        self.binary_tree = binary_tree

# crée l'arbre mais sans les fréquences qui ne nous interesse plus. 
    def tree(self, binary_tree) :
        i = binary_tree[1]                                    
        if type(i) == type("") : 
            return i              
        else : 
            return (self.tree(i[0]), self.tree(i[1]))
    
 # chaque lettre ensuite liée à un code binaire. Pour cela, on va suivre le chemin grâce à la variable "che"  qui stocke l'information gauche droite
    def table_de_code(self, node, che=""):
        global codes
        if type(node) == type(""):
            codes[node]=che
        else:
            self.table_de_code(node[0],che+"0")
            self.table_de_code(node[1],che+"1")   
        return codes
# il ne reste plus qu'à utiliser la fonction encode pour encoder
    def encode(self, str) :
        global codes
        message = ""
        for l in str : message += codes[l]
        return message


builder = TreeBuilder(text)

binary_tree = builder.construction_arbre(text)
#print(binary_tree)
codec = Codec(binary_tree)
arbre = codec.tree(binary_tree)
#print(arbre)
code= codec.table_de_code(arbre)
print (code)
encoded = codec.encode(text)
print(encoded)
# malheureusement je n'arrive pas à décoder ce qui est un comble. Je suis bloquée par des itérations infinies. 