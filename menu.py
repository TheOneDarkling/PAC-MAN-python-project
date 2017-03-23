from tkinter import *
from math import *
import constantes


menuBas = False
menuHaut = False

selectPrecedent = 0
select = 0

def gestionMenu(fen, affichage, boutons):
	global select, menuBas, menuHaut, selectPrecedent
	
	# Changements dans le menu
	if menuBas:
		if select <= 2:
			select += 1
	elif menuHaut:
		if select > 0:
			select -= 1
			
	menuHaut = False
	menuBas = False
	
	# verif les changements
	
	if select != selectPrecedent:
		selectPrecedent = select
		actuali(fen, affichage, boutons)
		
	#test si le choix est fait
	
	if constantes.valider:
		constantes.valider = False
		if select == 0:
			return constantes.CHOIX_PLAY
		elif select == 1:
			return constantes.CHOIX_HARDMODE
		elif select == 2:
			return constantes.CHOIX_OPTIONS
		elif select == 3:
			return constantes.CHOIX_QUITTER
		
	constantes.valider = False
	return constantes.CHOIX_NONE
		
	
		
		
def actuali(fen, affichage, boutons):
	import ressources
	
	for i in range(4):
		
		if select == i:
			affichage.itemconfig(boutons[i], image=ressources.boutonA[i])
		else:
			affichage.itemconfig(boutons[i], image=ressources.boutonD[i])
	
	
	
	
	
	
	
	

