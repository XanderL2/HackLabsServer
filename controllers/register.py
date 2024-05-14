import requests as req;
from configs import HOST, API_PORT, API_PROTOCOL;


endpoint =  f'{API_PROTOCOL}://{HOST}:{API_PORT}/api/';




def Register(requestForm): 

    username = requestForm.get("username");
    password = requestForm.get("password");
    age = requestForm.get("age");

    data = {

        "username": username,
        "passd": password,
        "age": age

    };


    try:

        response = req.post(endpoint + "/register", json=data);
        return response

    except Exception as e: 

        return e;

 
