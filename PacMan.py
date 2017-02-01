
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
		affichage.create_image(232, 256, image=background)
		mapCreated = True
	
	
	
	# Cette partie est rafraichie a 60fps
	gestionMap()
	
	
	
	#Gere la fin
	

	
	if(isPlay):
		fen.after(17, play)



	

def mapTest():
	global jeu
	
	for i in range(nbTilesLargeur+1):
		for j in range(nbTilesHauteur+1):
			if i == 0 or j == 0 or i == nbTilesHauteur or j == nbTilesLargeur or i == 1 or j == 1 or i == nbTilesHauteur-1 or j == nbTilesLargeur-1:
				jeu[j][i] =1

	
	
	
def etatJeu(): # Affiche la liste qui repertorie l'ensemble des pions
	fen2 = Tk()
	liste = []
	for j in range(22-1):
		for i in range(20-1):
			liste.append(jeu[i][j]) 
			
		chaine = Label(fen2)
		chaine.configure(text=str(liste))
		chaine.pack()
		liste.clear()

	


#=======================================================================
# PROGRAMME PRINCIPAL ==================================================
#=======================================================================

#Varibles utiles
tailleTile = 23
nbTilesHauteur = 22
nbTilesLargeur = 20

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

affichage = Canvas(fen, width=largeurAffichage, height= hauteurAffichage, bg="WHITE")
affichage.pack(side="top")



# Ressources graphiques

background = PhotoImage(file ='ressources/background.png')



#Gestion menu
playButton = Button(fen, text="Close", command=fen.quit)
playButton.pack(side=RIGHT)

playButton = Button(fen, text="Matrice", command=etatJeu)
playButton.pack(side=RIGHT)

playButton = Button(fen, text="Play", command=play)
playButton.pack(side=RIGHT)


fen.mainloop()
