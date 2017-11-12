from bs4 import BeatifulSoup
import sockets
import requests

session = requests.Session()

headers = {
        "User-Agent":"Mozilla/5.0",
        "accept":"text/html,application/xhtml+xml,application/xml",
        "accept-language":"ja,en-GB;q=0.8,en;q=0.6",
        "content-type":"application/x-www-form-unlencoded",
        "origin":"https://twitter.com",
        "referer":"https://twitter.com/",
        "upgrade-insecure-requests": "1"
        }
response = session.get('https://twitter.com/',headers=headers,allow_redirects=True)
soup = BeautifulSoup(response.text,"lxml")
auth_token=soup.find(attrs={'name': 'authority_token'}).get('value')

print ("authority_token: " + auth_token)
