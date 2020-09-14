from django.core.management.base import BaseCommand
from dataStorage.models import cache, phoneBench, phoneWeb, phoneImg
import re, requests
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
        key = options['key']
        android = processBench("android")
        ios = processBench("ios")
        #print(android.dataBench)
        for dataIn in android.dataBench:
            #print(android.dataBench.get(dataIn).get('name'))
            try:
                dataAndroid = phoneBench.objects.create(
                    device = android.dataBench.get(dataIn).get('name'),
                	modelNo = android.dataBench.get(dataIn).get('name'),
                	ram = android.dataBench.get(dataIn).get('ram'),
                	cpu = android.dataBench.get(dataIn).get('cpu'),
                	ux = android.dataBench.get(dataIn).get('ux'),
                	ddd = android.dataBench.get(dataIn).get('mem'),
                	total = android.dataBench.get(dataIn).get('total')
                )
                dataAndroid.save()
            except:
                print("error")
                pass
        for dataIn in ios.dataBench:
            #print(ios.dataBench.get(dataIn).get('total'))
            try:
                dataIos = phoneBench.objects.create(
                    device = ios.dataBench.get(dataIn).get('name'),
                	modelNo = ios.dataBench.get(dataIn).get('name'),
                	ram = ios.dataBench.get(dataIn).get('ram'),
                	cpu = ios.dataBench.get(dataIn).get('cpu'),
                	ux = ios.dataBench.get(dataIn).get('ux'),
                	ddd = ios.dataBench.get(dataIn).get('mem'),
                	total = ios.dataBench.get(dataIn).get('total')
                )
                dataIos.save()
            except:
                print("error[ios]")
                pass
        cacheObject = cache.objects.filter(satuts = False)
        if key == "selected":
            for object in cacheObject:
                print('%s --> %s' % (object.id, object.name))
            id = input("Select an ID : ")
            cacheObject = cache.objects.filter(satuts = False, id = id)
        for object in cacheObject:
            ####
            finalData = processWData(object.name)
            finalData = (finalData.dataWP)
            name  = finalData.get('name')
            print(finalData)
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
            ####
            ###
            mname = re.sub(" ","",str(name))
            i = 0
            for ilink in finalData.get('image').values():
    		    #print(ilink)
                path = ".\\"+mname
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
            ###
            data = processSpec(object.name)
            detail = eval(str(data.data))
            #print(detail[5])
            #tag = str(re.sub(" ","",str(name))
            cpu  = 9999
            ux  = 9999
            ddd  = 9999
            total  = 9999
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
            t = cache.objects.get(name = object.name)
            t.satuts = True
            t.tag = mname#re.sub(" ","",str(detail[0])),
            t.save()
            if detail:
                print('Successfully searched and found for %s' % object.name)
            else:
                print('Phone %s is not created' % object.name)
