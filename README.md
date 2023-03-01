
# SheGram (Instagram Fake Account Detection)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/titodelas/Shegram_Instagram_Detection?style=flat-square) ![GitHub issues](https://img.shields.io/github/issues-raw/titodelas/Shegram_Instagram_Detection?style=flat-square) ![GitHub](https://img.shields.io/github/license/titodelas/Shegram_Instagram_Detection?style=flat-square)

SheGram (She = Sherlock + Gram = Instagram) is a powerful tool developed in python which has 4 modes of use. The main one is the detection of fake profiles on Instagram, by analyzing the profile photo we can compare it with Google and check if it has been extracted from any other social network, such as Pinterest. The other main attraction is that it has a database with various fake accounts, as well as their ID in case they change their name.

## Installation
Clone the repository and navigate to the folder.
```bash
git clone https://github.com/titodelas/Shegram_Instagram_Detection.git
cd Shegram_Instagram_Detection
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
```bash
pip install -r requirements.txt
```
Run SheGram (It has and IDLE so don't care about ARGS)
```bash
python3 shygram.py
```
## Usage
Navigate into the SheGram folder, and run the file
```bash
cd Shegram_Instagram_Detection
python shegram.py
```

## How it works ?
First, Extract the Photo of a selected account with [Instaloader](https://instaloader.github.io)
```python
bot = instaloader.Instaloader()
path = os.getcwd() # Obtain the actual directory path
username = input("Instert Instagram account: @")
print(bot.download_profile(username,  profile_pic_only=True))
```
Once we have the profile picture, we analyze it with the [Google Search By Image tool](https://www.google.com/imghp?hl=EN) via Python [Request](https://pypi.org/project/requests/)
```python
filePath  =  f'{path}/{username}/{username}.jpg' # Actual Path of the File
searchUrl  =  'http://www.google.hr/searchbyimage/upload'
multipart  =  {'encoded_image':  (filePath,  open(filePath,  'rb')),  'image_content':  ''}
response  =  requests.post(searchUrl,  files=multipart,  allow_redirects=False)
fetchUrl  =  response.headers['Location']
webbrowser.open(fetchUrl)
```
## TO DO

-  [x] Download Profile Photo of the account
-  [x] Analyze via Google Image search
-  [x] Make a Database with the fake accounts
-  [x] Build a Search tool to find accounts in the Database 
- [ ] Show the results in console + webbrowser
- [ ] Autodetect if is a fake account or not

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU](https://choosealicense.com/licenses/gpl-2.0/)