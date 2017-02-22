
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


pacmanCaseX = 5 # pour les test
pacmanCaseY = 15


blocage = False # Evite que le fantome sois bloqué
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
	
	########################
	#Test si il y  a un mur
	########################
	
	
	if direction == constantes.HAUT and jeu[caseY-1][caseX] == 1: # SI MUR A HAUT
		if jeu[caseY][caseX+1] == 1:
			direction = constantes.GAUCHE
		elif jeu[caseY][caseX-1] == 1:
			direction = constantes.DROITE
		else:
			direction = choixDeDirection([constantes.GAUCHE, constantes.DROITE, constantes.BAS])
			###### CHOIX GAUCHE OU DROITE OU BAS
		
	elif direction == constantes.BAS and jeu[caseY+1][caseX] == 1: # SI MUR A BAS
		if jeu[caseY][caseX+1] == 1:
			direction = constantes.GAUCHE
		elif jeu[caseY][caseX-1] == 1:
			direction = constantes.DROITE
		else:
			direction = choixDeDirection([constantes.GAUCHE, constantes.DROITE, constantes.HAUT])
			###### CHOIX GAUCHE OU DROITE OU HAUT
			
		
	elif direction == constantes.DROITE and jeu[caseY][caseX+1] == 1: # SI MUR A DROITE
		if jeu[caseY-1][caseX] == 1:
			direction = constantes.BAS
		elif jeu[caseY+1][caseX] == 1:
			direction = constantes.HAUT
		else:
			direction = choixDeDirection([constantes.GAUCHE, constantes.BAS, constantes.HAUT])
			###### CHOIX HAUT OU BAS OU GAUCHE
		
	elif direction == constantes.GAUCHE and jeu[caseY][caseX-1] == 1: # SI MUR A GAUCHE
		if jeu[caseY-1][caseX] == 1:
			direction = constantes.BAS
		elif jeu[caseY+1][caseX] == 1:
			direction = constantes.HAUT
		else:
			direction = choixDeDirection([constantes.DROITE, constantes.BAS, constantes.HAUT])
			###### CHOIX HAUT OU BAS OU DROITE
	
	
	
	##############################
	#Test s'il y a un choix de dir
	##############################
	
	

	if direction == constantes.HAUT and jeu[caseY-1][caseX] == 0: # Croisement direction = HAUT
		if jeu[caseY][caseX+1] == 0  and jeu[caseY][caseX-1] == 0:
			direction = choixDeDirection([constantes.DROITE, constantes.BAS, constantes.HAUT, constantes.GAUCHE])
			###### CHOIX DROITE OU GAUCHE OU HAUT OU BAS
			
		elif jeu[caseY][caseX+1] == 0:
			direction = choixDeDirection([constantes.DROITE, constantes.BAS, constantes.HAUT])
			###### CHOIX DROITE OU HAUT OU BAS

		elif jeu[caseY][caseX-1] == 0:
			direction = choixDeDirection([constantes.BAS, constantes.HAUT, constantes.GAUCHE])
			###### CHOIX GAUCHE OU HAUT OU BAS
			
	elif direction == constantes.BAS and jeu[caseY+1][caseX] == 0:  # Croisement direction = BAS
		if jeu[caseY][caseX+1] == 0  and jeu[caseY][caseX-1] == 0:
			direction = choixDeDirection([constantes.DROITE, constantes.BAS, constantes.HAUT, constantes.GAUCHE])
			###### CHOIX DROITE OU GAUCHE OU BAS OU HAUT
			
		elif jeu[caseY][caseX+1] == 0:
			direction = choixDeDirection([constantes.DROITE, constantes.BAS, constantes.HAUT])
			###### CHOIX DROITE OU BAS OU HAUT

		elif jeu[caseY][caseX-1] == 0:
			direction = choixDeDirection([constantes.BAS, constantes.HAUT, constantes.GAUCHE])
			###### CHOIX GAUCHE OU BAS OU HAUT

	elif direction == constantes.DROITE and jeu[caseY][caseX+1] == 0:  # Croisement direction = DROITE
		if jeu[caseY+1][caseX] == 0  and jeu[caseY-1][caseX] == 0:
			direction = choixDeDirection([constantes.DROITE, constantes.BAS, constantes.HAUT, constantes.GAUCHE])
			###### CHOIX HAUT OU BAS OU DROITE
			
		elif jeu[caseY+1][caseX] == 0:
			direction = choixDeDirection([constantes.DROITE, constantes.BAS, constantes.GAUCHE])
			###### CHOIX BAS OU DROITE OU GAUCHE

		elif jeu[caseY-1][caseX] == 0:
			direction = choixDeDirection([constantes.DROITE, constantes.HAUT, constantes.GAUCHE])
			###### CHOIX HAUT OU DROITE OU GAUCHE
			
	elif direction == constantes.GAUCHE and jeu[caseY][caseX-1] == 0:  # Croisement direction = GAUCHE
		if jeu[caseY+1][caseX] == 0  and jeu[caseY-1][caseX] == 0:
			direction = choixDeDirection([constantes.DROITE, constantes.BAS, constantes.HAUT, constantes.GAUCHE])
			###### CHOIX HAUT OU BAS OU GAUCHE OU DROITE
			
		elif jeu[caseY+1][caseX] == 0:
			direction = choixDeDirection([constantes.DROITE, constantes.BAS, constantes.GAUCHE])
			###### CHOIX BAS OU GAUCHE OU DROITE

		elif jeu[caseY-1][caseX] == 0:
			direction = choixDeDirection([constantes.DROITE, constantes.HAUT, constantes.GAUCHE])
			###### CHOIX HAUT OU GAUCHE OU DROITE











