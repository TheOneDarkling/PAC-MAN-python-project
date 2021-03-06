
from tkinter import *
from math import *
import constantes
import pac

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

CASE_DEPL = [0, 3, 4, 2, 5, 6, 7, 8]

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
	
	vit = constantes.vitesseFantome
	
	if direction == constantes.HAUT:
		affichage.move(blinky, 0, -vit)
	elif direction == constantes.BAS:
		affichage.move(blinky, 0, vit)
	elif direction == constantes.DROITE:
		affichage.move(blinky, vit, 0)
	elif direction == constantes.GAUCHE:
		affichage.move(blinky, -vit, 0)
	else:
		affichage.move(blinky, 0, 0)
		
		
	################
	#Gestion matrice
	################

	if caseX != caseXAvant or caseY != caseYAvant:
		choixDirection = True
		changerMatrice(jeu)
		
	
	if direction == constantes.STOP:
		choixDirection = True
	
		
	
	
	
	
	
		
def changerMatrice(jeu):
	global caseXAvant, caseYAvant, caseY, caseX, typeDeCaseAvant
	
	jeu[caseYAvant][caseXAvant] = typeDeCaseAvant
	typeDeCaseAvant = jeu[caseY][caseX]
	
	"""if typeDeCaseAvant == 2: # Si le fantome touche pacman
		constantes.partiePerdu = True
	"""
	if typeDeCaseAvant == 8 or typeDeCaseAvant == 7 or typeDeCaseAvant == 6 : # Si le fantome touche un autre fantome
		typeDeCaseAvant = 0
		
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
	dirPossible.clear()





def choixDeDirection(dirPossible):
	global derniereDirection

	distanceX = pac.positionX() - caseX
	distanceY = pac.positionY() - caseY
	
	direction = constantes.STOP
	
	if abs(distanceX) > abs(distanceY): # Si plus grande distance en X
		if distanceX > 0 and (constantes.DROITE in dirPossible):
			direction = constantes.DROITE
		elif distanceX > 0: # sinon HAUT ou BAS
			if distanceY > 0 and (constantes.BAS in dirPossible):
				direction = constantes.BAS
			else:
				direction = constantes.HAUT
		elif distanceX < 0 and (constantes.GAUCHE in dirPossible):
			direction = constantes.GAUCHE
		elif distanceX < 0:
			if distanceY > 0 and (constantes.BAS in dirPossible):
				direction = constantes.BAS
			else:
				direction = constantes.HAUT
	elif abs(distanceX) < abs(distanceY): # Si plus grande distance en Y
		if distanceY >= 0 and (constantes.BAS in dirPossible):
			direction = constantes.BAS
		elif distanceY > 0 and (constantes.DROITE in dirPossible):
			if distanceX > 0:
				direction = constantes.DROITE
			else:
				direction = constantes.GAUCHE
		elif distanceY < 0 and (constantes.HAUT in dirPossible):
			direction = constantes.HAUT
		elif distanceY < 0:
			if distanceX > 0 and (constantes.DROITE in dirPossible):
				direction = constantes.DROITE
			else:
				direction = constantes.GAUCHE
	else: # Si meme distance
		if distanceY > 0 and (constantes.BAS in dirPossible):
			direction = constantes.BAS
		elif distanceX > 0 and (constantes.DROITE in dirPossible):
			direction = constantes.DROITE
		elif distanceY < 0 and (constantes.HAUT in dirPossible):
			direction = constantes.BAS
		elif distanceX < 0 and (constantes.GAUCHE in dirPossible):
			direction = constantes.GAUCHE
		else:
			direction = constantes.STOP
		
	derniereDirection = direction
			
	return direction





def spawn(blinky, affichage, fen, jeu):
	import ressources
	affichage.delete(fen, blinky)
	caseX = 9
	caseY = 7
	x = caseX*constantes.tailleTile
	y = caseY*constantes.tailleTile
	blinky = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.ghr)
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



