import requests as req;
import os;


from flask import session;
from controllers.register import endpoint;


def GetUserInfo(userId, json):

    for user in json:
        if(user.get("id") == userId): return user 
    

    


def GetUserStatistics(userId):

    response = req.get(endpoint + f"/statistics/{userId}");

    
    statistics = {
        "machines": 0,
        "attempts": 0,
        "losses": 0
    }
    

    if(response.status_code != 200):
        return statistics;    

    

    response = response.json(); 
    
    for register in response:    

        statistics["machines"] += register.get("machine");
        statistics["attempts"] += register.get("attempt");
        statistics["losses"] += register.get("loss");


    
    return statistics;
    

def GetUsers():
    response = req.get(endpoint + f"/users/");
    response = response.json();
    

    return response;

def GetUsers():

    response = req.get(endpoint + f"/users/");
    response = response.json();

    

    for user in response:    

        pathFile = os.path.join("static/profile", f"{user.get('id')}.png");


        if(os.path.exists(pathFile)):
            user["photo"] = pathFile; 

        else:
            user["photo"] = "/static/profile/default.png"
        

    

    return response;












    
    