def choixDeDirection(dirPossible):
	global blocage, derniereDirection
	
	distanceX = pacmanCaseX - caseX
	distanceY = pacmanCaseY - caseY
	
	nbCaseDistX = abs(distanceX)
	nbCaseDistY = abs(distanceY)
	
	if nbCaseDistX > nbCaseDistY:
		if distanceX > 0:
			if constantes.DROITE in dirPossible: #test si DROITE est possible
				return constantes.DROITE
			else:  #Sinon on regarde les Y
				if distanceY > 0:
					return constantes.BAS
				else:
					return constantes.HAUT
		else:
			if constantes.GAUCHE in dirPossible: #test si GAUCHE est possible
				return constantes.GAUCHE
			else:  #Sinon on regarde les Y
				if distanceY > 0:
					return constantes.BAS
				else:
					return constantes.HAUT
			
			
	elif nbCaseDistX < nbCaseDistY:
		if distanceY > 0:
			if constantes.BAS in dirPossible: #test si BAS est possible
				return constantes.BAS
			else:  #Sinon on regarde les X
				if distanceX > 0:
					return constantes.DROITE
				else:
					return constantes.GAUCHE
		else:
			if constantes.HAUT in dirPossible: #test si HAUT est possible
				return constantes.HAUT
			else:  #Sinon on regarde les X
				if distanceX > 0:
					return constantes.DROITE
				else:
					return constantes.GAUCHE
	
	"""
	
	directionOptimale = []
	
	if distanceX >= distanceY:
		directionOptimale.append(constantes.DROITE)
		if distanceY > 0:
			directionOptimale.append(constantes.BAS)
		else:
			directionOptimale.append(constantes.HAUT)
	elif distanceX <= distanceY:
		directionOptimale.append(constantes.BAS)
		if distanceX > 0:
			directionOptimale.append(constantes.DROITE)
		else:
			directionOptimale.append(constantes.GAUCHE)
			
	if directionOptimale[0] in dirPossible:
		blocage = False
		return directionOptimale[0]
	elif not blocage:
		blocage = True
		derniereDirection = directionOptimale[1]
		return directionOptimale[1]
	else:
		return derniereDirection

	"""








