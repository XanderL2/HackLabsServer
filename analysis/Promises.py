import pandas as pd;
import requests as req;
import matplotlib.pyplot as plt
import os;


from analysis.FavoriteTools import endpoint;





def Promises():
   

    # Data Extraction
    statisticsRes= req.get(endpoint + f"/statistics"); 
    usersRes= req.get(endpoint + f"/users"); 
    



    # Data Cleaning 
    dfStatistics = pd.DataFrame(statisticsRes.json());
    dfUsers = pd.DataFrame(usersRes.json());

    dfStatistics.drop(columns=['id', 'toolId', 'createdAt'], inplace=True);
    dfUsers.rename(columns={'id': 'userId'}, inplace=True)
    dfStatistics = dfStatistics.merge(dfUsers, on='userId', how='left').drop(columns=['state', 'createdAt'])


    

    # Data Analysis 
    dfStatistics = dfStatistics.query('age <= 20')\
                    .groupby("username", as_index=False).agg({'machine': 'sum', 'age': 'first'})\
                    .sort_values(by=['machine', 'age'], ascending=[False, True]).head(5)


    # Data visualization 
    plt.figure(figsize=(10, 6));
    plt.barh(dfStatistics['username'], dfStatistics['machine'], color=['skyblue', 'pink', 'lavender', 'palegoldenrod', 'peachpuff']);
    plt.gca().invert_yaxis()



    plt.title('Top 5 promises of Hacking');
    plt.xlabel('Machines');
    plt.ylabel('Users');
    

    # Saving and rebuilding the graph

    properties = {}

    path = f'static/statistics/promises.png';

    if(os.path.exists(path)):
        os.remove(path)

    
    plt.savefig(path, bbox_inches='tight', dpi=300);


    properties = {
        "path": path,
        "users": dfStatistics['username'].to_list()
    }



    return properties; 



   


     



