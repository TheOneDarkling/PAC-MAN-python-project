
from tkinter import *
import fantomeRouge
import constantes

### FONCTIONS JEU

def play():
	global isPlay, mapCreated, blinky
	
	# On affiche la map 1 fois
	if not mapCreated:
		affichage.create_image(234+15, 273, image=background)
		afficherPacGommes()
		
		blinky = fantomeRouge.init(affichage)
		
		mapCreated = True
	affichage.create_image(234+8, 390+8, anchor=NW, image=pcl1)
	# Cette partie est rafraichie 60 fois par secondes
	
	fantomeRouge.gestion(affichage, blinky, jeu)
	
	
	#Gere la fin
	

	
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
	for j in range(nbTilesHauteur):
		for i in range(nbTilesLargeur):
			liste.append(jeu[j][i])
			if (jeu[j][i] == 0) :
				affichage.create_text(i*(tailleTile)+13, j*(tailleTile)+13,text ="0", fill ="white")
			elif (jeu[j][i] == 1) :
				affichage.create_text(i*(tailleTile)+13, j*(tailleTile)+13,text ="1", fill ="green")
			elif (jeu[j][i] == 2) :
				affichage.create_text(i*(tailleTile)+13, j*(tailleTile)+13,text ="2", fill ="yellow")
			elif (jeu[j][i] == 3) :
				affichage.create_text(i*(tailleTile)+13, j*(tailleTile)+13,text ="3", fill ="grey") 
			elif (jeu[j][i] == 4) :
				affichage.create_text(i*(tailleTile)+13, j*(tailleTile)+13,text ="4", fill ="brown") 
			elif (jeu[j][i] == 5) :
				affichage.create_text(i*(tailleTile)+13, j*(tailleTile)+13,text ="5", fill ="red")
			
		chaine = Label(fen2)
		chaine.configure(text=str(liste))
		
		
		chaine.pack()
		liste.clear()
	#matrice.write(str(jeu))
	
	
	
###deplacement

#def img(cpt):
#	global image
#	if cpt == 0:
#		image = can.create_image(x, y, anchor=NW, image=pacmanleft)
#	elif cpt == 1:
#		image = can.create_image(x, y, anchor=NW, image=pacmanright)
#	elif cpt == 2:
#		image = can.create_image(x, y, anchor=NW, image=pacmantop)
#	elif cpt == 3:
#		image = can.create_image(x, y, anchor=NW, image=pacmanbot)
	
#def go_left(event =None):
#	if limite():
#		can.delete(image)
#		img(3)		
#	else:
#		
		
#def go_right(event =None):
#	if limite():
#		can.delete(image)
#		img(3)
#	else:
#		
		
	
#def go_up(event =None):
#	if limite():
#		can.delete(image)
#		img(3)	
#	else:
#		
		
	
#def go_down(event =None):
#	if limite():
#		can.delete(image)
#		img(3)
#	else:
#		
		
	
#def limite():
#	if jeu[i][j] == 3:
#		return True
#	else:
#		return False
			
	
	
##FONCTIONS PAC GOMMES

def afficherPacGommes():
	global listePacGommes
	
	
	for j in range(nbTilesHauteur):
		for i in range(nbTilesLargeur):
			if jeu[j][i] == 3:
				listePacGommes[j][i] = affichage.create_oval(i*tailleTile+rayonPacGomme, j*tailleTile+rayonPacGomme, i*tailleTile+tailleTile-rayonPacGomme, j*tailleTile+tailleTile-rayonPacGomme, fill="grey")
			elif jeu[j][i] == 4:
				listePacGommes[j][i] = affichage.create_oval(i*tailleTile+rayonSuperPacGomme, j*tailleTile+rayonSuperPacGomme, i*tailleTile+tailleTile-rayonSuperPacGomme, j*tailleTile+tailleTile-rayonSuperPacGomme, fill="grey")

		

	
	
	
	
	
	
	
### AUTRES

def test():
	global cpt, lol
	
	if cpt%2 == 0:
		lol = affichage.create_oval(0, 0, 100, 100, fill="red")
	else:
		affichage.delete(fen, lol);
		
	cpt +=1
		





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


jeu = []
jeu.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
jeu.append([1,3,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,3,1])
jeu.append([1,4,1,1,3,1,1,1,3,1,3,1,1,1,3,1,1,4,1])
jeu.append([1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1])
jeu.append([1,3,1,1,3,1,3,1,1,1,1,1,3,1,3,1,1,3,1])
jeu.append([1,3,3,3,3,1,3,3,3,1,3,3,3,1,3,3,3,3,1])
jeu.append([1,1,1,1,3,1,1,1,0,1,0,1,1,1,3,1,1,1,1])
jeu.append([0,0,0,1,3,1,0,0,0,5,0,0,0,1,3,1,0,0,0])
jeu.append([1,1,1,1,3,1,0,1,1,1,1,1,0,1,3,1,1,1,1])
jeu.append([0,0,0,0,3,0,0,1,0,0,0,1,0,0,3,0,0,0,0])
jeu.append([1,1,1,1,3,1,0,1,1,1,1,1,0,1,3,1,1,1,1])
jeu.append([0,0,0,1,3,1,0,0,0,0,0,0,0,1,3,1,0,0,0])
jeu.append([1,1,1,1,3,1,0,1,1,1,1,1,0,1,3,1,1,1,1])
jeu.append([1,3,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,3,1])
jeu.append([1,3,1,1,3,1,1,1,3,1,3,1,1,1,3,1,1,3,1])
jeu.append([1,4,3,1,3,3,3,3,3,2,3,3,3,3,3,1,3,4,1])
jeu.append([1,1,3,1,3,1,3,1,1,1,1,1,3,1,3,1,3,1,1])
jeu.append([1,3,3,3,3,1,3,3,3,1,3,3,3,1,3,3,3,3,1])
jeu.append([1,3,1,1,1,1,1,1,3,1,3,1,1,1,1,1,1,3,1])
jeu.append([1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1])
jeu.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])


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

#Gestion fenetre
fen = Tk()
fen.title("PAC MAN")


background = PhotoImage(file ='ressources/mapv2.png')

affichage = Canvas(fen, width=largeurAffichage, height= hauteurAffichage, bg="WHITE")
affichage.pack(side="top")

pcl1 = PhotoImage(file="ressources/pictures/pac-man/pacman-l 4.gif")




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
cpt = 0

playButton = Button(fen, text="test", command=test)
playButton.pack(side=RIGHT)

# Deplacements
image = None

#fen.bind("<Left>", go_left)          
#fen.bind("<Right>", go_right)       
#fen.bind("<Up>", go_up)            
#fen.bind("<Down>", go_down)

fen.mainloop()
