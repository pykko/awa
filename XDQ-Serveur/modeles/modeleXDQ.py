#!/usr/bin/python3
# coding: utf-8


import mysql.connector


connexion = None


def getConnexion() :
    global connexion

    try :
        print( 'Modele> 1' )
        if connexion == None :
            connexion = mysql.connector.connect(
                host = 'localhost' ,
                user = 'developpeur' ,
                password = '1lovelace1' ,
                database = 'xdq'
            )
        print('Modele> 2')

        return connexion
    except :
        return None


def seConnecter( pseudo , mdp ) :
    try :
        curseur = getConnexion().cursor()

        requete = '''
            select id , email
            from Joueur
            where pseudo = %s
            and mdp = %s
        '''

        curseur.execute( requete , ( pseudo , mdp ) )

        enregistrement = curseur.fetchone()

        joueur = {}

        if enregistrement != None :
            joueur[ 'id' ] = enregistrement[ 0 ]
            joueur[ 'pseudo' ] = pseudo
            joueur[ 'email' ] = enregistrement[ 1 ]

        curseur.close()
        return joueur

    except mysql.connector.Error as e :
        print( e )
        return None


def initierPartie( idJoueur , couleur ) :
    try :
        curseur = getConnexion().cursor()

        requetePartie = '''
                insert into Partie( creation , initiateur , son_tour )
                values( now() , %s , %s )
            '''

        if couleur == 'B' :
            curseur.execute( requetePartie , ( idJoueur , idJoueur ) )
        else :
            curseur.execute( requetePartie , ( idJoueur, None ) )

        idPartie = curseur.lastrowid

        requeteChoisir = '''
                insert into Choisir
                values( %s , %s , %s )
            '''
        curseur.execute( requeteChoisir , ( idPartie , idJoueur , couleur ) )

        connexion.commit()

        curseur.close()

        return idPartie


    except mysql.connector.Error as e :
        print( e )
        return None

