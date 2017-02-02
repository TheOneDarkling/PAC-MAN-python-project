
from tkinter import *



	
def afficherJeu():		
	print(jeu)



def gestionMap():
	global jeu
	#for i in range(nbTilesLargeur+1):
		#for j in range(nbTilesHauteur+1):
			#if jeu[j][i] == 0:
			#	affichage.create_image(i*tailleTile, j*tailleTile, image=vide)
			#else:
				#affichage.create_image(j*tailleTile, i*tailleTile, image=mur)
	
	



def play():
	global isPlay, mapCreated
	
	# On affiche la map 1 fois
	if not mapCreated:
		affichage.create_image(234, 273, image=background)
		mapCreated = True
	
	
	
	# Cette partie est rafraichie a 60fps
	gestionMap()
	
	
	
	#Gere la fin
	

	
	if(isPlay):
		fen.after(17, play)



def quadrier():
	#Cadriage
	for i in range(nbTilesLargeur):
		affichage.create_line(i*26, 0, i*26, 548, width=1, fill="white")
		
	for j in range(nbTilesHauteur):
		affichage.create_line(0, j*26, 468, j*26, width=1, fill="white")


		
	
	
def etatJeu(): # Affiche la liste qui repertorie l'ensemble des pions
	fen2 = Tk()
	liste = []
	for j in range(nbTilesHauteur):
		for i in range(nbTilesLargeur):
			liste.append(jeu[j][i]) 
			
		chaine = Label(fen2)
		chaine.configure(text=str(liste))
		chaine.pack()
		liste.clear()

	


#=======================================================================
# PROGRAMME PRINCIPAL ==================================================
#=======================================================================

#Varibles utiles
tailleTile = 26
nbTilesHauteur = 21
nbTilesLargeur = 18

hauteurAffichage = tailleTile * nbTilesHauteur
largeurAffichage = tailleTile * nbTilesLargeur

isPlay = True
mapCreated = False #Flag pour créer la map de base 


#Gestion plateau

jeu = [[0] * (nbTilesLargeur) for _ in range(nbTilesHauteur)]

afficherJeu()


#Gestion fenetre
fen = Tk()
fen.title("PAC MAN")

import ressources
background = PhotoImage(file ='ressources/map.png')

affichage = Canvas(fen, width=largeurAffichage, height= hauteurAffichage, bg="WHITE")
affichage.pack(side="top")


#Gestion menu
playButton = Button(fen, text="Close", command=fen.quit)
playButton.pack(side=RIGHT)

playButton = Button(fen, text="Matrice", command=etatJeu)
playButton.pack(side=RIGHT)

playButton = Button(fen, text="Quadrier", command=quadrier)
playButton.pack(side=RIGHT)

playButton = Button(fen, text="Play", command=play)
playButton.pack(side=RIGHT)


fen.mainloop()
