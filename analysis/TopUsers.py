import os, sys;
import requests as req;
import pandas as pd;




sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")));
# Añadir el directorio padre al PYTHONPATH

from configs import HOST, API_PORT, API_PROTOCOL;


endpoint =  f'{API_PROTOCOL}://{HOST}:{API_PORT}/api/';




def TopUsers(usersJson, limit = 5):


    statisticsResp = req.get(endpoint + "/statistics");



    if(statisticsResp.status_code != 200): return False;



    statisticsDF = pd.DataFrame(statisticsResp.json());
    statisticsDF = statisticsDF.groupby("userId")["machine"].sum()\
                    .sort_values(ascending=False).head(limit);




    usersId = statisticsDF.index.tolist()



    # Buscar los usuarios correspondientes a los IDs en usersId
    users = [user for user in usersJson if user.get("id") in usersId]

    # Ordenar los usuarios según el orden de usersId
    users.sort(key=lambda x: usersId.index(x.get("id")))

    return users


    
    



    
    


























