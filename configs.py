# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23685822"))
    API_HASH = getenv("API_HASH", "ff0572e13ff2f63a50f6dc707e0c4c9f")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002902542706")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "1018033649").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Leviabcd:VL0RUYZHI0xrwDvz@cluster0.0cvcei0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
