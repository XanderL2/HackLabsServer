import pandas as pd;
import requests as req;
import matplotlib.pyplot as plt
import os, sys;


from datetime import datetime
from analysis.FavoriteTools import endpoint;






def LogsPerUser(userId):
   

    response = req.get(endpoint + f"/statistics"); 
    


   

    # Get current year
    currentYear = datetime.now().year


    # Data Extraction
    df = pd.DataFrame(response.json());

    df = df.query(f"userId == {userId}").copy()

    if(df.empty):
        return f"/static/resources/images/asset1.png"




    
    # Data Cleaning 
    df[['date', 'time']] = df['createdAt'].str.split('T', expand=True);
    df[['year', 'month', 'day']] = df['date'].str.split('-', expand=True);

    df['year'] = pd.to_numeric(df['year']);
    df['month'] = pd.to_numeric(df['month']);
    df['day'] = pd.to_numeric(df['day']);    


    df.drop(columns=['createdAt', 'time', 'date', 'id', 'userId'], inplace=True);
    df.query(f"year == {currentYear}", inplace=True);



    
    # Data Analysis 
    monthlyData = df.groupby('month').sum();
    monthlyData = monthlyData.reindex(range(1, 13), fill_value=0);



    monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];




    # Data visualization 
    plt.figure(figsize=(10, 6));


    plt.plot(monthNames, monthlyData['machine'], label='Machines');
    plt.plot(monthNames, monthlyData['loss'], label='Losses');
    plt.plot(monthNames, monthlyData['attempt'], label='Attempts');


    plt.title(f'Activity Log Analysis {currentYear}');
    plt.xlabel('Month');
    plt.ylabel('Count');
    plt.xticks(rotation=45);
    plt.legend();
    

    path = f'static/dataVisualization/{userId}.png';

    if(os.path.exists(path)):
        os.remove(path)

    
    plt.savefig(path, bbox_inches='tight', dpi=300);

    return path





    
    
    




    


    






# LogsPerUser(51, response.json())



# print(datetime.date.today())
# print(datetime.datetime.now().time())
        


     



