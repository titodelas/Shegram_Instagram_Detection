import instaloader
import time, os
from GoogleSearch import Search

bot = instaloader.Instaloader()
path = os.getcwd() # Obtain the actual directory path
username = input("Instert Instagram account: @")
print(bot.download_profile(username,profile_pic_only=True))

# Trying to detect the .jpg file
time.sleep(1) # Whait time to create the folder with the pfp

for file in os.listdir(f"{path}/{username}"):
    if file.endswith(".jpg"): # Instagram pfp save as .jpg
        print(os.path.join(f"{path}/{username}", file))

output = Search(file_path=os.path.join(f"{path}/{username}", file))
print(output)