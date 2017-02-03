
from tkinter import *



def play():
	global isPlay, mapCreated
	
	# On affiche la map 1 fois
	if not mapCreated:
		affichage.create_image(234+15, 273, image=background)
		mapCreated = True
	
	# Cette partie est rafraichie 60 fois par secondes
	
	
	
	
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
	fen2 = Tk()
	liste = []
	for j in range(nbTilesHauteur):
		for i in range(nbTilesLargeur):
			liste.append(jeu[j][i])
			if (jeu[j][i] == 0) :
				affichage.create_text(i*(tailleTile)+13, j*(tailleTile)+13,text ="0", fill ="green")
			if (jeu[j][i] == 1) :
				affichage.create_text(i*(tailleTile)+13, j*(tailleTile)+13,text ="1", fill ="red") 
			 
			
		chaine = Label(fen2)
		chaine.configure(text=str(liste))
		
		
		chaine.pack()
		liste.clear()
	#matrice.write(str(jeu))
	
	



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


#Remplir matrice

#jeu = [[0] * (nbTilesLargeur) for _ in range(nbTilesHauteur)]

jeu = []
jeu.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
jeu.append([1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1])
jeu.append([1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1])
jeu.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
jeu.append([1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1])
jeu.append([1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1])
jeu.append([1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1])
jeu.append([0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0])
jeu.append([1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1])
jeu.append([0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0])
jeu.append([1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1])
jeu.append([0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0])
jeu.append([1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1])
jeu.append([1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1])
jeu.append([1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1])
jeu.append([1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1])
jeu.append([1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1])
jeu.append([1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1])
jeu.append([1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1])
jeu.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
jeu.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])


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
