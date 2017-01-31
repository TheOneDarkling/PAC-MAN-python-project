###test commit
from tkinter import *

	
def afficherJeu():
	print(jeu)
	
	

def dessinerMap():
	global jeu
	for i in range(nbTilesLargeur+1):
		for j in range(nbTilesHauteur+1):
			if jeu[j][i] == 0:
				affichage.create_image(i*tailleTile, j*tailleTile, image=vide)
			else:
				affichage.create_image(j*tailleTile, i*tailleTile, image=mur)
	



def play():
	global isPlay, mapCreated
	
	# Cette partie est rafraichie a 60fps
	
	dessinerMap()
	
	#Gere la fin
	

	
	if(isPlay):
		fen.after(17, play)



	

def mapTest():
	global jeu
	
	for i in range(nbTilesLargeur+1):
		for j in range(nbTilesHauteur+1):
			if i == 0 or j == 0 or i == nbTilesHauteur or j == nbTilesLargeur or i == 1 or j == 1 or i == nbTilesHauteur-1 or j == nbTilesLargeur-1:
				jeu[j][i] =1

	
	
	
	
	


#=======================================================================
# PROGRAMME PRINCIPAL ==================================================
#=======================================================================

#Varibles utiles
tailleTile = 16
nbTilesHauteur = 30
nbTilesLargeur = 30

hauteurAffichage = tailleTile * nbTilesHauteur
largeurAffichage = tailleTile * nbTilesLargeur

isPlay = True
mapCreated = False #Flag pour créer la map de base 


#Gestion plateau

jeu = [[0] * (nbTilesLargeur+1) for _ in range(nbTilesHauteur+1)]

mapTest()

afficherJeu()


#Gestion fenetre
fen = Tk()
fen.title("PAC MAN")

affichage = Canvas(fen, width=largeurAffichage, height= hauteurAffichage, bg="black")
affichage.pack(side="top")

#Les différantes TILES
vide = PhotoImage(file ='Tile/void.png')
mur = PhotoImage(file ='Tile/wall.png')


#Gestion menu
playButton = Button(fen, text="Play", command=play)
playButton.pack(side=RIGHT)


fen.mainloop()
