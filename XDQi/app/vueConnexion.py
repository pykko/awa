#!/usr/bin/python3
# coding: utf-8

from tkinter import *
from tkinter.messagebox import *
import http.client



class VueConnexion ( Toplevel ) :

    def __init__( self , parent ) :
        super().__init__( parent )
        self.title( 'Connexion' )

        lab_pseudo = Label( self , text='Pseudo :' , width = 20 , anchor = 'e' )
        self.ent_pseudo = Entry( self , width = 20 )

        lab_mdp = Label( self , text='MDP :' , width = 20 , anchor = 'e' )
        self.ent_mdp = Entry( self , width = 20 , show = '*' )

        btn_connecter = Button( self , text='Se connecter' , width = 12 , command = self.seConnecter )
        btn_annuler = Button( self , text='Annuler' , width = 12 , command = self.annuler )

        lab_pseudo.grid( padx = 5 , pady = 5 , row = 0 , column = 0 , sticky = 'e' )
        self.ent_pseudo.grid( padx = 5 , pady = 5 , row = 0  , column=1 , sticky = 'w' )

        lab_mdp.grid(padx = 5 , pady = 5 ,row=1, column=0, sticky='e' )
        self.ent_mdp.grid(padx = 5 , pady = 5 ,row=1, column=1, sticky='w')

        btn_connecter.grid(padx = 5 , pady = 5 ,row=2, column=0 )
        btn_annuler.grid(padx = 5 , pady = 5 ,row=2, column=1)


    def seConnecter( self ) :
        try:
            connexion = http.client.HTTPConnection( 'awa:5000' )
            chaineRequete = '/joueurs/connexion/{}/{}'.format( self.ent_pseudo.get() , self.ent_mdp.get() )
            print( chaineRequete )
            connexion.request( 'GET' , chaineRequete )
            reponse = connexion.getresponse()
            print( reponse.status , reponse.reason )
            print( reponse.read() )

            if reponse.status == 200 :
                showinfo( 'Connexion' , 'Authentification réussie !' )
            else :
                showerror( 'Connexion' , 'Authentification refusée !' )
        except :
            showerror( 'Connexion' , 'Petit problème réseau non ?' )


    def annuler( self ) :
        self.destroy()