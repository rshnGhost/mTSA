import requests, re
from bs4 import BeautifulSoup

#scrape the content
class Search:
    def __init__(self , os):
        print("here1")
        if os == "android":
            r = requests.get("http://www.antutu.com/en/ranking/rank1.htm")
        if os == "ios":
            r = requests.get("https://www.antutu.com/en/ranking/ios1.htm")
        soup = BeautifulSoup(r.content, 'html.parser')
        soup.prettify()
        content = soup.findAll('ul', attrs = {'class':'newrank-b'})
        for content in content:
            self.total = content.find('li', attrs = {'class':'blast'})
            self.total = (self.total.text)
            bench = re.sub("<li>","<p>",str(content))
            bench = re.sub("</li>","</p>",str(bench))
            bench = BeautifulSoup(bench, 'html.parser')
            bench.prettify()
            Ndata = bench.findAll('p')
            self.cpu = (Ndata[0].text)
            self.gpu = (Ndata[1].text)
            self.mem = (Ndata[2].text)
            self.ux = (Ndata[3].text)
            content = re.sub("</span>","_</span>",str(content))
            content = BeautifulSoup(content, 'html.parser')
            content.prettify()
            noTag = content.find('li', attrs = {'class':'bfirst'})
            self.ram = noTag.find('span', attrs = {'class':'memory'})
            data = content.find('li')
            no = (data.text.split('_'))[0]
            self.name = (data.text.split('_'))[1]
            self.name = re.sub("\d+\+\d*","",str(self.name))
            self.name = re.sub('\(','',str(self.name))
            self.name = re.sub('\)','',str(self.name))
            self.name = re.sub("\+"," Plus",str(self.name))
            self.ram = re.sub('\) _','',str(self.ram.text))
            self.ram = re.sub(' \(','',str(self.ram))

            #print(self.no)
            #print(self.name)
            #print(self.ram)
            #print(self.cpu)
            #print(self.gpu)
            #print(self.mem)
            #print(self.ux)
            #print(self.total)

def processBench(name):
    return Search(name)
