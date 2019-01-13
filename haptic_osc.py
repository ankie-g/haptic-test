from __future__ import division
from time import sleep
import OSC
import math

i=0
def append(i):
	c = OSC.OSCClient()
	c.connect(('127.0.0.1', 7400))
	oscmsg = OSC.OSCMessage()
	oscmsg.setAddress("/amp")
	oscmsg.append(i)
	c.send(oscmsg)
	print(oscmsg)
	oscmsg.clearData()

while(i<=255):
	append(i)
	i = i+1
	sleep(round(1/255,3))



