
from tkinter import *
import fantomeRouge
import constantes
import pac
import time


### FONCTIONS JEU

def play():
	global isPlay, mapCreated, blinky , pacman, ressources, listePacGommes, fen
	
	# On affiche la map 1 fois
	if not mapCreated:
		affichage.create_image(234+15, 273, image=background)
		afficherPacGommes(affichage)
		
		blinky = fantomeRouge.init(affichage)
		
		mapCreated = True
		
		pacman = pac.init(affichage)

	# Cette partie est rafraichie 60 fois par secondes
	
	
	
	isPlay = fantomeRouge.gestion(affichage, blinky, jeu,isPlay)
	
	pac.gestion(affichage,pacman,jeu, listePacGommes, fen)
	
	
	
	#Gere la fin
	
	if constantes.partiePerdu:
		gameOver()
	
	if(isPlay):
		fen.after(17, play)




### FONCTION STRUCTURE DE DONNéES

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
	
	couleur = ["white","green","yellow","grey","brown","red"]
	
	for j in range(nbTilesHauteur):
		for i in range(nbTilesLargeur):
			liste.append(jeu[j][i])
			affichage.create_text(i*(tailleTile)+13, j*(tailleTile)+13,text =jeu[j][i], fill =couleur[jeu[j][i]])
			
		chaine = Label(fen2)
		chaine.configure(text=str(liste))
		
		chaine.pack()
		liste.clear()

	
	
##FONCTIONS PAC GOMMES

def afficherPacGommes(affichage):
	global listePacGommes
	
	
	for j in range(nbTilesHauteur):
		for i in range(nbTilesLargeur):
			if jeu[j][i] == 3:
				listePacGommes[j][i] = affichage.create_oval(i*tailleTile+rayonPacGomme, j*tailleTile+rayonPacGomme, i*tailleTile+tailleTile-rayonPacGomme, j*tailleTile+tailleTile-rayonPacGomme, fill="grey")
			elif jeu[j][i] == 4:
				listePacGommes[j][i] = affichage.create_oval(i*tailleTile+rayonSuperPacGomme, j*tailleTile+rayonSuperPacGomme, i*tailleTile+tailleTile-rayonSuperPacGomme, j*tailleTile+tailleTile-rayonSuperPacGomme, fill="grey")
	
	
	#affichage.delete(fen, listePacGommes[1][1]) ## POUR SUPR
	print(listePacGommes)

		

	
	
	
	
	
	
	
### AUTRES

def test():
	global cpt, lol
	
	if cpt%2 == 0:
		lol = affichage.create_oval(0, 0, 100, 100, fill="red")
	else:
		affichage.delete(fen, lol);
		
	cpt +=1
		


def gameOver():
	global fen
	print("GAME OVER XD")
	fen.destroy()
	




#=======================================================================
# PROGRAMME PRINCIPAL ==================================================
#=======================================================================

#Varibles utiles
tailleTile = constantes.tailleTile                           # images decoupé 16*16
nbTilesHauteur = constantes.nbTilesHauteur							
nbTilesLargeur = constantes.nbTilesLargeur
rayonPacGomme = constantes.rayonPacGomme # + --> Plus petit   - --> Plus grand
rayonSuperPacGomme = constantes.rayonSuperPacGomme

hauteurAffichage = tailleTile * nbTilesHauteur		#Taille de la fenetre
largeurAffichage = tailleTile * nbTilesLargeur		#Taille de la fenetre

isPlay = True
mapCreated = False #Flag pour créer la map de base 
#Remplir matrice


jeu = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,3,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,3,1],
       [1,4,1,1,3,1,1,1,3,1,3,1,1,1,3,1,1,4,1],
       [1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
       [1,3,1,1,3,1,3,1,1,1,1,1,3,1,3,1,1,3,1],
       [1,3,3,3,3,1,3,3,3,1,3,3,3,1,3,3,3,3,1],
       [1,1,1,1,3,1,1,1,0,1,0,1,1,1,3,1,1,1,1],
       [0,0,0,1,3,1,0,0,0,5,0,0,0,1,3,1,0,0,0],
       [1,1,1,1,3,1,0,1,1,1,1,1,0,1,3,1,1,1,1],
       [0,0,0,0,3,0,0,1,0,0,0,1,0,0,3,0,0,0,0],
       [1,1,1,1,3,1,0,1,1,1,1,1,0,1,3,1,1,1,1],
       [0,0,0,1,3,1,0,0,0,0,0,0,0,1,3,1,0,0,0],
       [1,1,1,1,3,1,0,1,1,1,1,1,0,1,3,1,1,1,1],
       [1,3,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,3,1],
       [1,3,1,1,3,1,1,1,3,1,3,1,1,1,3,1,1,3,1],
       [1,4,3,1,3,3,3,3,3,2,3,3,3,3,3,1,3,4,1],
       [1,1,3,1,3,1,3,1,1,1,1,1,3,1,3,1,3,1,1],
       [1,3,3,3,3,1,3,3,3,1,3,3,3,1,3,3,3,3,1],
       [1,3,1,1,1,1,1,1,3,1,3,1,1,1,1,1,1,3,1],
       [1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


############DESCRIPTION###########
# 0 = ESPACE VIDE
# 1 = MUR
# 2 = PAC MAN
# 3 = PAC-GOMME
# 4 = SUPER-PAC-GOMME
# 5 = BLINKY(fantome rouge)
# 6 = PINKY(fantome rose)
# 7 = INKY(fantome bleu)
# 8 = CLYDE(fantome orange)

listePacGommes = [[0] * nbTilesLargeur for _ in range(nbTilesHauteur)]

blinky = 0
pacman = 0
bouche = 3

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

#Bouton test ne sert a rien pour le jeu

playButton = Button(fen, text="test", command=test)
playButton.pack(side=RIGHT)

# Deplacements
image = None

fen.bind("<Left>", pac.go_left)          
fen.bind("<Right>", pac.go_right)       
fen.bind("<Up>", pac.go_up)            
fen.bind("<Down>", pac.go_down)

fen.mainloop()
