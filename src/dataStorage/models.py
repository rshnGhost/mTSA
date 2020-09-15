from django.db import models
from django.conf import settings
from django.conf.urls.static import static
from django.db.models.signals import pre_save

def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    phoneData = instance.__class__
    #new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(instance.modelNo, filename)

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	phoneImg.modelNo = instance.modelNo
	phoneImg.image = instance.picture
	#if not instance.slug:
	# instance.slug = create_slug(instance)
	#instance.slug = unique_slug_generator(instance)

#CREATE YOUR TABLES HERE

class phoneBench(models.Model):
    month = models.CharField(max_length=140 ,unique=False)
    device = models.CharField(max_length=250)
    modelNo = models.CharField(max_length=250, unique=True)
    ram = models.CharField(max_length=250)
    cpu  = models.IntegerField(null=True)
    gpu  = models.IntegerField(null=True)
    mem  = models.IntegerField(null=True)
    ux  = models.IntegerField(null=True)
    total  = models.IntegerField(null=True)
    nt = models.IntegerField(null=True)
    net = models.IntegerField(null=True)
    pt = models.IntegerField(null=True)

    def __str__(self):
        return '%s' % self.device

    def __unicode__(self):
        return '%s' % self.device

    class Meta:
        ordering = ["-device", "-total"]

class phoneData(models.Model):
	name = models.CharField(max_length=250,null=True)
	modelNo = models.CharField(max_length=250, unique=True)
	network  = models.CharField(max_length=250,null=True)
	launch  = models.CharField(max_length=250,null=True)
	body  = models.CharField(max_length=250,null=True)
	display  = models.CharField(max_length=250,null=True)
	platform  = models.CharField(max_length=250,null=True)
	memory  = models.CharField(max_length=250,null=True)
	camera = models.CharField(max_length=250,null=True)
	gpu = models.CharField(max_length=250,null=True)
	dimension = models.CharField(max_length=250,null=True)
	battery  = models.CharField(max_length=250,null=True)
	price  = models.IntegerField(null=True)
	#picture = models.FileField(upload_to= 'pic/', default='pic/none/default.png')
	#picture = models.FileField(upload_to = upload_location, blank=False)
	picture = models.FileField(upload_to = upload_location, blank=True)

	def __str__(self):
		return '%s' % self.name

	def __unicode__(self):
		return '%s' % self.name

	class Meta:
		ordering = ["-name", "-modelNo"]

class antutu(models.Model):
    month = models.CharField(max_length=140 ,unique=False)
    url = models.CharField(max_length=140 ,unique=False)
    type = models.CharField(max_length=140 ,unique=False)

    def __str__(self):
        return self.month+"["+self.type+"]"

class PosTweet(models.Model):
    posphone = models.ForeignKey(phoneBench, related_name='PosTweet' ,on_delete=models.CASCADE)
    tag = models.CharField(max_length=140 ,unique=False)
    text = models.CharField(max_length=140 ,unique=True)

    def __str__(self):
        return self.tag

class NegTweet(models.Model):
    negphone = models.ForeignKey(phoneBench, related_name='NegTweet' ,on_delete=models.CASCADE)
    tag = models.CharField(max_length=140 ,unique=False)
    text = models.CharField(max_length=140 ,unique=True)

    def __str__(self):
        return self.tag

class NeuTweet(models.Model):
    neuphone = models.ForeignKey(phoneBench, related_name='NeuTweet' ,on_delete=models.CASCADE)
    tag = models.CharField(max_length=140 ,unique=False)
    text = models.CharField(max_length=140 ,unique=True)

    def __str__(self):
        return self.tag

class cache(models.Model):
    name = models.CharField(max_length=140, unique=True)
    tag = models.CharField(max_length=140)
    satuts = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class phoneImg(models.Model):
	modelNo = models.CharField(max_length=140 ,null=True)
	picture = models.FileField(upload_to = upload_location, blank=False)

	def __str__(self):
		return '%s' % self.modelNo

	def __unicode__(self):
		return '%s' % self.modelNo

	class Meta:
		ordering = ["-modelNo"]

