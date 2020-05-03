#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to get & read FaceDetected Events"""

import qi
import functools
import time
import sys
import argparse
from datetime import datetime



class attendancetaker(object):                       # starts taking attendence
    """
    A simple class to react to face detection events.
    """
    def onTouched(self, strVarName, value):       # When touch is detected on NAO's head, this function start running the program.
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

        self.sss(touched_bodies)

                                                            # Reconnect again to the event
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

    def sss(self, bodies):
        if (bodies == []):
            return
        else:
            touched1 =  bodies[1]
            print touched1
        if (touched1 == 'Head/Touch/Front'):
            self.tts.say ("Welcome to  \\pau=100\\ CSC 212" )
            
        
        
        
   

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
        self.subscriber = self.memory.subscriber("FaceDetected")
        self.subscriber.signal.connect(self.on_human_tracked)
        self.touch = self.memory_service.subscriber("TouchChanged")
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))
                                                                 # Get the services ALTextToSpeech and ALFaceDetection.
        self.tts = session.service("ALTextToSpeech")
        self.face_detection = session.service("ALFaceDetection")
        self.face_detection.subscribe("attendancetaker")
        self.got_face = False

    
   
    
    def on_human_tracked (self, value):
        """
        Callback for event FaceDetected.
        """
        
        if value == []:                                          # empty value when the face disappears
            self.got_face = False
        elif not self.got_face:                                  # only speak the first time a face appears
            self.got_face = True
            print "I saw a face!"
            #self.tts.say ("Hello student  " )

         # Second Field = array of face_Info's.
            faceInfoArray = value[1]
            for j in range( len(faceInfoArray)-1 ):
                faceInfo = faceInfoArray[j]
                #print(faceInfo)
                x = faceInfo[1]
                    


                
                #if x[i]:
                print x[2]
                y = x[2]
                if len(y) <= 1:
                   self.tts.say ("I can not recognize you")               # Says when it fails to recognize the face
                else:
                    self.tts.say("Welcome to the class  \\pau=100\\")
                    self.tts.say (str(y))
                    now = datetime.now()
                    print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month,now.day,now.year,now.hour, now.minute, now.second)
        
                    f= open("data1.txt","a")                              # creates a text file to save all information
                   #f.write ("Current date and time : \n")
                    f.write (y)
                    f.write (",   ")
                    f.write (now.strftime("%Y-%m-%d %H:%M:%S"))
                    f.write (",  ")
                    f.write ("CSC121")
                    f.write ("\n")
                    f.close()
                
                return y

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
                                                                    #stop running the program, when interrupted by user.
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
