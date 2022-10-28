# from ensurepip import version
import hashlib
# from nturl2path import url2pathname
import requests
# from bs4 import BeautifulSoup
from requests_html import HTMLSession
# from threading import Timer
import time
import urllib.request
from datetime import datetime

# version1 = requests.get("https://ssc.nic.in")
# soup = BeautifulSoup(version1.content, "html.parser")






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


print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
URL =  ["https://www.mha.gov.in/",
        "https://www.assamrifles.gov.in/english/",
        "https://www.bpsc.bih.nic.in/",
        "https://joinindianarmy.nic.in/",
        "https://afcat.cdac.in/AFCAT/",
        "https://indianairforce.nic.in/",
        "https://indiannavy.nic.in/",
        "https://www.joinindiannavy.gov.in/",
        "https://www.bpsc.bih.nic.in/",
        "https://joinindianarmy.nic.in/",
        "https://afcat.cdac.in/AFCAT/",
        "https://indianairforce.nic.in/",
        "https://indiannavy.nic.in/",
        "https://www.joinindiannavy.gov.in/",
        "https://rpsc.rajasthan.gov.in/advertisements",
        "https://www.cisfrectt.in/",
        "https://ctet.nic.in/",
        "https://www.bpssc.bih.nic.in/",
        "https://www.bpsc.bih.nic.in/",
        "https://www.jpsc.gov.in/",
        "https://jceceb.jharkhand.gov.in/",
        "https://vyapam.cgstate.gov.in/",
        "https://student.nielit.gov.in/",
        "https://upcet.nta.nic.in/",
        "https://updeled.gov.in/"]

old_links = []
new_links = []

headers = requests.utils.default_headers()

headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

def send_telegram_text(URL_TO_MONITOR, changed_link):
    token = "5677944998:AAG4LPvLtrANB0ZOIibNVNuKZvRXr9alROo"
    url = f"https://api.telegram.org/bot{token}"
    params = {"chat_id": "5710153306", "text": f"changes detected on {URL_TO_MONITOR}, the link is {changed_link}"}
    r = requests.get(url + "/sendMessage", params=params)

session = HTMLSession()
def get__links(url):
    r = session.get(url, headers=headers)
    return r.html.absolute_links


if __name__ == "__main__":
    while True:
        for url in URL:
            old_links.append(get__links(url))
            # print(old_links)

        time.sleep(1)

        for url in URL:
            new_links.append(get__links(url))
            
    
        for i in range(len(URL)):
            final_set = old_links[i].union(new_links[i]) - old_links[i].intersection(new_links[i])
            if len(final_set) > 0:
                send_telegram_text(URL[i], final_set)
                print("changed")
            # if old_links[i] != new_links[i]:
            #     send_telegram_text(URL[i])
            else:
                print("no change")
                print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
                send_telegram_text(URL[i], final_set)
             
#"https://navodaya.gov.in/nvs/en/Recruitment/Notification-Vacancies/",
        # "https://www.bpsc.bih.nic.in/",
        # "https://joinindianarmy.nic.in/latest-rally-jcos-or.htm",
        # "https://afcat.cdac.in/AFCAT/",
        # "https://indianairforce.nic.in/",
        # "https://indiannavy.nic.in/",
        # "https://www.joinindiannavy.gov.in/",
        # "https://rpsc.rajasthan.gov.in/advertisements",
        # "https://www.cisfrectt.in/",
        # "https://ctet.nic.in/",
        # "https://www.bpssc.bih.nic.in/",
        # "https://www.bpsc.bih.nic.in/",
        # "https://www.jpsc.gov.in/online_application.php",
        # "https://jceceb.jharkhand.gov.in/",
        # "https://vyapam.cgstate.gov.in/",
        # "https://student.nielit.gov.in/",
        # "https://upcet.nta.nic.in/",
        # "https://updeled.gov.in/",
        # "https://uppsc.up.nic.in/Notifications.aspx",
        # "https://www.uprvunl.org/recruitment-notices",
        # "https://upnrhm.gov.in/home/update_news_detail",
        # "https://consortiumofnlus.ac.in/clat-2022/",
        # "https://nta.ac.in/Home",
        # "https://aissee.nta.nic.in/",
        # "https://www.mha.gov.in/notifications/vacancies",
        # "https://bsf.gov.in/",
        # "https://mpsc.gov.in/",
        # "https://www.idbibank.in/idbi-bank-careers-current-openings.aspx",
        # "https://www.coalindia.in/",
        # "https://www.ibps.in/",
        # "https://www.pib.gov.in/indexd.aspx",
        # "https://pariksha.nic.in/Online_App/Notifications.aspx"