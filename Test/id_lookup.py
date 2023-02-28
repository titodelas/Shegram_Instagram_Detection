import instaloader

L = instaloader.Instaloader()
profile = instaloader.Profile.from_id(L.context, ID)
print(profile.username)