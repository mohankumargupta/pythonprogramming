#class
# class variables versus instance variables

class lightbulb(object):
	ON = 1
	OFF = 0
    
	def __init__(self):
		self.state = lightbulb.OFF;
	
	def turnLightOn(self):
 		self.state = lightbulb.ON
 	
	def turnLightOff(self):
		self.state = lightbulb.OFF

	def printHumanReadableState(self):
		if (self.state):
			return "ON"
		else:
			return "OFF"

boo = lightbulb()
print(boo.state)
boo.turnLightOn()
print(boo.state)
print(boo.printHumanReadableState())
boo.turnLightOff()
print(boo.state)
print(boo.printHumanReadableState())
print(dir(lightbulb))
print(lightbulb.ON)
print(lightbulb.OFF)

