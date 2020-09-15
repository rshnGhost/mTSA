from django.core.management.base import BaseCommand
from dataStorage.models import cache, phoneBench, phoneWeb, phoneImg, phoneData, antutu
import re, requests
from bs4 import BeautifulSoup
import os
import shutil
#from bs4 import BeautifulSoup
from main.checkSpec import processSpec
from main.checkBench import processBench
from main.checkData import processWData

name = ""
#PWD = os.path.dirname(os.path.realpath(__file__ ))
f1 = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))), 'Files')
PWD = os.path.join(f1 , 'mediaFile')
class Command(BaseCommand):
    help = 'Create a phone entry with the detials in cache'

    def add_arguments(self, parser):
        parser.add_argument('key', type=str)
        #parser.add_argument('name', nargs='+', type=str)

    def handle(self, *args, **options):
        #r = requests.get("http://www.antutu.com/en/ranking/rank1.htm")
        #soup = BeautifulSoup(open("C:\\Users\\user\\Desktop\\autoProject\\mTSA-master\\android.html","r",encoding='utf-8'), "html.parser")
        r = requests.get("https://www.antutu.com/en/ranking/ios1.htm")
        #soup = BeautifulSoup(open("C:\\Users\\user\\Desktop\\autoProject\\mTSA-master\\ios.html","r",encoding='utf-8'), "html.parser")
        soup = BeautifulSoup(r.content, 'html.parser')
        soup.prettify()
        content = soup.find('div', attrs={"style":"float: right;color: #999999;margin-top: 30px;margin-right: 35px;"})
        antutuObj = antutu.objects.last()
        #print(str(content))
        month = re.sub("\*","",str(content.text))
        key = options['key']
        if(antutuObj.month != month):
            try:
                android = processBench("android")
                antutuObj = antutu.objects.create(
                    month = android.month,
                    url = "http://www.antutu.com/en/ranking/rank1.htm",
                    type = "android"
                )
                antutuObj.save()
                ios = processBench("ios")
                antutuObj = antutu.objects.create(
                    month = ios.month,
                    url = "https://www.antutu.com/en/ranking/ios1.htm",
                    type = "ios"
                )
                antutuObj.save()
            except:
                print("error[processBench(connection)]")
                pass
            #print(android.dataBench)
            for dataIn in android.dataBench:
                print(">"+android.dataBench.get(dataIn).get('name').strip()+"<")
                try:
                    dataAndroid = phoneBench.objects.create(
                        month = month,
                        device = android.dataBench.get(dataIn).get('name').strip(),
                    	modelNo = re.sub(" ","",str(android.dataBench.get(dataIn).get('name'))),
                    	ram = android.dataBench.get(dataIn).get('ram'),
                    	cpu = android.dataBench.get(dataIn).get('cpu'),
                        gpu = android.dataBench.get(dataIn).get('gpu'),
                        mem = android.dataBench.get(dataIn).get('mem'),
                    	ux = android.dataBench.get(dataIn).get('ux'),
                    	total = android.dataBench.get(dataIn).get('total')
                    )
                    dataAndroid.save()
                except:
                    print("error[android]")
                    pass
            for dataIn in ios.dataBench:
                #print(ios.dataBench.get(dataIn).get('total'))
                try:
                    dataIos = phoneBench.objects.create(
                        month = month,
                        device = ios.dataBench.get(dataIn).get('name').strip(),
                    	modelNo = re.sub(" ","",str(ios.dataBench.get(dataIn).get('name'))),
                    	ram = ios.dataBench.get(dataIn).get('ram'),
                    	cpu = ios.dataBench.get(dataIn).get('cpu'),
                        gpu = ios.dataBench.get(dataIn).get('gpu'),
                        mem = ios.dataBench.get(dataIn).get('mem'),
                    	ux = ios.dataBench.get(dataIn).get('ux'),
                    	total = ios.dataBench.get(dataIn).get('total')
                    )
                    dataIos.save()
                except:
                    print("error[ios]")
                    pass
        cacheObject = cache.objects.filter(satuts = False)
        if key == "selected":
            for object in cacheObject:
                try:
                    pBObj = phoneBench.objects.filter(device = object.name)
                    if pBObj.count() == 1:
                        print('%s --> %s' % (object.id, object.name))
                except:
                    print("error[phoneBench]")
                    pass
            id = input("Select an ID : ")
            cacheObject = cache.objects.filter(satuts = False, id = id)
        for object in cacheObject:
            ####
            mname = re.sub(" ","",str(object.name))
            pWObject = phoneWeb.objects.filter(name = object.name)
            if pWObject.count() != 0:
                try:
                    finalData = processWData(object.name)
                except:
                    print("error[processWData]")
                    pass
                finalData = (finalData.dataWP)
                name  = finalData.get('name')
                print(finalData)
                try:
                    pWObject = phoneWeb.objects.create(
                    	name  = finalData.get('name'),
                    	link = finalData.get('link'),
                    	NetworkTechnology = finalData.get('Network').get('Technology'),
                    	Network2Gbands = finalData.get('Network').get('2G bands'),
                    	Network3Gbands = finalData.get('Network').get('3G bands'),
                    	Network4Gbands = finalData.get('Network').get('4G bands'),
                    	NetworkSpeed = finalData.get('Network').get('Speed'),
                    	LaunchAnnounced = finalData.get('Launch').get('Announced'),
                    	LaunchStatus = finalData.get('Launch').get('Status'),
                    	BodyDimensions = finalData.get('Body').get('Dimensions'),
                    	BodyWeight = finalData.get('Body').get('Weight'),
                    	BodyBuild = finalData.get('Body').get('Build'),
                    	BodySIM = finalData.get('Body').get('SIM'),
                    	DisplayType = finalData.get('Display').get('Type'),
                    	DisplaySize = finalData.get('Display').get('Size'),
                    	DisplayResolution = finalData.get('Display').get('Resolution'),
                    	DisplayOption = finalData.get('Display').get('Option'),
                    	PlatformOS = finalData.get('Platform').get('OS'),
                    	PlatformChipset = finalData.get('Platform').get('Chipset'),
                    	PlatformCPU = finalData.get('Platform').get('CPU'),
                    	PlatformGPU = finalData.get('Platform').get('GPU'),
                    	MemoryCardslot = finalData.get('Memory').get('Card slot'),
                    	MemoryInternal = finalData.get('Memory').get('Internal'),
                    	MemoryOption = finalData.get('Memory').get('Option'),
                    	MainCameraTriple = finalData.get('Main Camera').get('Triple'),
                    	MainCameraFeatures = finalData.get('Main Camera').get('Features'),
                    	MainCameraVideo = finalData.get('Main Camera').get('Video'),
                    	SelfiecameraSingle = finalData.get('Selfie camera').get('Single'),
                    	SelfiecameraFeatures = finalData.get('Selfie camera').get('Features'),
                    	SelfiecameraVideo = finalData.get('Selfie camera').get('Video'),
                    	SoundLoudspeaker  = finalData.get('Sound').get('Loudspeaker '),
                    	Sound35mmjack  = finalData.get('Sound').get('3.5mm jack '),
                    	CommsWLAN = finalData.get('Comms').get('WLAN'),
                    	CommsBluetooth = finalData.get('Comms').get('Bluetooth'),
                    	CommsGPS = finalData.get('Comms').get('GPS'),
                    	CommsRadio = finalData.get('Comms').get('Radio'),
                    	CommsUSB = finalData.get('Comms').get('USB'),
                    	FeaturesSensors = finalData.get('Features').get('Sensors'),
                    	BatteryOption = finalData.get('Battery').get('Option'),
                    	BatteryCharging = finalData.get('Battery').get('Charging'),
                    	MiscColors = finalData.get('Misc').get('Colors'),
                    	MiscModels = finalData.get('Misc').get('Models'),
                    	MiscSAR = finalData.get('Misc').get('SAR'),
                    	MiscSAREU = finalData.get('Misc').get('SAR EU'),
                    	MiscPrice = finalData.get('Misc').get('Price'),
                    	TestsPerformance = finalData.get('Tests').get('Performance'),
                    	TestsDisplay = finalData.get('Tests').get('Display'),
                    	TestsCamera = finalData.get('Tests').get('Camera'),
                    	TestsAudioquality = finalData.get('Tests').get('Audio quality'),
                    	TestsBatterylife = finalData.get('Tests').get('Battery life')
                    )
                    pWObject.save()
                    i = 0
                    for ilink in finalData.get('image').values():
            		    #print(ilink)
                        path = mname
                        outfolder=os.path.join(PWD, path)
                        if not os.path.exists(outfolder):
                            os.makedirs(outfolder)
                        print(ilink)
                        filename = mname+"["+str(i)+"].jpg"
                        i = i + 1
                        r = requests.get(ilink, stream = True)
                        outpath = os.path.join(outfolder, filename)
                        print(outpath)
                        with open(outpath,'wb') as f:
                            shutil.copyfileobj(r.raw, f)
                        iObject = phoneImg.objects.create(
                            modelNo = mname,
                        	picture = mname+"/"+filename,
                        )
                        iObject.save()
                except:
                    print("error[phoneWeb]")
                    pass
            ####
                try:
                    #mname = re.sub(" ","",str(name))
                    pDObject = phoneData.objects.create(
                    	name  = finalData.get('name'),
                    	#link = finalData.get('link'),
                    	modelNo = mname,
                    	network = finalData.get('Network').get('Technology'),
                    	launch = finalData.get('Launch').get('Announced'),
                    	body = finalData.get('Body').get('Dimensions'),
                    	display = finalData.get('Tests').get('Display'),
                    	platform = finalData.get('Platform').get('OS'),
                    	memory = finalData.get('Memory').get('Internal'),
                    	camera = finalData.get('Tests').get('Camera'),
                    	gpu = finalData.get('Platform').get('GPU'),
                    	dimension = finalData.get('Display').get('Size'),
                    	battery = finalData.get('Battery').get('Charging'),
                    	price = 1000,#finalData.get('Misc').get('Price'),
                        picture = mname+"/"+mname+"[0].jpg"#"OnePlus8Pro/OnePlus8Pro[1].jpg"
                    )
                    pDObject.save()
                except:
                    print("error[phoneData]")
                    pass
            else:
                try:
                    pDObject = phoneData.objects.create(
                    	name  = pWObject.name,
                    	#link = finalData.get('link'),
                    	modelNo = mname,
                    	network = pWObject.NetworkTechnology,
                    	launch = pWObject.LaunchAnnounced,
                    	body = pWObject.BodyDimensions,
                    	display = pWObject.TestsDisplay,
                    	platform = pWObject.PlatformOS,
                    	memory = pWObject.MemoryInternal,
                    	camera = pWObject.TestsCamera,
                    	gpu = pWObject.PlatformGPU,
                    	dimension = pWObject.DisplaySize,
                    	battery = pWObject.BatteryCharging,
                    	price = 1000,#finalData.get('Misc').get('Price'),
                        picture = mname+"/"+mname+"[0].jpg"#"OnePlus8Pro/OnePlus8Pro[1].jpg"
                    )
                    pDObject.save()
                except:
                    print("error[phoneData]")
                    pass
            ###
            #mname = re.sub(" ","",str(name))
            ###
            '''pBenchObject = phoneBench.objects.filter(device = object.name)
            if pBenchObject.count() == 0:
                pass
            else:
                try:
                    data = processSpec(object.name)
                except:
                    print("error[processSpec]")
                    pass
                detail = eval(str(data.data))
                #print(detail[5])
                #tag = str(re.sub(" ","",str(name))
                cpu  = 9999
                ux  = 9999
                ddd  = 9999
                total  = 9999
                try:
                    pObject = phoneBench.objects.create(
                            device = str(name),
                        	modelNo = mname,
                        	ram = str(detail[7]),
                        	cpu  = 9999,
                        	ux  = 9999,
                        	ddd  = 9999,
                        	total  = 9999,
                        	nt = 0,
                        	net = 0,
                        	pt = 0,
        			)
                    pObject.save()
                except:
                    print("error[phoneBench]")
                    pass'''
            detail = object.name
            t = cache.objects.get(name = object.name)
            t.satuts = True
            t.tag = mname#re.sub(" ","",str(detail[0])),
            t.save()
            if detail:
                print('Successfully searched and found for %s' % object.name)
            else:
                print('Phone %s is not created' % object.name)
