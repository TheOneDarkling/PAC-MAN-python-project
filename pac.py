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
	bouche = 3

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
		if bouche ==0 :
			affichage.itemconfig(pacman,image=ressources.pcu1)
				
		elif bouche ==1 :
			affichage.itemconfig(pacman,image=ressources.pcu2)
				
		elif bouche == 2:
			affichage.itemconfig(pacman,image=ressources.pcu3)
			
		elif bouche == 3:
			affichage.itemconfig(pacman,image=ressources.pcu4)
			
		elif bouche == 4:
			affichage.itemconfig(pacman,image=ressources.pcu5)
				
		elif bouche == 5:
			affichage.itemconfig(pacman,image=ressources.pcu6)
				
		elif bouche == 6:
			affichage.itemconfig(pacman,image=ressources.pcu7)
			
		elif bouche == 7:
			affichage.itemconfig(pacman,image=ressources.pcu7)
			bouche = 0	
		bouche = bouche + 1	
		affichage.move(pacman,0,-1)
		
	elif direction == 1:
		if bouche ==0 :
			affichage.itemconfig(pacman,image=ressources.pcd1)
			bouche = bouche + 1	
		elif bouche ==1 :
			affichage.itemconfig(pacman,image=ressources.pcd2)
			bouche = bouche + 1	
		elif bouche == 2:
			affichage.itemconfig(pacman,image=ressources.pcd3)
			bouche = bouche + 1	
		elif bouche == 3:
			affichage.itemconfig(pacman,image=ressources.pcd4)
			bouche = bouche + 1	
		elif bouche == 4:
			affichage.itemconfig(pacman,image=ressources.pcd5)
			bouche = bouche + 1	
		elif bouche == 5:
			affichage.itemconfig(pacman,image=ressources.pcd6)
			bouche = bouche + 1	
		elif bouche == 6:
			affichage.itemconfig(pacman,image=ressources.pcd7)
			bouche = bouche + 1	
		elif bouche == 7:
			affichage.itemconfig(pacman,image=ressources.pcd7)
			bouche = 0

		bouche = bouche + 1
		affichage.move(pacman,0,1)
		
		
	elif direction == 2:
		affichage.itemconfig(pacman,image=ressources.pcr1)
		affichage.move(pacman,1,0)
		
	elif direction == 3:
		affichage.itemconfig(pacman,image=ressources.pcl1)
		affichage.move(pacman,-1,0)
	else:
		print ("rien")


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
		direction = 4
		
	elif direction == constantes.BAS and jeu[caseY+1][caseX] == 1: # SI MUR A BAS
		direction = 4
			
		
	elif direction == constantes.DROITE and jeu[caseY][caseX+1] == 1: # SI MUR A DROITE
		direction = 4
		
	elif direction == constantes.GAUCHE and jeu[caseY][caseX-1] == 1: # SI MUR A GAUCHE
		direction = 4
	
