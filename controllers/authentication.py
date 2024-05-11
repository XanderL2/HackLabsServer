import requests as req;
from configs import HOST, API_PORT;



endpoint =  f'http://{HOST}:{API_PORT}/api/';


def Authentication(requestForm): 

    username = requestForm.get("username");
    password = requestForm.get("password");

    data = {
        "username": username,
        "password": password
    };


    print(data)

    try:

        response = req.post(endpoint + "/login", json=data);
        return response

    except Exception as e: 

        print(e);
        return False;

    
    
    





    


    
    

























