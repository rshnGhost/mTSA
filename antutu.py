import requests, re
from bs4 import BeautifulSoup

#r = requests.get("http://www.antutu.com/en/ranking/rank1.htm")
soup = BeautifulSoup(open("C:\\Users\\user\\Desktop\\autoProject\\mTSA-master\\android.html","r",encoding='utf-8'), "html.parser")
#r = requests.get("https://www.antutu.com/en/ranking/ios1.htm")
#soup = BeautifulSoup(open("C:\\Users\\user\\Desktop\\autoProject\\mTSA-master\\ios.html","r",encoding='utf-8'), "html.parser")
#soup = BeautifulSoup(r.content, 'html.parser')
soup.prettify()
content = soup.find('div', attrs={"style":"float: right;color: #999999;margin-top: 30px;margin-right: 35px;"})
print(re.sub("\*","",str(content.text)))
