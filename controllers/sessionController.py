import jwt, mysql.connector;


from flask import session;
from configs import SECRET, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_DATABASE;


DB_CONNECTION = {

    "host": DB_HOST,
    "user": DB_USER,
    "password": DB_PASSWORD,
    "database": DB_DATABASE,
    "port": DB_PORT   
}



def EstablishSesion(token):
         
    decoded_token = jwt.decode(token, SECRET, algorithms=['HS256']);


    userId = decoded_token['id']
    userRole = decoded_token['role']


    session["userId"] = userId;
    session["userRole"] = userRole;
    session["token"] = token



def Logout():
    
    ConnectionDB = mysql.connector.connect(**DB_CONNECTION); 

    if(not ConnectionDB):
        return ConnectionError(f"Error DB!!")



    cursor = ConnectionDB .cursor();

    cursor.execute("UPDATE Users SET state = 0 WHERE id = %s;", (session.get("userId"),))


    if(cursor.rowcount == 0):
        cursor.close()
        ConnectionDB .close()

        return ValueError(f"Error DB!!");

    ConnectionDB.commit()
    cursor.close()
    ConnectionDB .close()

   

    
     
         


