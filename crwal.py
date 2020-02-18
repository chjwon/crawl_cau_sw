import urllib.request as ur
from bs4 import BeautifulSoup
#import datetime
import time
#import threading



notice_page = ur.urlopen("https://cse.cau.ac.kr/sub05/sub0501.php")
target_page = BeautifulSoup(notice_page,"html.parser")
#type is bs4.BeautifulSoup

page_body = target_page.find("section",{"id":"middle"})
div = page_body.div
section = div.find("section",{"id":"content"})
print(section.div.h2)
print()

form = section.find("form",{"id":"listpage_form"})
tbody = form.table.tbody
recent_notice = tbody.tr
recent_notice_url = recent_notice.find("td",{"class":"aleft"})

page_number = str(recent_notice_url.a)[65:69]
notice_title = str(recent_notice_url.a)[139:-12]



def cau_crawl(curr_minute):
    print(notice_title)

while True :
    time_=int(time.time())%3600%180
    print("Enter \"stop\" if you want to stop")
    if (time_ ==0 or 60 or 120):
        cau_crawl(1)
    whether_stop = input()
    if(whether_stop == 'stop'):
        break   

print("-----------------------------------------")

complete_url = "https://cse.cau.ac.kr/sub05/sub0501.php" + "?dir=bbs&nmode=view&code=oktomato_bbs05&uid=" + page_number + "&search=&keyword=&temp1=&offset=1"
print(complete_url)

