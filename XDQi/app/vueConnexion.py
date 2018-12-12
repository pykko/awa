#!/usr/bin/python3
# coding: utf-8

from tkinter import *

class VueConnexion ( Toplevel ) :

    def __init__( self , parent ) :
        super().__init__( parent )
        self.title( 'Connexion' )


    def seConnecter( self ) :
        self.destroy()