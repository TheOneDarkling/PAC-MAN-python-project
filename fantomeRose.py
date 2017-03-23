
from tkinter import *
from math import *
import constantes
import pac


#### ATTRIBUTS

direction = constantes.DROITE

caseX = 10
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
	pinky = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.ghp)
	return pinky




def gestion(affichage, pinky, jeu):
	global x, y, caseXAvant, caseYAvant, caseX, caseY, choixDirection
	
	caseXAvant = caseX #servent a voir si la matrice doit changer
	caseYAvant = caseY
	
	################
	# Actualise les coord avant  le deplacement
	################
	
	x, y = affichage.coords(pinky)
	
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
	
	vit = constantes.vitesseFantome+0.2
	
	if direction == constantes.HAUT:
		affichage.move(pinky, 0, -vit)
	elif direction == constantes.BAS:
		affichage.move(pinky, 0, vit)
	elif direction == constantes.DROITE:
		affichage.move(pinky, vit, 0)
	elif direction == constantes.GAUCHE:
		affichage.move(pinky, -vit, 0)
	else:
		affichage.move(pinky, 0, 0)
		
		
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

	if typeDeCaseAvant == 8 or typeDeCaseAvant == 5 or typeDeCaseAvant == 7 : # Si le fantome touche un autre fantome
		typeDeCaseAvant = 0
		
	jeu[caseY][caseX] = 6

	
	
	
	
	
	
	
	
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
	
	direction = choixDeDirection(dirPossible, jeu)
	dirPossible.clear()





def choixDeDirection(dirPossible, jeu):
	global derniereDirection
	#pour tendre une embuscade il faur détérminer un point devant pac man
	
	pointEmbu = creationEmbu(dirPossible, jeu)
	
	distanceX = pointEmbu[0] - caseX
	distanceY = pointEmbu[1] - caseY
	
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
	



def spawn(pinky, affichage, fen, jeu):
	import ressources
	global caseX, caseY, typeDeCaseAvant
	affichage.delete(fen, pinky)
	caseX = 9
	caseY = 7
	typeDeCaseAvant = jeu[caseY][caseX]
	jeu[caseY][caseX] = 7
	x = caseX*constantes.tailleTile
	y = caseY*constantes.tailleTile
	pinky = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.ghp)
	return pinky
	


def directionOpp(direction):
	if direction == constantes.BAS:
		return constantes.HAUT
	elif direction == constantes.HAUT:
		return constantes.BAS
	elif direction == constantes.DROITE:
		return constantes.GAUCHE
	elif direction == constantes.GAUCHE:
		return constantes.DROITE





def creationEmbu(dirPossible, jeu):
	ptX = 0
	ptY = 0
	pointEmbu = [ptX, ptY]
	
	dist = 0 # distance de l'embu
	
	
	# cherche le croissement suivant la direction de pacman
	
	if pac.direction == constantes.DROITE or pac.direction == constantes.GAUCHE: ## Deplacement horizontal
		pointEmbu[1] = pac.positionY()
		ptX = pac.positionX()
	else:
		pointEmbu[0] = pac.positionX()
		ptY = pac.positionY()
		
		

	if pac.direction == constantes.HAUT and constantes.HAUT in dirPossible: ## HAUT
		while jeu[ptY-dist][ptX] != 1:
			dist += 1
		pointEmbu[1] = ptY-dist
	elif pac.direction == constantes.HAUT:
		pointEmbu[1] = ptY
		
		
		
	if pac.direction == constantes.BAS and constantes.BAS in dirPossible: ## BAS
		while jeu[ptY+dist][ptX] != 1:
			dist += 1
		pointEmbu[1] = ptY+dist
	elif pac.direction == constantes.BAS:
		pointEmbu[1] = ptY
		
		
		
	if pac.direction == constantes.GAUCHE and constantes.GAUCHE in dirPossible: ## GAUCHE
		while jeu[ptY][ptX-dist] != 1:
			dist += 1
		pointEmbu[0] = ptX-dist
	elif pac.direction == constantes.GAUCHE:
		pointEmbu[0] = ptX	
		
		
		
	if pac.direction == constantes.DROITE and constantes.DROITE in dirPossible: ## DROITE
		while jeu[ptY][ptX+dist] != 1:
			dist += 1
		pointEmbu[0] = ptX+dist
	elif pac.direction == constantes.DROITE:
		pointEmbu[0] = ptX	
	
	
	return pointEmbu
