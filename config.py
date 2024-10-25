import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "20860620")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "25d2343b36fc5aea3604c6c50a8e2b59") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7677995674:AAHWPb5lrQLkXSAGDvtZ5r8UHKiMps5SyVw") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002269101929') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://madara:madara@cluster0.tjfuu1g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","USERDATA") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6199677027")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002197851838')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()


    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8040"))
