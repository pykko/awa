#!/usr/bin/python3
# coding: utf-8


from flask import *
import json

from modeles import modeleXDQ

app = Flask( __name__ )

@app.route( '/' , methods = [ 'GET' ] )
def accueillir() :
    return make_response( 'XDQ' )

@app.route( '/joueurs/connexion/<pseudo>/<mdp>' , methods = [ 'GET' ] )
def seConnecter( pseudo , mdp ) :

    print( pseudo , mdp )

    joueur = modeleXDQ.seConnecter( pseudo , mdp )

    print( joueur )

    if joueur !=  None and len( joueur ) != 0 :
        reponse = make_response( json.dumps( joueur ) )
        reponse.mimeType = 'application/json'
        reponse.status_code = 200
    else :
        reponse = make_response( '' )
        reponse.mimeType = 'application/json'
        reponse.status_code = 404

    return reponse



if __name__ == '__main__' :
    app.run( debug = True , host = '0.0.0.0' , port = 5000 )


