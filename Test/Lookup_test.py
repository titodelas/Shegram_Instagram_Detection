import requests

def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.co.in'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        print(urllink.url)

googleSearch('Linkin Park')