import OSC
c = OSC.OSCClient()
c.connect(('127.0.0.1', 7400))   # connect to SuperCollider
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/test10")
oscmsg.append(10)
c.send(oscmsg)
oscmsg.clearData();
oscmsg.setAddress("/test3")
oscmsg.append(3)
c.send(oscmsg)
