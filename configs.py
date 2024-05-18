from dotenv import load_dotenv
import os

load_dotenv()  


#Server
HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", "5000")



#REST API
API_PORT = os.getenv("API_PORT", 3000)
SECRET = os.getenv("SECRET")
API_PROTOCOL = os.getenv('API_PROTOCOL', 'http');



#BD
DB_HOST = os.getenv("DB_HOST", "localhost");
DB_PORT = os.getenv("DB_PORT", 3306);
DB_USER = os.getenv('DB_USER');
DB_PASSWORD = os.getenv('DB_PASSWORD');
DB_DATABASE = os.getenv('DB_DATABASE');

