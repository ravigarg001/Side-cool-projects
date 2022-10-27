
import requests
from requests_html import HTMLSession
import time

def get__links(url):
    session = HTMLSession()
    r = session.get(url)
    return r.html.absolute_links


URL = ["https://ssc.nic.in", "https://bhartipur.in/", "https://sarkariresult.com/"]
if __name__ == "__main__":
    while True:
        old_links = []
        new_links = []
        for i in URL:
            old_links.append(get__links(i))
        time.sleep(2)
        for i in URL:
            new_links.append(get__links(i))
            
    
        for i in range(len(old_links)):
            if old_links[i] == new_links[i]:
                # print("changed")
                token = "5677944998:AAG4LPvLtrANB0ZOIibNVNuKZvRXr9alROo"
                url = f"https://api.telegram.org/bot{token}"
                params = {"chat_id": "5710153306", "text": "changes detected", }
                r = requests.get(url + "/sendMessage", params=params)
             
       
