from tkinter import *


	
def afficherJeu():
	print(jeu)
	


def play():
	global isPlay
	# Cette partie est rafraichie a 60fps
	
	actualiserMap()
	
	#Gere la fin
	

	
	if(isPlay):
		fen.after(17, play)



def actualiserMap():
	vide = PhotoImage(file ='Tile/void.png')
	item = affichage.create_image(0, 0, image=vide)
	
	affichage.pack(side="top")
	
	#for i in range(nbTilesLargeur):
		#for j in range(nbTilesHauteur):
		#	affichage.create_image(j*tailleTile, i*tailleTile, image=vide)
	
	

	
	


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


jeu = [[0] * nbTilesLargeur for _ in range(nbTilesHauteur)]

#Gestion plateau
afficherJeu()


#Gestion fenetre
fen = Tk()
fen.title("PAC MAN")

affichage = Canvas(fen, width=largeurAffichage, height= hauteurAffichage, bg="black")
affichage.pack(side="top")




#Gestion menu
playButton = Button(fen, text="Play", command=play)
playButton.pack(side=RIGHT)


fen.mainloop()
