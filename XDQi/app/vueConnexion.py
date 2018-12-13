#!/usr/bin/python3
# coding: utf-8

from tkinter import *
from requests import *



class VueConnexion ( Toplevel ) :

    def __init__( self , parent ) :
        super().__init__( parent )
        self.title( 'Connexion' )

        lab_pseudo = Label( self , text='Pseudo :' , width = 20 , anchor = 'e' )
        ent_pseudo = Entry( self , width = 20 )

        lab_mdp = Label( self , text='MDP :' , width = 20 , anchor = 'e' )
        ent_mdp = Entry( self , width = 20 , show = '*' )

        btn_connecter = Button( self , text='Se connecter' , width = 12 , command = self.seConnecter )
        btn_annuler = Button( self , text='Annuler' , width = 12 , command = self.annuler )

        lab_pseudo.grid( padx = 5 , pady = 5 , row = 0 , column = 0 , sticky = 'e' )
        ent_pseudo.grid( padx = 5 , pady = 5 , row = 0  , column=1 , sticky = 'w' )

        lab_mdp.grid(padx = 5 , pady = 5 ,row=1, column=0, sticky='e' )
        ent_mdp.grid(padx = 5 , pady = 5 ,row=1, column=1, sticky='w')

        btn_connecter.grid(padx = 5 , pady = 5 ,row=2, column=0 )
        btn_annuler.grid(padx = 5 , pady = 5 ,row=2, column=1)


    def seConnecter( self ) :
        self.destroy()

    def annuler( self ) :
        self.destroy()