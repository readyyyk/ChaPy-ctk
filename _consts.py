from os import getenv
from dotenv import load_dotenv


load_dotenv()

SERVER_URL = getenv("SERVER_URL")
AVATAR_API_URL = getenv("AVATAR_API_URL")
