import os;
import requests as req;
from configs import HOST, API_PORT, API_PROTOCOL;



endpoint =  f'{API_PROTOCOL}://{HOST}:{API_PORT}/api/';


def PatchData(request, session):
    

    token = session.get("token"); 
     

    headers = {
        "x-access-token": token
    };

   
    body = {};  


    for key, value in request.form.items():
        if(value != ""):
            body.update({key: value});

    

    if(body == {} and request.files.get("photo") == None): return False
    
    response = req.patch(endpoint + "users", json=body, headers=headers);    


    return response
    
    
    

    
def SavePhoto(filesDict, session):

    formats = ("png", 'jpeg', "jpg")
    photo = filesDict.get('photo')


    
    if photo is None or not photo.filename.lower().endswith(formats):
        return False


    userId = session.get("userId")
    newFileName= f"{userId}.png"  


    pathFile = os.path.join("/static/profile", newFileName)


    
    if os.path.exists(pathFile):
        os.remove(pathFile)


    photo.save(os.path.join("static/profile", newFileName))
