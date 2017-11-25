from bs4 import BeautifulSoup
import requests

class TwitterLogging_in:
  def __init__(self):
    #user name
    self.username = "komisho2510"
    #password
    self.password = "komiyama"

  def login(self):

    #to create session
    session = requests.Session()
    
    headers = {
      "User-Agent": "Mozilla/5.0",
      "accept": "text/html, application/xhtml+xml,application/xml,image/webp,image/apng,*/*;q=0.8",
      "accept-language": "ja,en-US;q=0.8,en;q=0.6",
      "content-type": "application/x-www-form-urlencoded",
      "origin":"https://twitter.com",
      "referer":"https://twitter.com",
      "upgrade-insecure-requests":"1"
      }

    payload = {
        "session[username_or_email]": "",
        "session[password]":"",
        "remember_me":"1",
        "return_to_ssl":"true",
        "scribe_log":"",
        "redirect_after_login":"/",

        }
    try:

      response = session.get('https://twitter.com/',headers=headers,allow_redirects=True)
      soup = BeautifulSoup(response.text,"lxml")
      auth_token = soup.find(attrs={'name':'authenticity_token'}).get('value')
      print("authericity_token:  {}".format(auth_token))
    except requests.ConnectionError:
      print("connection error")
      print("http_status:{}".format(response.http_status))

    payload['authenticity_token'] = auth_token
    payload['session[username_or_email]'] = self.username
    payload['session[password]'] = self.password
    
    try:
      login = session.post('https://twitter.com/sessions',headers=heeaders,data=payload,allowredirects=False)
      if login.status_code == 302:
        print ("successfully logging in")
        print ("http status:{}".format(login.status_code))

      else:
        print ("logging in failed")

    except:
      print (payload)
      print ("\n status_code: {}".format(login.status_code))
      print ("Error Loggin in")


if __name__ == '__main__':
  TwiLogin = TwitterLogging_in()
  TwiLogin.login()
#print('authority_token: '+auth_token)
#print('http status code: {}'.format(response.status_code))
