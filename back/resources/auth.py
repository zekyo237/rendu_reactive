from flask import request,session
from model.user import User
from flask_restful import Resource
from flask import Response, request,current_app as app
from flask_jwt_extended import create_access_token
import json
import os 
import datetime
from .utils import update_bd,countJsonelt,retouver_utilisateur
from flask.json import jsonify

class RegisterApi(Resource):
    def post(self):

        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        filename = os.path.join(SITE_ROOT,'base_donnee.json')
        body=request.get_json()
        user=User(**body)
        user.hash_password()
        user.creation_id(countJsonelt(filename)+1)
        username=user.password
        
        
    
        update_bd(filename,user.__dict__)
           
        return {'id':str(username)},200


class LoginApi(Resource):
    def post(self):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        filename = os.path.join(SITE_ROOT,'base_donnee.json')
        body = request.get_json()
        currentuser=User(**body)
        verificateur=retouver_utilisateur(filename,currentuser)
        
        

        if(verificateur==1) :
            expires = datetime.timedelta(minutes=10)
            access_token= create_access_token(identity=str(currentuser.username),expires_delta=expires)
            return {'token':access_token},200
        if(verificateur==0):
           return {'error': 'username or password invalid'}, 401 


class GetAllElementApi(Resource):

    def get(self):
         listeUtilisateur=[]
         SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
         filename = os.path.join(SITE_ROOT,'base_donnee.json')
         with open(filename) as fichier: 
                data= json.load(fichier) 
                fichier.close
                return data,200

class getuserbylist(Resource):
    def get(self,listid,id):
        print(listid != "Utilisateur1")
        if((listid!= 'Utilisateur1') and (listid!='Utilisateur2') and (listid!='Utilisateur3')):
            return {'message':"liste incorrecte"},401
        liste=[]
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        filename = os.path.join(SITE_ROOT,'base_donnee.json')
        with open(filename) as fichier: 
                data= json.load(fichier) 
                fichier.close
        liste=data[listid]
        for tapis in liste:
            if(tapis['id']==id):
                print(tapis['id'])
                username=tapis['username']
                print(username)
                return {"username":str(username)}
                break
                
            
        return {"message":"rien à signaler"}


        


