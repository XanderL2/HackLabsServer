from dotenv import load_dotenv
import os

load_dotenv()  

HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", "5000")
API_PORT = os.getenv("API_PORT", 3000)
SECRET = os.getenv("SECRET")

