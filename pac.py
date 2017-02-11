#########PAC ##########
from tkinter import *
from math import *
import constantes



direction = 3
caseX = 9
caseY = 15
x = caseX*constantes.tailleTile
y = caseY*constantes.tailleTile

caseXAvant = caseX #servent a voir si la matrice doit changer
caseYAvant = caseY
typeDeCaseAvant = 0 # Permet de remettre la bonne case dans la matrice
choixDirection = True




###Deplacement###
def gestionpac(affichage):
	import ressources
	pacman = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.pcl5)
	return pacman

def move(affichage,pacman,jeu):
	import ressources	
	global direction, image, choixDirection
	global x, y, caseXAvant, caseYAvant, caseX, caseY, choixDirection

	caseXAvant = caseX #servent a voir si la matrice doit changer
	caseYAvant = caseY

	x, y = affichage.coords(pacman)
	
	if (x <= (caseX*constantes.tailleTile-constantes.tailleTile/2) or x >= (caseX+1)*constantes.tailleTile+((constantes.tailleTile/2)+5)):
		caseX = floor(x/constantes.tailleTile)
		
	if (y <= (caseY*constantes.tailleTile-constantes.tailleTile/2) or y >= (caseY+1)*constantes.tailleTile+((constantes.tailleTile/2)+5)):
		caseY = floor(y/constantes.tailleTile)

	if choixDirection:
		gestionDirection(jeu)
		choixDirection = False

	if direction == 0:
		affichage.itemconfig(pacman,image=ressources.pcu1)
		affichage.move(pacman,0,-1)
		
	elif direction == 1:
		affichage.itemconfig(pacman,image=ressources.pcd1)
		affichage.move(pacman,0,1)
		
		
	elif direction == 2:
		affichage.itemconfig(pacman,image=ressources.pcr1)
		affichage.move(pacman,1,0)
		
	elif direction == 3:
		affichage.itemconfig(pacman,image=ressources.pcl1)
		affichage.move(pacman,-1,0)


	if caseX != caseXAvant or caseY != caseYAvant:
		changerMatrice(jeu)
		choixDirection = True
	
	



def changerMatrice(jeu):
	global caseXAvant, caseYAvant, caseY, caseX, typeDeCaseAvant
	
	jeu[caseYAvant][caseXAvant] = typeDeCaseAvant
	typeDeCaseAvant = jeu[caseY][caseX]
	jeu[caseY][caseX] = 0





def go_left(event =None):
	global direction
	direction = constantes.GAUCHE
	
	
def go_right(event =None):
	global direction
	direction = constantes.DROITE

	
def go_up(event =None):
	global direction
	direction = constantes.HAUT
	

def go_down(event =None):
	global direction
	direction = constantes.BAS
	

		
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
	