class phoneWeb(models.Model):
	name  = models.CharField(max_length=250 ,null=True)
	link = models.CharField(max_length=250 ,null=True)
	NetworkTechnology = models.CharField(max_length=250 ,null=True)
	Network2Gbands = models.CharField(max_length=250 ,null=True)
	Network3Gbands = models.CharField(max_length=250 ,null=True)
	Network4Gbands = models.CharField(max_length=250 ,null=True)
	NetworkSpeed = models.CharField(max_length=250 ,null=True)
	LaunchAnnounced = models.CharField(max_length=250 ,null=True)
	LaunchStatus = models.CharField(max_length=250 ,null=True)
	BodyDimensions = models.CharField(max_length=250 ,null=True)
	BodyWeight = models.CharField(max_length=250 ,null=True)
	BodyBuild = models.CharField(max_length=250 ,null=True)
	BodySIM = models.CharField(max_length=250 ,null=True)
	DisplayType = models.CharField(max_length=250 ,null=True)
	DisplaySize = models.CharField(max_length=250 ,null=True)
	DisplayResolution = models.CharField(max_length=250 ,null=True)
	DisplayOption = models.CharField(max_length=250 ,null=True)
	PlatformOS = models.CharField(max_length=250 ,null=True)
	PlatformChipset = models.CharField(max_length=250 ,null=True)
	PlatformCPU = models.CharField(max_length=250 ,null=True)
	PlatformGPU = models.CharField(max_length=250 ,null=True)
	MemoryCardslot = models.CharField(max_length=250 ,null=True)
	MemoryInternal = models.CharField(max_length=250 ,null=True)
	MemoryOption = models.CharField(max_length=250 ,null=True)
	MainCameraTriple = models.CharField(max_length=250 ,null=True)
	MainCameraFeatures = models.CharField(max_length=250 ,null=True)
	MainCameraVideo = models.CharField(max_length=250 ,null=True)
	SelfiecameraSingle = models.CharField(max_length=250 ,null=True)
	SelfiecameraFeatures = models.CharField(max_length=250 ,null=True)
	SelfiecameraVideo = models.CharField(max_length=250 ,null=True)
	SoundLoudspeaker  = models.CharField(max_length=250 ,null=True)
	Sound35mmjack  = models.CharField(max_length=250 ,null=True)
	CommsWLAN = models.CharField(max_length=250 ,null=True)
	CommsBluetooth = models.CharField(max_length=250 ,null=True)
	CommsGPS = models.CharField(max_length=250 ,null=True)
	CommsRadio = models.CharField(max_length=250 ,null=True)
	CommsUSB = models.CharField(max_length=250 ,null=True)
	FeaturesSensors = models.CharField(max_length=250 ,null=True)
	BatteryOption = models.CharField(max_length=250 ,null=True)
	BatteryCharging = models.CharField(max_length=250 ,null=True)
	MiscColors = models.CharField(max_length=250 ,null=True)
	MiscModels = models.CharField(max_length=250 ,null=True)
	MiscSAR = models.CharField(max_length=250 ,null=True)
	MiscSAREU = models.CharField(max_length=250 ,null=True)
	MiscPrice = models.CharField(max_length=250 ,null=True)
	TestsPerformance = models.CharField(max_length=250 ,null=True)
	TestsDisplay = models.CharField(max_length=250 ,null=True)
	TestsCamera = models.CharField(max_length=250 ,null=True)
	TestsAudioquality = models.CharField(max_length=250 ,null=True)
	TestsBatterylife = models.CharField(max_length=250 ,null=True)

	def __str__(self):
		return self.name

#from .utils import unique_slug_generator
pre_save.connect(pre_save_post_receiver, sender=phoneData)
