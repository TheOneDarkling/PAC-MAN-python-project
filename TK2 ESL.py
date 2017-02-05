from tkinter import *


def start_it(): 
    "Démarrage de l'animation" 
    global flag 
    if flag ==0: 
        flag =1 
        move() 

def stop_it(): 
    "Arrêt de l'animation" 
    global flag 
    flag =0 
# Fonctions de mouvement

#def test(image):
	
	
	


def img(cpt):
	global image
	if cpt == 0:
		image = can.create_image(x, y, anchor=NW, image=pacmanleft)
	elif cpt == 1:
		image = can.create_image(x, y, anchor=NW, image=pacmanright)
	elif cpt == 2:
		image = can.create_image(x, y, anchor=NW, image=pacmantop)
	elif cpt == 3:
		image = can.create_image(x, y, anchor=NW, image=pacmanbot)
	


def go_left(event =None):
	global x, y, x2, x2, depl, image
	x-=depl
	#x2-=depl
	if limite():
		can.delete(image)
		img(0)
		
	else:
		x+=depl
		#x2+=depl


def go_right(event =None):
	global x, y, x2, x2, depl
	x+=depl
	#x2+=depl
	
	if limite():
		can.delete(image)
		img(1)
		
	else:
		x-=depl
		#x2-=depl
	
	
def go_up(event =None):
	global x, y, x2, y2, depl
	y-=depl
	#y2-=depl
	
	if limite():
		can.delete(image)
		
		img(2)
		
	else:
		y+=depl
		#y2+=depl
	

def go_down(event =None):
	global x, y, x2, y2, depl
	y+=depl
	#y2+=depl
	
	if limite():
		can.delete(image)
		
		img(3)
			
	else:
		y-=depl
		#y2-=depl
	



############### Bordures du canvas############
def limite():
	global x, y, x2, y2, DIM
	if x<0 or x2>DIM or y<0 or y2>DIM:
		return False
	else:
		return True






##############code principal#####################

fen = Tk()
fen.title("Tk N.VF && T.R")


#Variables utiles

flag =0   
taille = 40
x, y = 200, 200
x2, y2 = x+taille, y+taille
depl = 3 # Le pas

DIM = 400

#Widgets

can = Canvas(fen,bg='dark grey', width=DIM, height=DIM, relief="ridge")
can.pack(side=LEFT, padx =5, pady =5)
bou1 =Button(fen, text="Start", width =10, command =start_it) 
bou1.pack(side =LEFT) 
bou2 =Button(fen, text="Stop", width =10, command =stop_it) 
bou2.pack(side =LEFT) 


pacmanleft = PhotoImage(file="ressources/pictures/pac-man/pacman-l 4.gif")
pleft = can.create_image(x, y, anchor=NW, image=pacmanleft)
can.delete(pleft)

pacmanright = PhotoImage(file="ressources/pictures/pac-man/pacman-r 4.gif")
#pright = can.create_image(x, y, anchor=NW, image=pacmanright)

pacmantop = PhotoImage(file="ressources/pictures/pac-man/pacman-u 6.gif")
#ptop = can.create_image(x, y, anchor=NW, image=pacmantop)


pacmanbot = PhotoImage(file="ressources/pictures/pac-man/pacman-d 3.gif")
#pbot = can.create_image(x, y, anchor=NW, image=pacmanbot)


bou1 = Button(fen,text='Quitter', width =8, command=fen.destroy)
bou1.pack(side=BOTTOM)

# Deplacements
image = None

fen.bind("<Left>", go_left)          
fen.bind("<Right>", go_right)       
fen.bind("<Up>", go_up)            
fen.bind("<Down>", go_down)          




fen.mainloop()

