import os, sys;
import requests as req;
import pandas as pd;

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")));
from configs import HOST, API_PORT, API_PROTOCOL;





endpoint =  f'{API_PROTOCOL}://{HOST}:{API_PORT}/api/';




def FavoriteTools(userId):

    statistics = req.get(endpoint + f"/statistics/{userId}");


    if(statistics.status_code != 200): return False



    statisticsDF = pd.DataFrame(statistics.json());
    statisticsDF = statisticsDF.groupby("toolId")["loss"].count()\
                    .sort_values(ascending=False).head(5)



    toolsId= [];
    for index, value in statisticsDF.items():
        toolsId.append(index);




    tools = [];
    for tool in toolsId:

        response = req.get(endpoint + f"/tools/{tool}");
        
        if(response.status_code != 200):
            return False ;

        tools.append(response.json()[0].get("name"));
        

    return tools 
