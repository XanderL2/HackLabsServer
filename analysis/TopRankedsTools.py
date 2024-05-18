import pandas as pd;
import requests as req;
import matplotlib.pyplot as plt
import os;


from analysis.FavoriteTools import endpoint;



def TopRankedsTools():
   

    # Data Extraction
    statisticsRes= req.get(endpoint + f"/statistics"); 
    toolsRes = req.get(endpoint + f"/tools"); 
    



    # Data Cleaning 
    dfStatistics = pd.DataFrame(statisticsRes.json());
    dfTools = pd.DataFrame(toolsRes.json());

    dfStatistics.drop(columns=['id', 'userId', 'createdAt', 'machine', 'attempt', 'loss'], inplace=True);


    dfTools.rename(columns={'id': 'toolId'}, inplace=True)
    dfStatistics = dfStatistics.merge(dfTools, on='toolId', how='left').drop(columns=['description']);



    # # Data Analysis 
    dfStatistics = dfStatistics.groupby("name")['toolId'].count().sort_values(ascending=False);



    # # Data visualization 
    plt.figure(figsize=(10, 8))  

    plt.pie(dfStatistics.values, labels=dfStatistics.index, autopct='%1.1f%%',
            colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
            startangle=140, 
            
    );


    plt.title('Top 5 best-ranked tools', fontsize=14, color='navy')
    plt.legend(dfStatistics.index, title="Herramientas", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))   


    # Saving and rebuilding the graph

    properties = {}

    path = f'static/statistics/TopRankedsTool.png';

    if(os.path.exists(path)):
        os.remove(path)

    
    plt.savefig(path, bbox_inches='tight', dpi=300);


    properties = {
        "path": path,
        "name": dfStatistics.index.to_list()
    }


    return properties; 



