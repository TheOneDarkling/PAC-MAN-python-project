
from tkinter import *
import menu
import fantomeRouge
import fantomeOrange
import fantomeBleu
import fantomeRose
import constantes
import pac
import time


### MENU

def menuPrincipal():
	""" Premiere fonction qui affiche le menu(en fontion des var booleans) """
	global fen, affMenu, creationMenu, boutons, choixMenu
	import ressources
	
	if affMenu:
		if creationMenu:
			fond = affichage.create_image(constantes.milieuX, constantes.milieuY, image=ressources.backgroundMenu)
			logoPac = affichage.create_image(constantes.milieuX, 100, image=ressources.logo)
			
			boutons = [affichage.create_image(constantes.milieuX, constantes.debutMenu + constantes.espace*1, image=ressources.boutonA[0]),
			           affichage.create_image(constantes.milieuX, constantes.debutMenu + constantes.espace*2, image=ressources.boutonD[1]),
			           affichage.create_image(constantes.milieuX, constantes.debutMenu + constantes.espace*3, image=ressources.boutonD[2]),
			           affichage.create_image(constantes.milieuX, constantes.debutMenu + constantes.espace*4, image=ressources.boutonD[3])]
			           #PLAY/HARDCORE/OPTION/QUIT
			           
			creationMenu = False
			
		choixMenu = menu.gestionMenu(fen, affichage, boutons)
		
		#gestion du choix
		if choixMenu == constantes.CHOIX_PLAY:
			affMenu = False
			
		if choixMenu == constantes.CHOIX_HARDMODE:
			affMenu = False
			constantes.vitesseFantome += 0.2
			
		if choixMenu == constantes.CHOIX_OPTIONS:
			print("PAS DE MENU OPTIONS POUR L'INSTANT")
			
		if choixMenu == constantes.CHOIX_QUITTER:
			fen.destroy()
			
		
	else:
		play()
	

	fen.after(17, menuPrincipal) # 17 = 60FPS
	
	
	



### FONCTIONS JEU

def play():
	""" Fonction principale, elle gere le jeu"""
	global mapCreated, blinky , pacman, ressources, listePacGommes, fen, clyde, inky, pinky
	import ressources
	# On affiche la map 1 fois
	if not mapCreated:
		affichage.create_image(249, 273, image=background)
		afficherPacGommes(affichage)
		
		blinky = fantomeRouge.init(affichage)
		clyde = fantomeOrange.init(affichage)
		inky = fantomeBleu.init(affichage)
		pinky = fantomeRose.init(affichage)
		
		mapCreated = True
		
		pacman = pac.init(affichage)

	# Cette partie est rafraichie 60 fois par secondes
	##################################################
	
	
	if fantomeEnJeu[0]:
		fantomeRouge.gestion(affichage, blinky, jeu)
	
	if fantomeEnJeu[1]:
		fantomeOrange.gestion(affichage, clyde, jeu)
		
	if fantomeEnJeu[2]:
		fantomeBleu.gestion(affichage, inky, jeu)
		
	if fantomeEnJeu[3]:
		fantomeRose.gestion(affichage, pinky, jeu)

	
	pac.gestion(affichage,pacman,jeu, listePacGommes, fen)
	
	
	#SPAWN des fantome
	
	for i in range(4):
		if not fantomeEnJeu[i]:
			constantes.timerFantome[i] += 1
	
	if not fantomeEnJeu[0] and constantes.timerFantome[0] >= constantes.tempsSpawn and aucunFantomeDansSpawn():
		fantomeEnJeu[0] = True
		blinky = fantomeRouge.spawn(blinky, affichage, fen, jeu)

	if not fantomeEnJeu[1] and constantes.timerFantome[1] >= constantes.tempsSpawn and aucunFantomeDansSpawn():
		fantomeEnJeu[1] = True
		clyde = fantomeOrange.spawn(clyde, affichage, fen, jeu)
		
	if not fantomeEnJeu[2] and constantes.timerFantome[2] >= constantes.tempsSpawn and aucunFantomeDansSpawn():
		fantomeEnJeu[2] = True
		inky = fantomeBleu.spawn(inky, affichage, fen, jeu)
		
	if not fantomeEnJeu[3] and constantes.timerFantome[3] >= constantes.tempsSpawn and aucunFantomeDansSpawn():
		fantomeEnJeu[3] = True
		pinky = fantomeRose.spawn(pinky, affichage, fen, jeu)
	
	
	#superMode
	if constantes.superMode:
		constantes.timerSuperMode += 1
		if constantes.timerSuperMode >= 1200:
			constantes.timerSuperMode = 0
			constantes.superMode = False
		
	
	#Gere la fin
	##################################################
	if constantes.partiePerdu:
		gameOver()
	
	




