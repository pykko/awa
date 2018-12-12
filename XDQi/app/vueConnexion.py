#!/usr/bin/python3
# coding: utf-8

from tkinter import *
from requests import *



class VueConnexion ( Toplevel ) :

    def __init__( self , parent ) :
        super().__init__( parent )
        self.title( 'Connexion' )

        Label( self , text='Pseudo :' ).pack()
        Label( self , text='MDP :' ).pack()


        Button( self , text='Se connecter' , command = self.seConnecter ).pack()


    def seConnecter( self ) :
        self.destroy()