#########PAC ##########
from tkinter import *
from math import *
import constantes



caseX = 9
caseY = 15
x = caseX*constantes.tailleTile
y = caseY*constantes.tailleTile

###Deplacement###


def affichepac(affichage):
	import ressources
	pacman = affichage.create_image(x+(constantes.tailleTile/2), y+(constantes.tailleTile/2), image=ressources.pcl5)	
	return pacman

def img(cpt):
	global image
	if cpt == 0:
		image = can.create_image(x, y, anchor=NW, image=pcl1)
	elif cpt == 1:
		image = can.create_image(x, y, anchor=NW, image=pcr1)
	elif cpt == 2:
		image = can.create_image(x, y, anchor=NW, image=pct1)
	elif cpt == 3:
		image = can.create_image(x, y, anchor=NW, image=pcd1)

def go_left(event =None):
	global x
	x+=depl
	if limite():
		can.delete(image)
		img(3)		
	
		
	
def go_right(event =None):
	global x
	x-=depl
	if limite():
		can.delete(image)
		img(3)
	
		
	

def go_up(event =None):
	global y
	y-=depl
	if limite():
		can.delete(image)
		img(3)	
	
		
	

def go_down(event =None):
	global y
	y+=depl
	if limite():
		
		can.delete(image)
		img(3)
	
def limite():
	print ("dd")