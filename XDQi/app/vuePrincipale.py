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
        self.barreMenus = Menu( self )
        self.config(menu=self.barreMenus)

        self.menuFichier = Menu(self.barreMenus, tearoff=0)
        self.barreMenus.add_cascade(label='Fichier', menu=self.menuFichier)

        self.menuFichier.add_command(label='Se connecter', command=self.seConnecter)
        self.menuFichier.add_command(label='Se déconnecter' , command=self.sedDeconnecter , state = 'disabled' )
        self.menuFichier.add_separator()
        self.menuFichier.add_command(label='Quitter', command=self.quitterApplication)

        self.menuParties = Menu(self.barreMenus, tearoff=0)
        self.barreMenus.add_cascade( label="Parties" , menu=self.menuParties , state = 'disabled' )

        self.menuParties.add_command( label = 'Initier'  , command = self.initierPartie )


    def seConnecter( self ) :
        resultat = VueConnexion(self)
        resultat.transient(self)
        resultat.grab_set()
        resultat.focus_force()
        self.wait_window(resultat)


    def sedDeconnecter( self ) :
        reponse = askyesno('Déconnexion', 'Confirmez-vous la déconnexion ?' )
        print(reponse)
        if reponse == True :
            self.menuFichier.entryconfig(0, state='normal')
            self.menuFichier.entryconfig(1, state='disabled')
            self.barreMenus.entryconfig(2, state='disabled')


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
