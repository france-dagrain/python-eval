import numpy as np
from colorama import Fore, Style
import os
os.chdir("C:/Users/Lenovo/Documents/GitHub/python-eval/needleman_wunsch")
mon_fichier = open("DATASET.txt", "r")
#on le lit avec read.
import ruler
from ruler import Ruler


contenu = mon_fichier.read()
contenu = contenu.split()
print(contenu)
i=0
while i < len(contenu) : 
    ruler = Ruler(contenu[i], contenu[i+1])
    print(ruler.distance(contenu[i], contenu[i+1],ruler.compute(contenu[i], contenu[i+1])))
    i +=2


#python3 bundle.py DATASET

