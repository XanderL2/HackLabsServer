import os;
import requests as req;
from configs import HOST, API_PORT, API_PROTOCOL;



endpoint =  f'{API_PROTOCOL}://{HOST}:{API_PORT}/api/';


def PatchData(form, session):
    
    token = session.get("token"); 

     
    headers = {
        "x-access-token": token
    };

   
    body = {};  


    for key, value in form.items():
        if(value != ""):
            body.update({key: value});

    

    if(body == {}): return False
    
    response = req.patch(endpoint + "users", json=body, headers=headers);    


    return response
    
    
    

    
def SavePhoto(filesDict, session):


    photo = filesDict.get('photo');   

    if(photo == None):
        return False;



    userId = session.get("userId");
    listsImages = os.listdir("../static/profile")

    
    for image in listsImages:
        if(image == f"{userId}.png"): 
            os.remove(f"../static/profile/{userId}.png");

    

    

    photo.save('/static/profile', )
    




    

    
    

     
    
    




