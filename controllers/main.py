import requests as req;

from flask import session;
from controllers.register import endpoint;


def GetUserInfo(userId):

    response = req.get(endpoint + f"/users/{userId}");
    
    return response.json();


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







    
    



