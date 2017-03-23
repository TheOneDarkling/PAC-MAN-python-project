#########PAC ##########
from tkinter import *
from math import *
import constantes
import menu

choixUtilisateur = constantes.STOP

direction = constantes.STOP
caseX = 9
caseY = 15
x = caseX*constantes.tailleTile
y = caseY*constantes.tailleTile

caseXAvant = caseX #servent a voir si la matrice doit changer
caseYAvant = caseY
typeDeCaseAvant = 0 # Permet de remettre la bonne case dans la matrice
choixDirection = True

CASE_DEPL = [0, 3, 4]

nbPacGommeEat = 0

timer = 0
cpt = 0
img = 0



###Deplacement###
def init(affichage):
	import ressources
	pacman = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.pctest)
	return pacman




def gestion(affichage,pacman,jeu, listePacGommes, fen):
	global x, y, caseXAvant, caseYAvant, caseX, caseY, choixDirection, direction, timer
	
	caseXAvant = caseX #servent a voir si la matrice doit changer
	caseYAvant = caseY
	
	################
	# Actualise les coord avant  le deplacement
	################
	
	x, y = affichage.coords(pacman)
	
	if (x <= (caseX*constantes.tailleTile-constantes.tailleTile/2) or x >= (caseX+1)*constantes.tailleTile+((constantes.tailleTile/2)+5)):
		caseX = floor(x/constantes.tailleTile)
		
	if (y <= (caseY*constantes.tailleTile-constantes.tailleTile/2) or y >= (caseY+1)*constantes.tailleTile+((constantes.tailleTile/2)+5)):
		caseY = floor(y/constantes.tailleTile)
	
	#GERER direction
	
	direction = gestionDirection(jeu)
		
	animation(affichage, pacman)
	
	################
	# Avance
	################
	
	
	if direction == constantes.HAUT:
		affichage.move(pacman, 0, -1)
	elif direction == constantes.BAS:
		affichage.move(pacman, 0, 1)
	elif direction == constantes.DROITE:
		affichage.move(pacman, 1, 0)
	elif direction == constantes.GAUCHE:
		affichage.move(pacman, -1, 0)
	else:
		affichage.move(pacman, 0, 0)
		
		
		
	################
	#Gestion matrice
	################

	if caseX != caseXAvant or caseY != caseYAvant:
		changerMatrice(jeu, affichage, listePacGommes, fen)

	
	



def changerMatrice(jeu, affichage, listePacGommes, fen):
	global caseXAvant, caseYAvant, caseY, caseX, typeDeCaseAvant, nbPacGommeEat
	
	jeu[caseYAvant][caseXAvant] = typeDeCaseAvant
	typeDeCaseAvant = jeu[caseY][caseX]
	
	if typeDeCaseAvant == 3 or typeDeCaseAvant == 4: #il y a une pacgomme ou une SUPER pacgomme
		if typeDeCaseAvant == 4:
			constantes.superMode = True
			
		nbPacGommeEat += 1
		affichage.delete(fen, listePacGommes[caseY][caseX])
		typeDeCaseAvant = 0
		
		
	jeu[caseY][caseX] = 2
	print(nbPacGommeEat)




def go_left(event =None):
	global choixUtilisateur
	choixUtilisateur = constantes.GAUCHE
	
	
def go_right(event =None):
	global choixUtilisateur
	choixUtilisateur = constantes.DROITE

	
def go_up(event =None):
	global choixUtilisateur
	choixUtilisateur = constantes.HAUT
	menu.menuHaut = True
	

def go_down(event =None):
	global choixUtilisateur
	choixUtilisateur = constantes.BAS
	menu.menuBas = True
	
	
def gestionDirection(jeu):
	global direction
	
	dirPossible = []
	dirPossible.clear()
	
	if jeu[caseY][caseX+1] in CASE_DEPL:
		dirPossible.append(constantes.DROITE)
	if jeu[caseY][caseX-1] in CASE_DEPL:
		dirPossible.append(constantes.GAUCHE)
	if jeu[caseY-1][caseX] in CASE_DEPL:
		dirPossible.append(constantes.HAUT)
	if jeu[caseY+1][caseX] in CASE_DEPL:
		dirPossible.append(constantes.BAS)
	
	if choixUtilisateur in dirPossible:
		return choixUtilisateur
	else:
		if direction == constantes.BAS and jeu[caseY+1][caseX] in CASE_DEPL:
			return direction
		elif direction == constantes.HAUT and jeu[caseY-1][caseX] in CASE_DEPL:
			return direction
		elif direction == constantes.DROITE and jeu[caseY][caseX+1] in CASE_DEPL:
			return direction
		elif direction == constantes.GAUCHE and jeu[caseY][caseX-1] in CASE_DEPL:
			return direction
		





def positionX():
	return caseX
	
def positionY():
	return caseY
	
	
	
def animation(affichage, pacman):
	global timer, cpt, img
	import ressources
	
	
	#timer
	if cpt >= 8:
		timer = 0
		cpt = 0 
		
	if timer >= 7:
		cpt += 1
		img = timer - cpt
	else:
		timer += 1
		cpt = 2
		img = timer
	#
	
	if direction == constantes.STOP:
		affichage.itemconfig(pacman, image=ressources.pctest)
	elif direction == constantes.BAS:
		affichage.itemconfig(pacman, image=ressources.pacmanD[img])
	elif direction == constantes.HAUT:
		affichage.itemconfig(pacman, image=ressources.pacmanU[img])
	elif direction == constantes.DROITE:
		affichage.itemconfig(pacman, image=ressources.pacmanR[img])
	elif direction == constantes.GAUCHE:
		affichage.itemconfig(pacman, image=ressources.pacmanL[img])
		
		
	
	
	
	
	
	
	
	
	
	
	
