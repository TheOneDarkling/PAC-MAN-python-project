
from tkinter import *

import constantes

#### ATTRIBUTS

direction = constantes.HAUT

caseX = 9
caseY = 7
x = caseX*constantes.tailleTile
y = caseY*constantes.tailleTile
 

#### Fonctions

def init(affichage):
	import ressources
	blinky = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.ghr)
	
	
	
	


def gestion():
	return 0;
	
	
