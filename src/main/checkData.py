import requests
import re
import bs4
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup

class Search:
	def __init__(self , tag):
		driver = webdriver.Chrome()
		webpage = driver.get('https://www.gsmarena.com/')
		searchbox = driver.find_element_by_xpath('/html/body/header/div/div/div[2]/form/input')
		searchbox.send_keys(tag)
		#searchbox.send_keys('samsung galaxy m30s')
		time.sleep(3)
		#go = driver.find_element_by_xpath('/html/body/header/div/div/div[2]/form/span/input')
		#go.click()
		searchbox.send_keys(Keys.ENTER)
		time.sleep(3)
		mobile = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/ul/li/a/img')
		mobile.click()
		time.sleep(3)
		URLm = driver.current_url
		image = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div[3]/ul/li[2]/a')
		image.click()
		time.sleep(3)
		URLi = driver.current_url
		driver.close()
		#print(URLm)
		#print(URLi)
####
		heading = ""
		row = []
		detail = []
		finalData = {}
		specification = {}
		r = requests.get(URLm)
		#r = requests.get("https://www.gsmarena.com/samsung_galaxy_m30s-9818.php")
		#soup = bs4.BeautifulSoup(open("C:\\Users\\user\\Desktop\\Project\\Automation\\sm30s.html"), 'html.parser')
		soup = bs4.BeautifulSoup(r.content, 'html.parser')

		name = soup.find('h1', attrs = {'class':'specs-phone-name-title'})
		name = name.text
		finalData.update({'name':name})
		finalData.update({'link':URLm})
		#print(name)
		specAll = soup.findAll('table')
		#print(spec)
		for spec in specAll:
			dataH = spec.findAll('th', attrs = {'scope':'row'})
			#print(spec)
			for data in dataH:
				#print(data.text)
				#heading.append(re.sub("\\xa0","",str(data.text)))
				heading = re.sub("\\xa0","",str(data.text))
				dataT = spec.findAll('td', attrs = {'class':'ttl'})
				row.clear()
				detail.clear()
				specification.clear()
				for datar in dataT:
					#print(data.text)
					rowd = re.sub("\\xa0","",str(datar.text))
					if rowd == '':
						#row = "BatteryOption"
						row.append("Option")
					else:
						#row = rowd
						row.append(rowd)
				dataD = spec.findAll('td', attrs = {'class':'nfo'})
				for datad in dataD:
					#print(data.text)
					txt = re.sub("\\xa0","",str(datad.text))
					txt = re.sub("\n","",str(txt))
					#detail = txt
					detail.append(txt)
				for i in range(len(row)):
					#print(heading+""+row[i]+" = finalData.get('"+heading+"').get('"+row[i]+"'),")
					specification.update({row[i]:detail[i]})
				for i in specification:
					finalData.update({heading:specification})
					#finalData[heading] = specification.values()
					#print(specification)
				heading = ""
				del specification
				specification = {}

		r = requests.get(URLi)
		soup = bs4.BeautifulSoup(r.content, 'html.parser')
		soup = re.sub("our photos</h2>","</div>",str(soup))
		soup = bs4.BeautifulSoup(soup, 'html.parser')
		divT = soup.find('div', attrs = {'id':'pictures-list'})
		#print(name)
		link = divT.findAll('img')
		i = 0
		for imgLink in link:
			specification.update({i:imgLink['src']})
			i = i + 1
		finalData.update({'image':specification})
		#for ilink in finalData.get('image').values():
		#    print(ilink)

		print(finalData)
		self.dataWP = finalData

def processWData(name):
    return Search(name)


"""
print(finalData.get('name'))
print(finalData.get('Network').get('Technology'))
print(finalData.get('Network').get('2G bands'))
print(finalData.get('Network').get('3G bands'))
print(finalData.get('Network').get('4G bands'))
print(finalData.get('Network').get('Speed'))

print(finalData.get('Launch').get('Announced'))
print(finalData.get('Launch').get('Status'))

print(finalData.get('Body').get('Dimensions'))
print(finalData.get('Body').get('Weight'))
print(finalData.get('Body').get('Build'))
print(finalData.get('Body').get('SIM'))

print(finalData.get('Display').get('Type'))
print(finalData.get('Display').get('Size'))
print(finalData.get('Display').get('Resolution'))
print(finalData.get('Display').get('Option'))

print(finalData.get('Platform').get('OS'))
print(finalData.get('Platform').get('Chipset'))
print(finalData.get('Platform').get('CPU'))
print(finalData.get('Platform').get('GPU'))

print(finalData.get('Memory').get('Card slot'))
print(finalData.get('Memory').get('Internal'))
print(finalData.get('Memory').get('Option'))

print(finalData.get('Main Camera').get('Triple'))
print(finalData.get('Main Camera').get('Features'))
print(finalData.get('Main Camera').get('Video'))

print(finalData.get('Selfie camera').get('Single'))
print(finalData.get('Selfie camera').get('Features'))
print(finalData.get('Selfie camera').get('Video'))

print(finalData.get('Sound').get('Loudspeaker '))
print(finalData.get('Sound').get('3.5mm jack '))

print(finalData.get('Comms').get('WLAN'))
print(finalData.get('Comms').get('Bluetooth'))
print(finalData.get('Comms').get('GPS'))
print(finalData.get('Comms').get('Radio'))
print(finalData.get('Comms').get('USB'))

print(finalData.get('Features').get('Sensors'))

print(finalData.get('Battery').get('Option'))
print(finalData.get('Battery').get('Charging'))

print(finalData.get('Misc').get('Colors'))
print(finalData.get('Misc').get('Models'))
print(finalData.get('Misc').get('SAR'))
print(finalData.get('Misc').get('SAR EU'))
print(finalData.get('Misc').get('Price'))

print(finalData.get('Tests').get('Performance'))
print(finalData.get('Tests').get('Display'))
print(finalData.get('Tests').get('Camera'))
print(finalData.get('Tests').get('Audio quality'))
print(finalData.get('Tests').get('Battery life'))
"""
