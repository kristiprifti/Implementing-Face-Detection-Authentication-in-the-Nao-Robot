import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep
import datetime
import time
import sys
import subprocess 
import requests
from bs4 import BeautifulSoup

"""
I use subprocess to call (py -2 Uses_Nao_Camera_To_Take_Pic.py) and I direct the standard out to subprocess.PIPE
Import would be ideal but Uses_Nao_Camera_To_Take_Pic.py  works only on python 2.7 and the some of the python libraries only work
on python 2.7 
"""
subprocess.run('py -2 Uses_Nao_Camera_To_Take_Pic.py' , stdout = subprocess.PIPE)
now = datetime.datetime.now() # Sets now to the currnet date and time
"""
I open the text file created by Modifys_the_start_attedance_time.py and read courseid and date

"""
with open ('class_starts_time.txt' , 'r') as f:
	size_to_read =18
	time_enrty = f.read(size_to_read)
	courseid = f.readline()
timenow4 = (now.strftime("%m/%d/%Y %I:%M%p"))

datetime2 = now.strptime(timenow4, '%m/%d/%Y %I:%M%p')
datetime1 = now.strptime(time_enrty, '%m/%d/%Y %I:%M%p')

    #calculate the difference
timediff = datetime2 - datetime1

    #convert to seconds
seconds = timediff.total_seconds()
n = seconds 

"""

"""
def convert(seconds): 
    return time.strftime("%H hours %M minutes and %S seconds", time.gmtime(n))
"""
It calculates if the student is late or not 
"""
if ((datetime2 <= datetime1) or (seconds <= 300)): #There is 5-minute tolerance
	lateornot = []
	lateornot= ("You are on time ")
	latev = ''
else:
	lateornot = ("You are late by " + convert(n))
	latev = 'on'

"""
Function  get_encoded_faces()
The function get_encoded_faces() reads through all the faces 
in the faces folder and it encodes all  faces into a format
that the machine learning model inside face_recogntion module
can use to detect the faces.

It's essential to name the faces in the faces folder what 
they are. It will utilize  those labels to name your face
if your face matches one of the faces in the faces folder


"""

def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded

"""
The function unknown_image_encoded(img) gets the image given 
and encodes that image into a format that machine learning 
module face_recognition can read and returns that encoding


"""

def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding

"""
classify_face(im) takes the name of an image and draws a box
around the face and preform the face detection and show the face
and also is going to return a list faces.

faces = get_encoded_faces() - Start by getting all the ecoded faces

faces_encoded = list(faces.values()) - Turing these face valuse into a list 

known_face_names = list(faces.keys()) - All the names this is returned as a dictionary
the face is encoded is all the values and the names of all those faces are all of the keys

img = cv2.imread(im, 1) - Read the given image 

face_locations = face_recognition.face_locations(img) - Find all the locations of the 
face in the image by passing IMG  which is read in by OpenCV
It finds all the locations for our faces.

unknown_face_encodings = face_recognition.face_encodings(img, face_locations)
- Encode unknown face  (test.jpg) 

matches = face_recognition.compare_faces(faces_encoded, face_encoding) - Compare 
all the faces that we know against the faces in the images and see if any of them are 
the same. If they are a box will be drawn and the name of the face. If they are not
a box with "Unknunk " will be written in the test.png image

"""

def classify_face(im):
    """
    will find all of the faces in a given image and label
    them if it knows what they are
    :param im: str of file path
    :return: list of face names
    """
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
    """
    Resize optinal 
    """
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

        """
        All the photo lables in the faces foler end with (number) so a simiple .find("(") command takes the () away from
        the label leaving us with the full name of the person

        """

        result = name.find('(') 
        fullname = (name[:result])
        """
        If face_recogntion module recognizes a face but that face is not in the faces module then 
        it will print unknown and we print 12345678 to use it on the start attednace program 

        """
        if (name == "Unknown"):
            print("12345678")
        else:
            """
            f'{len(face_locayion)}-people - will return the number of people in photo taken by Nao'
            """
            print (f'{len(face_locations)}-people')
            print (fullname)
            print(courseid)
            print (lateornot)
        c34 = fullname.find(' ')
        firstname = (fullname[:c34])
        lastname =  (fullname[c34:])
        """
        We get all the data courseid , fristname , lastname,  datetime1,and late or not and submited on the website 
        

        """
        login_data = {
	        'Course': courseid,
	        'FirstName': firstname,
	        'LastName': lastname,
	        'Date': datetime2,
	        'Attendance': 'on',
	        'Late': latev,
	        'submitbutton': 'Submit'
                }
        if(fullname == "Unknow"):
        	print("I-dont-know-you")
        else:
        
            with requests.Session() as s:
            	url = "https://rbattendance.000webhostapp.com/update.php"
            	r = s.get(url)
            	soup = BeautifulSoup(r.content, 'html5lib')
            	r = s.post(url, data = login_data)
            	#print(r.content)
        
            




        """
        This for loop is reponsible for drawing on the image  
        """

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Draw a box around the face
            cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)


    # Display the resulting image
    
    
    while True:
        #cv2.imshow('Video', img)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
            return face_names 



(classify_face("test.png"))

"""
Credit : Tech with tim 

"""

