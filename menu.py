#coding: utf-8

import tkinter as tk
from tkinter import *
import os

#from ClassPong import *


class Menu(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()

        self.titre = tk.Label(self, text='Menu')
        self.titre.pack()

        #LABELS
        self.lbHauteur=tk.Label(self, text='Hauteur: ')
        self.lbLargeur=tk.Label(self, text='Largeur: ')
        self.lbVitesseBarre=tk.Label(self, text='Vitesse de la barre: ')
        self.lbVitesseBalle=tk.Label(self, text='Vitesse de la balle: ')

        #CONTROLES
        self.HauteurValue=tk.Label(self, text="0")
        self.LargeurValue=tk.Label(self, text="0")
        self.VitesseBarreValue=tk.Label(self, text="0")
        self.VitesseBalleValue=tk.Label(self, text="0")
        
        # self.inputHauteur=tk.Entry(self, width=10)
        # self.inputHauteur.insert(0,"800")
        # self.inputLargeur=tk.Entry(self, width=10)
        # self.inputLargeur.insert(0,"600")

        self.scaleVitesseBarre=tk.Scale(self, orient=tk.HORIZONTAL, from_=1, to=15, command=self.valueVitesseBarre)
        self.scaleVitesseBalle=tk.Scale(self, orient=tk.HORIZONTAL, from_=1, to=15, command=self.valueVitesseBalle)
        self.scaleTailleHauteur=tk.Scale(self, orient=tk.HORIZONTAL, from_=200, to=800, command=self.valueHauteur)
        self.scaleTailleLargeur=tk.Scale(self, orient=tk.HORIZONTAL, from_=200, to=800, command=self.valueLargeur)
        
        self.boutonValid=tk.Button(self, text="Valider", command=self.validCfg)
        #self.boutonLaunch=tk.Button(self, text="Lancer", command=lambda: "C:\Users\user\Desktop\MATHS\projet math\Pong-Project\pong.py")

        self.log=tk.Text(self, height=1, bg='black', fg='white')

        #POSITIONS
        self.titre.grid(row=0, column=0, columnspan=2)
        self.lbHauteur.grid(row=1, column=0, columnspan=2)
        self.lbLargeur.grid(row=2, column=0, columnspan=2)
        self.lbVitesseBarre.grid(row=3, column=0, columnspan=2)
        self.lbVitesseBalle.grid(row=4, column=0, columnspan=2)
        
        # self.inputHauteur.grid(row=1, column=5)
        # self.inputLargeur.grid(row=2, column=5)

        self.boutonValid.grid(row=8, column=3)
        #self.boutonLaunch.grid(row=7, column=7)

        self.scaleTailleLargeur.grid(row=1, column=3, sticky=tk.E)
        self.scaleTailleHauteur.grid(row=2, column=3, sticky=tk.E)

        self.scaleVitesseBarre.grid(row=3, column=3, sticky=tk.E)
        self.scaleVitesseBalle.grid(row=4, column=3, sticky=tk.E)

        self.log.grid(row=8, column=0, columnspan=2)

    def valueVitesseBarre(self, valueVitBar):
        #s=str("ValBarre=")+valueVitBar+"\n"
        #self.log.insert('1.0', s)
        self.value1=valueVitBar

    def valueVitesseBalle(self, valueVitBal):
        #s=str("ValBalle= ")+valueVitBal+"\n"
        #self.log.insert('1.0', s)
        self.value2=valueVitBal

    def valueLargeur(self, valueLarg):        
        #s=str("ValLargeur= ")+valueLarg+"\n"
        #self.log.insert('1.0', s)
        self.value3=valueLarg

    def valueHauteur(self, valueHaut):
        #s=str("ValHauteur= ")+valueHaut+"\n"
        #self.log.insert('1.0', s)
        self.value4=valueHaut

    def validCfg(self):
        with open("cfg.py", "w") as fichier: 
            fichier.write("def width():")
            fichier.write("\n")

            fichier.write("    screen_width = ")
            fichier.write(str(self.value3))
            fichier.write("\n")
            
            fichier.write("    return screen_width")
            fichier.write("\n")
            
            fichier.write("def height():")
            fichier.write("\n")
            fichier.write("    screen_height = ")
            fichier.write(str(self.value4))
            fichier.write("\n")
            
            fichier.write("    return screen_height")
            fichier.write("\n")

            fichier.write("    #vitesseballe = ")
            fichier.write(str(self.value2))
            fichier.write("\n")

            fichier.write("    #vitessebarre = ")
            fichier.write(str(self.value1))

            s=str("Done! \n")
            self.log.insert('1.0', s)

m = Menu()
m.mainloop()