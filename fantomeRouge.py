
from tkinter import *
from math import *
import constantes

#### ATTRIBUTS

direction = constantes.DROITE

caseX = 9
caseY = 7
x = caseX*constantes.tailleTile
y = caseY*constantes.tailleTile


caseXAvant = caseX #servent a voir si la matrice doit changer
caseYAvant = caseY
typeDeCaseAvant = 0 # Permet de remettre la bonne case dans la matrice
choixDirection = True


pacmanCaseX = 9 # pour les test
pacmanCaseY = 15

CASE_DEPL = [0, 3, 4]

blocageBas = False # Evite que le fantome sois bloqué
blocageHaut = False
derniereDirection = constantes.STOP


#### Fonctions

def init(affichage):
	import ressources
	blinky = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.ghr)
	return blinky
	
	
	

def gestion(affichage, blinky, jeu):
	global x, y, caseXAvant, caseYAvant, caseX, caseY, choixDirection
	
	caseXAvant = caseX #servent a voir si la matrice doit changer
	caseYAvant = caseY
	
	################
	# Actualise les coord avant  le deplacement
	################
	
	x, y = affichage.coords(blinky)
	
	if (x <= (caseX*constantes.tailleTile-constantes.tailleTile/2) or x >= (caseX+1)*constantes.tailleTile+((constantes.tailleTile/2)+5)):
		caseX = floor(x/constantes.tailleTile)
		
	if (y <= (caseY*constantes.tailleTile-constantes.tailleTile/2) or y >= (caseY+1)*constantes.tailleTile+((constantes.tailleTile/2)+5)):
		caseY = floor(y/constantes.tailleTile)

	
	################
	# Choisis la direction
	################
	
	if choixDirection:
		gestionDirection(jeu)
		choixDirection = False
	
	################
	# Avance
	################
	
	
	if direction == constantes.HAUT:
		affichage.move(blinky, 0, -1)
	elif direction == constantes.BAS:
		affichage.move(blinky, 0, 1)
	elif direction == constantes.DROITE:
		affichage.move(blinky, 1, 0)
	elif direction == constantes.GAUCHE:
		affichage.move(blinky, -1, 0)
	else:
		affichage.move(blinky, 0, 0)
		
		
	################
	#Gestion matrice
	################

	if caseX != caseXAvant or caseY != caseYAvant:
		changerMatrice(jeu)
		choixDirection = True
		
	
	
	
	
	
		
def changerMatrice(jeu):
	global caseXAvant, caseYAvant, caseY, caseX, typeDeCaseAvant
	
	jeu[caseYAvant][caseXAvant] = typeDeCaseAvant
	typeDeCaseAvant = jeu[caseY][caseX]
	jeu[caseY][caseX] = 5
	
	
	
	
	
	
	
	
def gestionDirection(jeu):
	global direction
	
	dirPossible = []
	if jeu[caseY][caseX+1] in CASE_DEPL:
		dirPossible.append(constantes.DROITE)
	if jeu[caseY][caseX-1] in CASE_DEPL:
		dirPossible.append(constantes.GAUCHE)
	if jeu[caseY-1][caseX] in CASE_DEPL:
		dirPossible.append(constantes.HAUT)
	if jeu[caseY+1][caseX] in CASE_DEPL:
		dirPossible.append(constantes.BAS)

	direction = choixDeDirection(dirPossible)





def choixDeDirection(dirPossible):
	return constantes.STOP



