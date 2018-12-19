#!/usr/bin/python3
# coding: utf-8

from tkinter import *
from tkinter.messagebox import *
from vueConnexion import VueConnexion

class VuePrincipale ( Tk ) :

    def __init__( self ) :
        super().__init__()
        self.title('XouDouQi')
        self.geometry('400x300')

        self.creerBarreMenus()

    def creerBarreMenus( self ) :
        barreMenus = Menu( self )
        self.config(menu=barreMenus)

        menuFichier = Menu(barreMenus, tearoff=0)
        barreMenus.add_cascade(label='Fichier', menu=menuFichier)

        menuFichier.add_command(label='Se connecter', command=self.seConnecter)
        menuFichier.add_command(label='Se déconnecter')
        menuFichier.add_separator()
        menuFichier.add_command(label='Quitter', command=self.quitterApplication)

        menuParties = Menu(barreMenus, tearoff=0)
        barreMenus.add_cascade( label="Parties" , menu=menuParties )

        menuParties.add_command( label = 'Initier'  , command = self.initierPartie )


    def seConnecter( self ) :
        resultat = VueConnexion(self)
        resultat.transient(self)
        resultat.grab_set()
        resultat.focus_force()
        self.wait_window(resultat)

    def quitterApplication(self):
        reponse = askquestion('Quitter', 'Voulez-vous vraiment quitter ?', icon='question')
        if reponse == 'yes':
            self.destroy()


    def initierPartie( self ):
        reponse = askyesno( 'Initier une partie' , "Confirmez-vous la création d'une nouvelle partie ? " )
        print( reponse )
        if reponse == True :
            connexion = http.client.HTTPConnection('awa:5000')
            chaineRequete = '/joueurs/connexion/{}/{}'.format(self.ent_pseudo.get(), self.ent_mdp.get())
            print(chaineRequete)
            connexion.request('GET', chaineRequete)
            reponse = connexion.getresponse()
            print(reponse.status, reponse.reason)
            print(reponse.read())