import qi
import functools
import time
import sys
import os
import argparse
from datetime import datetime
import subprocess



class attendancetaker(object):
    """
    A simple class to react to face detection events.
    """
    def onTouched(self, strVarName, value):
        """ This will be called each time a touch
        is detected.

        """
        # Disconnect to the event when talking,
        # to avoid repetitions
        self.touch.signal.disconnect(self.id)

        touched_bodies = []
        for p in value:
            if p[1]:
                touched_bodies.append(p[0])

        self.sss(touched_bodies) # gets all the touched bodies array 


        # Reconnect again to the event
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

    def sss(self, bodies):

    	batcmd = ("python Face_Recognition_Module.py") # variable used to 

        if (bodies == []):
            return
        else:
            touched1 =  bodies[1]
            print touched1
        if (touched1 == 'Head/Touch/Front'):
            self.tts.say ("Hi there  \\pau=100\\ my name is Nao \\pau=100\\ im the attendance robot " )
        if (touched1 == 'Head/Touch/Middle'):
            self.tts.say ("Touch the back of my head  \\pau=100\\ to start attendance" )
        if (touched1 == 'Head/Touch/Rear'):
            self.tts.say ("Attendance started" )
            restuls = subprocess.check_output(batcmd, shell=True)
            file = open('output.txt','w')
            file.write(restuls)
            file.close()
            file = open ('output.txt', 'r+')
            cc23 = (file.read(8))
            cc24 = (file.readline())
            cc25 = (file.readline())
            cc26 = (file.readline())
            cc27 = (file.readline())
            if(cc23 == "12345678"):
            	self.tts.say ("You are not a student \\pau=100\\  in this class \\pau=100\\ or you are not in the \\pau=100\\ faces folder")
            elif (cc23 == "1-people"):
            	self.tts.say("Welcome to " + cc26  + "\\pau=100\\" + cc25 )
            	self.tts.say(cc27)
            else:
            	self.tts.say("Nao can not   recognize your face \\pau=100\\ or more then two  people present")
          
        
      
    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(attendancetaker, self).__init__()
        app.start()
        session = app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        self.memory_service = session.service("ALMemory")
        # Connect the event callback.
        #self.subscriber = self.memory.subscriber("FaceDetected")
        #self.subscriber.signal.connect(self.on_human_tracked)
        self.touch = self.memory_service.subscriber("TouchChanged")
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))
        # Get the services ALTextToSpeech and ALFaceDetection.
        self.tts = session.service("ALTextToSpeech")
        #self.face_detection = session.service("ALFaceDetection")
        #self.face_detection.subscribe("HumanGreeter")
        #self.got_face = False
    '''
    def on_human_tracked(self, value):
        if value == []:
            self.got_face = False
        elif not self.got_face:
            self.got_face = True
            #self.tts.say("Hello, Im the attendance robot  pau=100 touch the back of my head to  start attendance")
    '''
    
    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting Attendance Taker"
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping attendance taker"
            self.face_detection.unsubscribe("attendancetaker")
            #stop
            sys.exit(0)
            


    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.141",
                        help="Robot IP address. On robot or Local Naoqi: use '192.168.1.141'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["attendancetaker", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    human_greeter = attendancetaker(app)
    human_greeter.run()
    