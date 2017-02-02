
from tkinter import *



	
def afficherJeu():		
	print(jeu)



#def gestionMap():
#	global jeu
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
		affichage.create_image(234+15, 273, image=background)
		mapCreated = True
	
	
	
	# Cette partie est rafraichie
	gestionMap()
	
	
	
	#Gere la fin
	

	
	if(isPlay):
		fen.after(17, play)



def quadrillage():
	#quadrillage
	for i in range(nbTilesLargeur):
		affichage.create_line(i*tailleTile, 0, i*tailleTile, hauteurAffichage, width=1, fill="white")
		
	for j in range(nbTilesHauteur):
		affichage.create_line(0, j*tailleTile, largeurAffichage, j*tailleTile, width=1, fill="white")


		
	
	
def etatJeu(): 
# Creation d'une matrice et affichage
	matrice = open("matrice.txt", "w")
	fen2 = Tk()
	liste = []
	for j in range(nbTilesHauteur):
		for i in range(nbTilesLargeur):
			liste.append(jeu[j][i])
			if (jeu[j][i] == 0) :
				affichage.create_text(i*(tailleTile)+13, j*(tailleTile)+13,text ="0", fill ="red") 
			 
			
		chaine = Label(fen2)
		chaine.configure(text=str(liste))
		
		
		chaine.pack()
		liste.clear()
	#matrice.write(str(jeu))
	matrice.close()
	



#=======================================================================
# PROGRAMME PRINCIPAL ==================================================
#=======================================================================

#Varibles utiles
tailleTile = 26                           # images decoupé 16*16
nbTilesHauteur = 21							
nbTilesLargeur = 19

hauteurAffichage = tailleTile * nbTilesHauteur		#Taille de la fenetre
largeurAffichage = tailleTile * nbTilesLargeur		#Taille de la fenetre

isPlay = True
mapCreated = False #Flag pour créer la map de base 


#Gestion plateau

jeu = [[0] * (nbTilesLargeur) for _ in range(nbTilesHauteur)]

afficherJeu()


#Gestion fenetre
fen = Tk()
fen.title("PAC MAN")


background = PhotoImage(file ='ressources/mapv2.png')

affichage = Canvas(fen, width=largeurAffichage, height= hauteurAffichage, bg="WHITE")
affichage.pack(side="top")





#Gestion menu
playButton = Button(fen, text="Close", command=fen.quit)
playButton.pack(side=RIGHT)

playButton = Button(fen, text="Matrice", command=etatJeu)
playButton.pack(side=RIGHT)

playButton = Button(fen, text="quadrillage", command=quadrillage)
playButton.pack(side=RIGHT)

playButton = Button(fen, text="Play", command=play)
playButton.pack(side=RIGHT)


fen.mainloop()
