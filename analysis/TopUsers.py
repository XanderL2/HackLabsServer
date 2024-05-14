import os, sys;
import requests as req;
import pandas as pd;




sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")));
# Añadir el directorio padre al PYTHONPATH

from configs import HOST, API_PORT, API_PROTOCOL;


endpoint =  f'{API_PROTOCOL}://{HOST}:{API_PORT}/api/';




def TopUsers(limit = 5):


    statisticsResp = req.get(endpoint + "/statistics");





    if(statisticsResp.status_code != 200): return False;




    statisticsDF = pd.DataFrame(statisticsResp.json());
    statisticsDF = statisticsDF.groupby("userId")["machine"].sum()\
                    .sort_values(ascending=False).head(limit);





    usersId = []


    for index, value in statisticsDF.items():
        usersId.append(index);





    users = []

    for user in usersId:


        userInfo = req.get(endpoint + f"/users/{user}");

        if(userInfo.status_code != 200): return False;




        users.append(userInfo.json()[0]);
        



    return users
    
    



    
    


























