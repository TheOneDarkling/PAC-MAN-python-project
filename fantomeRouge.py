
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


pacmanCaseX = 8
pacmanCaseY = 8


#### Fonctions

def init(affichage):
	import ressources
	blinky = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.ghr)
	return blinky
	
	
	

def gestion(affichage, blinky, jeu):
	global x, y, caseXAvant, caseYAvant, caseX, caseY
	
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
	
	
	gestionDirection(jeu)
	
	
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
	
	
	
	
	
		
def changerMatrice(jeu):
	global caseXAvant, caseYAvant, caseY, caseX, typeDeCaseAvant
	
	jeu[caseYAvant][caseXAvant] = typeDeCaseAvant
	typeDeCaseAvant = jeu[caseY][caseX]
	jeu[caseY][caseX] = 5
	
	
	
	
	
	
def gestionDirection(jeu):
	global direction
	
	#Test si il y  a un mur
	if direction == constantes.HAUT and jeu[caseY-1][caseX] == 1:
		direction = constantes.STOP
	elif direction == constantes.BAS and jeu[caseY+1][caseX] == 1:
		direction = constantes.STOP
	elif direction == constantes.DROITE and jeu[caseY][caseX+1] == 1:
		direction = constantes.STOP
	elif direction == constantes.GAUCHE and jeu[caseY][caseX-1] == 1:
		direction = constantes.STOP

	#else:
	#	direction = constantes.DROITE











