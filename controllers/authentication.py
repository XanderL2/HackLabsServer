import requests as req;
from configs import HOST, API_PORT;



endpoint =  f'http://{HOST}:{API_PORT}/api/';


def AuthUser(username, password): 

    data = {
  
        "username": "UsuarioPrueba",
        "password": "prueba123"
  
    };


    endpointLogin = endpoint + "login";

    response = req.post(endpointLogin, data=data);


    return response
    


    
    

























