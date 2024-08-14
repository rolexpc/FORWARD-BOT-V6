import os
from os import environ

class Config:
    API_ID = os.environ.get("API_ID", "12618934")
    API_HASH = os.environ.get("API_HASH", "49aacd0bc2f8924add29fb02e20c8a16")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6518956653:AAF-j8WlImz7Y3bGuukewYORslS__wDvQAk") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://anus01:anus01@cluster0.dy9fh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "anus01")
    PORT = int(os.environ.get("PORT", "8080"))
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '1297128957').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    