### FONCTION STRUCTURE DE DONNéES

def quadrillage():
	""" Fonction de debug, affiche un quadriage """
	for i in range(nbTilesLargeur):
		affichage.create_line(i*tailleTile, 0, i*tailleTile, hauteurAffichage, width=1, fill="white")
		
	for j in range(nbTilesHauteur):
		affichage.create_line(0, j*tailleTile, largeurAffichage, j*tailleTile, width=1, fill="white")





def etatJeu():
	""" Fonction de debug, affiche la matrice du jeu à l'etat actuel """
	fen2 = Tk()
	liste = []
	
	couleur = ["white","green","yellow","grey","brown","red", "pink", "blue","orange"]
	
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
	""" Affiche tous les pac gommes sur la carte """
	global listePacGommes
	
	
	for j in range(nbTilesHauteur):
		for i in range(nbTilesLargeur):
			if jeu[j][i] == 3:
				listePacGommes[j][i] = affichage.create_oval(i*tailleTile+rayonPacGomme, j*tailleTile+rayonPacGomme, i*tailleTile+tailleTile-rayonPacGomme, j*tailleTile+tailleTile-rayonPacGomme, fill="grey")
			elif jeu[j][i] == 4:
				listePacGommes[j][i] = affichage.create_oval(i*tailleTile+rayonSuperPacGomme, j*tailleTile+rayonSuperPacGomme, i*tailleTile+tailleTile-rayonSuperPacGomme, j*tailleTile+tailleTile-rayonSuperPacGomme, fill="grey")
	
	
	#affichage.delete(fen, listePacGommes[1][1]) ## POUR SUPR


	
	
### TEST de position


def aucunFantomeDansSpawn():
	""" Renvoie True si aucun fantome ne se trouve dans la zone d'apparition(evite les superpositions)"""
	entite = [2, 5, 6, 7, 8]
	flag = True
	
	for i in range(len(entite)):
		if (jeu[7][9] in  entite) or (jeu[7][8] in  entite) or (jeu[7][10] in  entite):
			flag = False
	
	return flag
		
		


	
	
	
### AUTRES

def test():
	"""Inutile pour le jeu, sert a faire des test"""
	global cpt, lol
	
	if cpt%2 == 0:
		lol = affichage.create_oval(0, 0, 100, 100, fill="red")
	else:
		affichage.delete(fen, lol);
		
	cpt +=1
		

def toucheEnter(event =None):
	constantes.valider = True
	



def gameOver():
	""" Fonction qui est lancée lorsqu'un fantome touche pacman"""
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

creationMenu = True
affMenu = True
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
clyde  = 0
inky = 0
pinky = 0
pacman = 0
bouche = 3

boutons = list()
choixMenu = constantes.CHOIX_NONE
# Si les fantomes sont en jeu

fantomeEnJeu = [True, False, False, False] #Rouge/Orange/BLEU/ROSE

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

#Bouton test ne sert a rien pour le jeu

playButton = Button(fen, text="test", command=test)
playButton.pack(side=RIGHT)

# Deplacements
image = None

fen.bind("<Left>", pac.go_left)          
fen.bind("<Right>", pac.go_right)       
fen.bind("<Up>", pac.go_up)            
fen.bind("<Down>", pac.go_down)
fen.bind("<Return>", toucheEnter)

# Menu

menuPrincipal()

fen.mainloop()
