import os

api_id = 23634056
api_hash = os.environ.get("API_HASH", "f2debf49c2f57bad88086ecd17cb5df3")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "5082207960,7612404009")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "5082207960,7612404009")
owner_users = [int(num) for num in osowner_users.split(",")]
