import os
API_ID = int(os.getenv("16460251"))
API_HASH = os.getenv("67068034caedfb02e3bbfef339f827bd")
BOT_TOKEN = os.getenv("5121380728:AAEOWGflH_3BR4VMUHfjdgH7BF_yjJLDlLs")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
