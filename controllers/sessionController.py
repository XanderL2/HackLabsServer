from flask import session;
import jwt;

from configs import SECRET;



def EstablishSesion(token):


         
    decoded_token = jwt.decode(token, SECRET, algorithms=['HS256']);

    userId = decoded_token['id']
    userRole = decoded_token['role']

    session["userId"] = userId;
    session["userRole"] = userRole;
    session["token"] = token






    
    

    
