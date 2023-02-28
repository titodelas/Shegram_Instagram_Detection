import instaloader
import time, os
import requests
import webbrowser


def photo():
    global path
    global username
    bot = instaloader.Instaloader()
    path = os.getcwd() # Obtain the actual directory path
    username = input("Instert Instagram account: @")
    print(bot.download_profile(username,profile_pic_only=True))

def detect_file(): # Trying to detect the .jpg file
    global file
    time.sleep(1) # Whait time to create the folder with the pfp

    for file in os.listdir(f"{path}/{username}"):
        if file.endswith(".jpg"): # Instagram pfp save as .jpg
            # Rename the file to make easy the detection
            os.rename(f'{path}/{username}/{file}', f'{path}/{username}/{username}.jpg')
        else:
            pass

def reverse_lookup(): # Upload photo to Google Image Search
    filePath = f'{path}/{username}/{username}.jpg'
    searchUrl = 'http://www.google.hr/searchbyimage/upload'
    multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']
    webbrowser.open(fetchUrl)

photo()
detect_file()
reverse_lookup()