#########PAC ##########
from tkinter import *
from math import *
import constantes



direction = 3
depl = 5
caseX = 9
caseY = 15
x = caseX*constantes.tailleTile
y = caseY*constantes.tailleTile

###Deplacement###
def gestionpac(affichage):
	import ressources
	pacman = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.pcl5)
	return pacman

def move(affichage,pacman):
	import ressources	
	global direction, image
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
	
	
		
		
	
