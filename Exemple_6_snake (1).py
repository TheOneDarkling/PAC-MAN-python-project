from tkinter import * 

# === Définition de quelques gestionnaires d'événements : 

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

def go_left(event =None): 
    "délacement vers la gauche" 
    global dx, dy 
    dx, dy = -1, 0 

def go_right(event =None): 
    global dx, dy 
    dx, dy = 1, 0 

def go_up(event =None): 
    "déplacement vers le haut" 
    global dx, dy 
    dx, dy = 0, -1 
    
def go_down(event =None): 
    global dx, dy 
    dx, dy = 0, 1 
    
def move(): 
    "Animation du serpent par récursivité" 
    global flag 
    # Principe du mouvement opéré : on déplace le carré de queue, dont les 
    # caractéristiques sont mémorisées dans le premier élément de la liste 
    # <serp>, de manière à l'amener en avant du carré de tête, dont les 
    # caractéristiques sont mémorisées dans le dernier élément de la liste. 
    # On définit ainsi un nouveau carré de tête pour le serpent, dont on 
    # mémorise les caractéristiques en les ajoutant à la liste. 
    # Il ne reste plus qu'à effacer alors le premier élément de la liste, 
    # et ainsi de suite ... : 
    c = serp[0]             # extraction des infos concernant le carré de queue 
    cq = c[0]               # réf. de ce carré (coordonnées inutiles ici) 
    l =len(serp)            # longueur actuelle du serpent (= n. de carrés) 
    c = serp[l-1]           # extraction des infos concernant le carré de tête 
    xt, yt = c[1], c[2]     # coordonnées de ce carré 
    # Préparation du déplacement proprement dit. 
    # (cc est la taille du carré. dx & dy indiquent le sens du déplacement) : 
    xq, yq = xt+dx*cc, yt+dy*cc             # coord. du nouveau carré de tête 
    # Vérification : a-t-on atteint les limites du canevas ? : 
    if xq<0 or xq>canX-cc or yq<0 or yq>canY-cc: 
        flag =0             # => arrêt de l'animation 
        can.create_text(canX/2, 20, anchor =CENTER, text ="Perdu !!!", 
                        fill ="red", font="Arial 14 bold") 
    can.coords(cq, xq, yq)    # déplacement effectif 
    serp.append([cq, xq, yq])     # mémorisation du nouveau carré de tête 
    del(serp[0])                  # effacement (retrait de la liste) 
    # Appel récursif de la fonction par elle-même (=> boucle d'animation) : 
    if flag >0: 
        fen.after(50, move)    

# === Programme principal : ======== 

# Variables globales modifiables par certaines fonctions : 
flag =0                 # commutateur pour l'animation 
dx, dy = 1, 0           # indicateurs pour le sens du déplacement 

# Autres variables globales : 
canX, canY = 500, 500   # dimensions du canevas 
x, y, cc = 100, 100, 15         # coordonnées et coté du premier carré 

# Création de l'espace de jeu (fenêtre, canevas, boutons ...) : 
fen =Tk() 
can =Canvas(fen, bg ='dark gray', height =canX, width =canY) 
can.pack(padx =10, pady =10) 
bou1 =Button(fen, text="Start", width =10, command =start_it) 
bou1.pack(side =LEFT) 
bou2 =Button(fen, text="Stop", width =10, command =stop_it) 
bou2.pack(side =LEFT) 
bou3 = Button(fen,text='Quitter', width =8, command=fen.destroy)
bou3.pack(side=BOTTOM)

# Association de gestionnaires d'événements aux touches fléchées du clavier : 
fen.bind("<Left>", go_left)         # Attention : les événements clavier 
fen.bind("<Right>", go_right)       # doivent toujours être associés à la 
fen.bind("<Up>", go_up)             # fenêtre principale, et non au canevas 
fen.bind("<Down>", go_down)         # ou à un autre widget. 

pacmanleft = PhotoImage(file="ressources/pictures/pac-man/pacman-l 4.gif")
#pleft = can.create_image(x, y, anchor=NW, image=pacmanleft)


pacmanright = PhotoImage(file="ressources/pictures/pac-man/pacman-r 4.gif")
#pright = can.create_image(x, y, anchor=NW, image=pacmanright)

pacmantop = PhotoImage(file="ressources/pictures/pac-man/pacman-u 6.gif")
#ptop = can.create_image(x, y, anchor=NW, image=pacmantop)


pacmanbot = PhotoImage(file="ressources/pictures/pac-man/pacman-d 3.gif")
#pbot = can.create_image(x, y, anchor=NW, image=pacmanbot)



# Création du serpent initial (= ligne de 5 carrés). 
# On mémorisera les infos concernant les carrés créés dans une liste de listes : 
serp =[]                            # liste vide 
# Création et mémorisation des 5 carrés : le dernier (à droite) est la tête. 
i =0 
while i <1: 
    carre = can.create_image(x, y, anchor=NW, image=pacmanright)
    # Pour chaque carré, on mémorise une petite sous-liste contenant 
    # 3 éléments : la référence du carré et ses coordonnées de base : 
    serp.append([carre, x, y]) 
    x =x+cc                 # le carré suivant sera un peu plus à droite 
    i =i+1 

fen.mainloop() 
