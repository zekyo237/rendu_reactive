import json
from random import seed
from random import randint
from model.user import User


def update_bd(filename,valeur):
    number_liste=randint(1,3)
    with open(filename) as json_file: 
        data= json.load(json_file) 
        json_file.close

    
    liste='Utilisateur'+str(number_liste)
    temp = data[liste]  
    temp.append(valeur) 


    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
        json_file.close


def countJsonelt(filename):
    with open(filename) as json_file: 
        data= json.load(json_file) 
        json_file.close

    liste1=data['Utilisateur1']  
    liste2=data['Utilisateur2']  
    liste3=data['Utilisateur3']  
    return len(liste1)+len(liste2)+len(liste3)




def retouver_utilisateur(filename,currentuser):
    verificateur=0
    with open(filename) as json_file: 
            data= json.load(json_file) 
            json_file.close
    liste1=[]
    liste2=[]
    liste3=[]
    for tampon in data['Utilisateur1']:
            liste1.append(User(tampon['username'],tampon["password"]))
        
    for tapis in liste1:
            if(tapis.username==currentuser.username and tapis.check_password(currentuser.password)):
                verificateur=1
                break
    return verificateur

    for tampon in data['Utilisateur2']:
            liste2.append(User(tampon['username'],tampon["password"]))
        
    for tapis in liste2:
            if(tapis.username==currentuser.username and tapis.check_password(currentuser.password)):
                verificateur=1
                break
    return verificateur

    for tampon in data['Utilisateur3']:
            liste3.append(User(tampon['username'],tampon["password"]))
        
    for tapis in liste3:
            if(tapis.username==currentuser.username and tapis.check_password(currentuser.password)):
                verificateur=1
                break
    return verificateur