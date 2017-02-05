
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


pacmanCaseX = 8
pacmanCaseY = 8


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
		print("CHOIX DIRECTION")
	
	
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
	
	########################
	#Test si il y  a un mur
	########################
	
	
	if direction == constantes.HAUT and jeu[caseY-1][caseX] == 1: # SI MUR A HAUT
		if jeu[caseY][caseX+1] == 1:
			direction = constantes.GAUCHE
		elif jeu[caseY][caseX-1] == 1:
			direction = constantes.DROITE
		else:
			direction = constantes.GAUCHE
			###### CHOIX GAUCHE OU DROITE
		
	elif direction == constantes.BAS and jeu[caseY+1][caseX] == 1: # SI MUR A BAS
		if jeu[caseY][caseX+1] == 1:
			direction = constantes.GAUCHE
		elif jeu[caseY][caseX-1] == 1:
			direction = constantes.DROITE
		else:
			direction = constantes.GAUCHE
			###### CHOIX GAUCHE OU DROITE
			
		
	elif direction == constantes.DROITE and jeu[caseY][caseX+1] == 1: # SI MUR A DROITE
		if jeu[caseY-1][caseX] == 1:
			direction = constantes.BAS
		elif jeu[caseY+1][caseX] == 1:
			direction = constantes.HAUT
		else:
			direction = constantes.HAUT
			###### CHOIX HAUT OU BAS
		
	elif direction == constantes.GAUCHE and jeu[caseY][caseX-1] == 1: # SI MUR A GAUCHE
		if jeu[caseY-1][caseX] == 1:
			direction = constantes.BAS
		elif jeu[caseY+1][caseX] == 1:
			direction = constantes.HAUT
		else:
			direction = constantes.HAUT
			###### CHOIX HAUT OU BAS
	
	
	
	##############################
	#Test s'il y a un choix de dir
	##############################
	
	

	if direction == constantes.HAUT and jeu[caseY-1][caseX] == 0: # Croisement direction = HAUT
		if jeu[caseY][caseX+1] == 0  and jeu[caseY][caseX-1] == 0:
			direction = constantes.HAUT
			###### CHOIX DROITE OU GAUCHE OU HAUT
			
		elif jeu[caseY][caseX+1] == 0:
			direction = constantes.HAUT
			###### CHOIX DROITE OU HAUT

		elif jeu[caseY][caseX-1] == 0:
			direction = constantes.HAUT
			###### CHOIX GAUCHE OU HAUT
			
	elif direction == constantes.BAS and jeu[caseY+1][caseX] == 0:  # Croisement direction = HAUT
		if jeu[caseY][caseX+1] == 0  and jeu[caseY][caseX-1] == 0:
			direction = constantes.BAS
			###### CHOIX DROITE OU GAUCHE OU BAS
			
		elif jeu[caseY][caseX+1] == 0:
			direction = constantes.BAS
			###### CHOIX DROITE OU BAS

		elif jeu[caseY][caseX-1] == 0:
			direction = constantes.BAS
			###### CHOIX GAUCHE OU BAS

	elif direction == constantes.DROITE and jeu[caseY][caseX+1] == 0:  # Croisement direction = DROITE
		if jeu[caseY+1][caseX] == 0  and jeu[caseY-1][caseX] == 0:
			direction = constantes.DROITE
			###### CHOIX HAUT OU BAS OU DROITE
			
		elif jeu[caseY+1][caseX] == 0:
			direction = constantes.DROITE
			###### CHOIX BAS OU DROITE

		elif jeu[caseY-1][caseX] == 0:
			direction = constantes.DROITE
			###### CHOIX HAUT OU DROITE
			
	elif direction == constantes.GAUCHE and jeu[caseY][caseX-1] == 0:  # Croisement direction = GAUCHE
		if jeu[caseY+1][caseX] == 0  and jeu[caseY-1][caseX] == 0:
			direction = constantes.GAUCHE
			###### CHOIX HAUT OU BAS OU GAUCHE
			
		elif jeu[caseY+1][caseX] == 0:
			direction = constantes.GAUCHE
			###### CHOIX BAS OU GAUCHE

		elif jeu[caseY-1][caseX] == 0:
			direction = constantes.GAUCHE
			###### CHOIX HAUT OU GAUCHE











