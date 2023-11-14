from dotenv import load_dotenv
import os

load_dotenv()

HOST = "localhost"
USER = "root"
PASSWORD = "dev"
DATABASE = "tcc"
PORT = "3306"

JWT_SECRET = os.urandom(24)
JWT_ALGORITHM = 'HS256'
TIME_EXPIRES = 30