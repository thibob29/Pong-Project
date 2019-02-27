#coding: utf-8

import tkinter as tk
from tkinter import *
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
        
        # self.inputHauteur=tk.Entry(self, width=4)
        # self.inputHauteur.insert(0,"")
        # self.inputLargeur=tk.Entry(self, width=4)
        # self.inputLargeur.insert(0,"")

        self.scaleVitesseBarre=tk.Scale(self, orient=tk.HORIZONTAL, from_=1, to=15, command=self.valueVitesseBarre)
        self.scaleVitesseBalle=tk.Scale(self, orient=tk.HORIZONTAL, from_=1, to=15, command=self.valueVitesseBalle)
        self.scaleTailleHauteur=tk.Scale(self, orient=tk.HORIZONTAL, from_=200, to=800, command=self.valueHauteur)
        self.scaleTailleLargeur=tk.Scale(self, orient=tk.HORIZONTAL, from_=200, to=800, command=self.valueLargeur)
        
        self.boutonValid=tk.Button(self, text="Valider", command=self.validCfg)

        self.log=tk.Text(self, height=5, bg='black', fg='white')


        #POSITIONS
        self.titre.grid(row=0, column=0, columnspan=5)
        self.lbHauteur.grid(row=1, column=0, columnspan=5)
        self.lbLargeur.grid(row=2, column=0, columnspan=5)
        self.lbVitesseBarre.grid(row=3, column=0, columnspan=5)
        self.lbVitesseBalle.grid(row=4, column=0, columnspan=5)
        
        # self.inputHauteur.grid(row=1, column=5)
        # self.inputLargeur.grid(row=2, column=5)

        self.boutonValid.grid(row=6, column=7)

        self.scaleTailleLargeur.grid(row=1, column=7, sticky=tk.E)
        self.scaleTailleHauteur.grid(row=2, column=7, sticky=tk.E)

        self.scaleVitesseBarre.grid(row=3, column=7, sticky=tk.E)
        self.scaleVitesseBalle.grid(row=4, column=7, sticky=tk.E)

        self.log.grid(row=8, column=0, columnspan=5)

    def valueVitesseBarre(self, valueVitBar):
        s=str("ValBarre=")+valueVitBar+"\n"
        self.log.insert('1.0', s)
        self.value1=valueVitBar

    def valueVitesseBalle(self, valueVitBal):
        s=str("ValBalle= ")+valueVitBal+"\n"
        self.log.insert('1.0', s)
        self.value2=valueVitBal

    def valueLargeur(self, valueLarg):        
        s=str("ValLargeur= ")+valueLarg+"\n"
        self.log.insert('1.0', s)
        self.value3=valueLarg

    def valueHauteur(self, valueHaut):
        s=str("ValHauteur= ")+valueHaut+"\n"
        self.log.insert('1.0', s)
        self.value4=valueHaut


    def validCfg(self):
        with open("data.cfg", "w") as fichier: 
            fichier.write("screen_width = ")
            fichier.write(self.value3)
            fichier.write("\n")

            fichier.write("screen_height = ")
            fichier.write(self.value4)
            fichier.write("\n")

            fichier.write("vitesseballe = ")
            fichier.write(self.value2)
            fichier.write("\n")

            fichier.write("vitessebarre = ")
            fichier.write(self.value1)
            fichier.write("\n")

m = Menu()
m.mainloop()