import instaloader
import time, os

bot = instaloader.Instaloader()
username = input("Instert Instagram account: @")
print(bot.download_profile(username,profile_pic_only=True))

# Trying to detect the .jpg file lmao
"""
time.sleep(5)

for file in os.listdir(f"/{username}"):
    if file.endswith(".jpg"): # Instagram pfp save as .jpg
        print(os.path.join(f"/{username}", file))
"""