class Test:
	def __init__(self , tag):
		self.pt = 500+1
		self.nt = 400+1
		self.net = 50+1
		self.tt = 950+1
		self.name = str(tag)


def process1(tag):
	#return T()
	d = dict()
	d['name'] = str(tag)
	d['pt'] = 500
	d['nt'] = 400
	d['net'] = 50
	d['tt'] = 950
	return d

def process(tag):
	return Test(tag)

#main(tag)
