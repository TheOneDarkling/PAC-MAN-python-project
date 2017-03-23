
from tkinter import *
from math import *
import random
import constantes
import pac


#### ATTRIBUTS

direction = constantes.DROITE

caseX = 8
caseY = 9
x = caseX*constantes.tailleTile
y = caseY*constantes.tailleTile


caseXAvant = caseX #servent a voir si la matrice doit changer
caseYAvant = caseY
typeDeCaseAvant = 0 # Permet de remettre la bonne case dans la matrice
choixDirection = True


pacmanCaseX = 9 # pour les test
pacmanCaseY = 15

CASE_DEPL = [0, 3, 4, 2, 5, 6, 7, 8]

blocageBas = False # Evite que le fantome sois bloqué
blocageHaut = False
derniereDirection = constantes.STOP

antiDemiTour = False

#### Fonctions

def init(affichage):
	import ressources
	clyde = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.gho)
	return clyde




def gestion(affichage, clyde, jeu):
	global x, y, caseXAvant, caseYAvant, caseX, caseY, choixDirection
	
	caseXAvant = caseX #servent a voir si la matrice doit changer
	caseYAvant = caseY
	
	################
	# Actualise les coord avant  le deplacement
	################
	
	x, y = affichage.coords(clyde)
	
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
	
	vit = constantes.vitesseFantome
	
	if direction == constantes.HAUT:
		affichage.move(clyde, 0, -vit)
	elif direction == constantes.BAS:
		affichage.move(clyde, 0, vit)
	elif direction == constantes.DROITE:
		affichage.move(clyde, vit, 0)
	elif direction == constantes.GAUCHE:
		affichage.move(clyde, -vit, 0)
	else:
		affichage.move(clyde, 0, 0)
		
		
	################
	#Gestion matrice
	################

	if caseX != caseXAvant or caseY != caseYAvant:
		choixDirection = True
		changerMatrice(jeu)
		
	
	if direction == constantes.STOP:
		choixDirection = True
		
	return True
		
	
	
	
	
	
		
def changerMatrice(jeu):
	global caseXAvant, caseYAvant, caseY, caseX, typeDeCaseAvant
	
	jeu[caseYAvant][caseXAvant] = typeDeCaseAvant
	typeDeCaseAvant = jeu[caseY][caseX]
	
	"""if typeDeCaseAvant == 2: # Si le fantome touche pacman
		constantes.partiePerdu = True
	"""
		
		
	if typeDeCaseAvant == 5 or typeDeCaseAvant == 7 or typeDeCaseAvant == 6 : # Si le fantome touche un autre fantome
		typeDeCaseAvant = 0
		
	jeu[caseY][caseX] = 8

	
	
	
	
	
	
	
	
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
	dirPossible.clear()





def choixDeDirection(dirPossible):
	""" Ce fantome se deplace de maniere aléatoire"""
	global direction, antiDemiTour
	
	if len(dirPossible) > 2 or not(direction in dirPossible):
		varAlea = random.randrange(len(dirPossible))
		direction = dirPossible[varAlea]
	
	
	return direction
	



def spawn(clyde, affichage, fen, jeu):
	import ressources
	global caseX, caseY, typeDeCaseAvant
	affichage.delete(fen, clyde)
	caseX = 9
	caseY = 7
	typeDeCaseAvant = jeu[caseY][caseX]
	jeu[caseY][caseX] = 8
	x = caseX*constantes.tailleTile
	y = caseY*constantes.tailleTile
	blinky = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.gho)
	return blinky
	


def directionOpp(direction):
	if direction == constantes.BAS:
		return constantes.HAUT
	elif direction == constantes.HAUT:
		return constantes.BAS
	elif direction == constantes.DROITE:
		return constantes.GAUCHE
	elif direction == constantes.GAUCHE:
		return constantes.DROITE



