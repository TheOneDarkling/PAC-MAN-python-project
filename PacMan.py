from tkinter import *



#=======================================================================
# PROGRAMME PRINCIPAL ==================================================
#=======================================================================


fen = Tk()

fen.title("PAC MAN")

plateau = Canvas(fen, width=500, height= 500, bg="black")
plateau.pack(side="top")

fen.mainloop()
