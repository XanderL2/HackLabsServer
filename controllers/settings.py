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
    
    
    

    





