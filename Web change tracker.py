
import requests
from requests_html import HTMLSession
import time
import urllib.request
from datetime import datetime

# version1 = requests.get("https://ssc.nic.in")
# soup = BeautifulSoup(version1.content, "html.parser")



#get all links
def get__links(url):
    session = HTMLSession()
    r = session.get(url)
    return r.html.absolute_links



# s = Timer(2.0, get__links, args={URL[0]}).start()
# old_links = []
# new_links = []

# for i in URL:
#     old_links.append(get__links(i))

# # time.sleep(2)

# for i in URL:
#     new_links.append(get__links(i))
#     if old_links != new_links:
#         print("changed")
#     else:
#         print("no change")


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
             
       