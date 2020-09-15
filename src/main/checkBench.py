import requests, re
from bs4 import BeautifulSoup

#scrape the content
class Search:
    def __init__(self , os):
        print("here1")
        headings = ["Name", "Ram", "Cpu", "Gpu", "Mem", "Ux", "Total"]
        row = []
        specification = {}
        self.dataBench = {}
        j = 1
        if os == "android":
            r = requests.get("http://www.antutu.com/en/ranking/rank1.htm")
            #soup = BeautifulSoup(open("C:\\Users\\user\\Desktop\\autoProject\\mTSA-master\\android.html","r",encoding='utf-8'), "html.parser")
        if os == "ios":
            r = requests.get("https://www.antutu.com/en/ranking/ios1.htm")
            #soup = BeautifulSoup(open("C:\\Users\\user\\Desktop\\autoProject\\mTSA-master\\ios.html","r",encoding='utf-8'), "html.parser")
        soup = BeautifulSoup(r.content, 'html.parser')
        soup.prettify()
        content = soup.find('div', attrs={"style":"float: right;color: #999999;margin-top: 30px;margin-right: 35px;"})
        self.month = re.sub("\*","",str(content.text))
        #print(re.sub("\*","",str(content.text)))
        content = soup.findAll('ul', attrs = {'class':'newrank-b'})
        for content in content:
            #print(content)
            #print("++++++++++++")
            total = content.find('li', attrs = {'class':'blast'})
            total = (total.text)
            bench = re.sub("<li>","<p>",str(content))
            bench = re.sub("</li>","</p>",str(bench))
            bench = BeautifulSoup(bench, 'html.parser')
            bench.prettify()
            Ndata = bench.findAll('p')
            cpu = (Ndata[0].text)
            gpu = (Ndata[1].text)
            mem = (Ndata[2].text)
            ux = (Ndata[3].text)
            content = re.sub("</span>","_</span>",str(content))
            content = BeautifulSoup(content, 'html.parser')
            content.prettify()
            noTag = content.find('li', attrs = {'class':'bfirst'})
            ram = noTag.find('span', attrs = {'class':'memory'})
            data = content.find('li')
            no = (data.text.split('_'))[0]
            name = (data.text.split('_'))[1]
            name = re.sub("\d+\+\d*","",str(name))
            name = re.sub('\(','',str(name))
            name = re.sub('\)','',str(name))
            name = re.sub("\+"," Plus",str(name))
            ram = re.sub('\) _','',str(ram.text))
            ram = re.sub(' \(','',str(ram))
            specification.clear()
            specification['name'] = name
            specification['ram'] = ram
            specification['cpu'] = cpu
            specification['gpu'] = gpu
            specification['mem'] = mem
            specification['ux'] = ux
            specification['total'] = total
            #specification.append(txt)
            #self.dataBench.update({j:specification})
            #print(self.dataBench)
            self.dataBench[j]=specification
            specification={}
            j = j+1

def processBench(name):
    return Search(name)
