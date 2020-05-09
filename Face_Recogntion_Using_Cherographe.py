#! /usr/bin/env python
# -*- encoding: UTF-8 -*-


import qi
import functools
import time
import sys
import argparse
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import datetime

"""
We want the robot to say name and welcome the student every time it
detects a student's face. To do this, we need to subscribe to the
HumanTracked event, raised by the ALFacedetection module, and link
it to a callback. A callback is a function that is executed every time
an event is raised. The example: run the script, and put student's face
in front of the robot : you should hear the name of student and compiler
will print the information. To begin with the algorithm, a aimple class
to get & read FaceDetected Events. The class is named as attendanceTaker,
which includes various functions like onTouched, __init___, onHumanTracked,
and run.
"""


class attendancetaker(object):                       # class begins
    """
    A simple class to react to face detection events.
    """
  
    
    """
    Function: onTouched(strVarName, value) and sss(bodies). These function
    aim to determine whether the robot is touched. on head. It is a
    Boolean behavior. So, whenever the touch is detected on NAO’s head,
    the program will start running in our machine and when touched again,
    it will stop running the program.
    """
    
    def onTouched(self, strVarName, value):     
        
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

    def sss(self, bodies):        #Will determine if the touch is from front, middle, or rear part
        if (bodies == []):
            return
        else:
            touched1 =  bodies[1]
            print(touched1)
        if (touched1 == 'Head/Touch/Front'):
            self.tts.say ("Welcome to  \\pau=100\\ CSC 212" )
            
        
        
        
    """
    Function: __init__(app). Here we are performing initialisation of qi
    framework and event detection. It access to the NAO's memory.
    If it detects the face, it calls OnHumanTracked function.
    """   

    def __init__(self, app):
        
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

    
    """
    Function: OnHumanTracked(value). When any face is detected, the Boolean present
    in the function changes to true and it calls the memory of NAO. If the robot had
    learned that face before using Choregraphe, then with the access in NAO mamory,
    It will say the name of the person and prints the information in compier or file.
    Else it will ask to detect the face again. This function also contains the algorithm
    for sending the student and time info to attendance report website.
    """
    
    def on_human_tracked (self, value):
        """
        Callback for event FaceDetected.
        """
        
        if value == []:                                          # empty value when the face disappears
            self.got_face = False
        elif not self.got_face:                                  # only speak the first time a face appears
            self.got_face = True
            print("I saw a face!")
            #self.tts.say ("Hello student  " )

         # Second Field = array of face_Info's.
            faceInfoArray = value[1]
            for j in range( len(faceInfoArray)-1 ):
                faceInfo = faceInfoArray[j]
                #print(faceInfo)
                x = faceInfo[1]
                    


                
                #if x[i]:
                print(x[2])
                y = x[2]
                if len(y) <= 1:
                   self.tts.say ("I can not recognize you")               # Says when it fails to recognize the face
                else:
                    self.tts.say("Welcome to the class  \\pau=100\\")
                    self.tts.say (str(y))
                    fullname = y
                    #now = datetime.now()
                    c34 = fullname.find(' ')
                    firstname = (fullname[:c34])
                    lastname =  (fullname[c34:])
                    #timenow4 = (now.strftime("%Y/%m/%d"))
                    #print timenow4


                    #print('%02d/%02d/%04d %02d:%02d:%02d' % (now.month,now.day,now.year,now.hour, now.minute, now.second))
        
                    f= open("data1.txt","a")                              # creates a text file to save all information
                   #f.write ("Current date and time : \n")
                    f.write (y)
                    f.write (",   ")
                   # f.write (now.strftime("%Y-%m-%d %H:%M:%S"))
                    f.write (",  ")
                    f.write ("CSC212")
                    f.write ("\n")
                    f.close()
                    login_data = {
                        'Course': 'CSC212',
                        'FirstName': firstname,
                        'LastName': lastname,
                        'Date': '2020-05-09',
                        'Attendance': 'on',
                        'Late': '',
                        'submitbutton': 'Submit'
                    }
                    
                    with requests.Session() as s:
                        url = "https://rbattendance.000webhostapp.com/update.php"
                        r = s.get(url)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        r = s.post(url, data = login_data)
                        print(r.content)
                
                return y

    """
    Function: run(), is called whenever the user runs the program. We can say this function
    is the base of our code. It prints the message when program is ran or terminatted.
    """

    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print("Starting Attendance Taker")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Interrupted by user, stopping attendance taker")
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
        print(("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help."))
        sys.exit(1)

    human_greeter = attendancetaker(app)
    human_greeter.run()
