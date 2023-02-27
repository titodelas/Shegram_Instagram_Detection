import instaloader
bot = instaloader.Instaloader()
username = input("Instert Instagram account: @")
print(bot.download_profile(username,profile_pic_only=True))
