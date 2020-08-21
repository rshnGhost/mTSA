import requests
import re
import bs4
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup
class Search:
    def __init__(self , tag):
        print("here2")
        driver = webdriver.Chrome()
        webpage = driver.get('https://www.devicespecifications.com/en')
        searchbox = driver.find_element_by_xpath('/html/body/div[1]/div/input')
        searchbox.send_keys(tag)#'samsung galaxy m30s')
        time.sleep(3)
        searchbox.send_keys(Keys.ENTER)
        self.URL = driver.current_url
        driver.close()
        #self.URL = "https://www.devicespecifications.com/en/model/d9da5412"
        r = requests.get(self.URL)
        soup = bs4.BeautifulSoup(r.content, 'html.parser')
        #soup = soup.prettify()
        #print(soup)
        content = re.sub(": ","<b>",str(soup))
        content = re.sub("<br/>","</b>",str(content))
        content = re.sub(", <b>","</b><b>",str(content))
        content = re.sub(','," +",str(content))
        #print(content)
        content = bs4.BeautifulSoup(content, 'html.parser')
        #print(soup)
        spec = content.find('h1')
        self.data = []
        if spec:
            self.data.append(spec.text.split(" - ")[0])
            print(self.data)
        spec = content.find('div', attrs = {'id':'model-brief-specifications'})
        #[x.extract() for x in content.findAll('span')]
        #[x.extract() for x in content.findAll('a')]
        #print(spec)
        i = 0
        #j = 0
        #self.heading = []
        for row in spec.findAll('b'):
            if (i%2)!=0:
                #print(row.text)
                self.data.append(row.text)
            #else if j != 0:
                #print(row.text)
                #heading.append(row.text)
                #j = 1
            i+=1
        #print(heading)
        #print(data)

def processSpec(name):
    return Search(name)
