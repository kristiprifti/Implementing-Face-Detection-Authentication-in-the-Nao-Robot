import requests
from bs4 import BeautifulSoup
import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep
import datetime
import time
import sys

print (sys.executable)

now = datetime.datetime.now()
os.system('py -2 testpic4.py')

with open ('test2.txt' , 'r') as f:
	size_to_read =18
	
	time_enrty = f.read(size_to_read)
	print(time_enrty)
	courseid = f.readline()
	print(courseid)
timenow4 = (now.strftime("%m/%d/%Y %I:%M%p"))
#time_entry =  input("Enter this room start time :")
datetime2 = now.strptime(timenow4, '%m/%d/%Y %I:%M%p')
datetime1 = now.strptime(time_enrty, '%m/%d/%Y %I:%M%p')

print(datetime2)
print(datetime1)

#calculate the difference
timediff = datetime2 - datetime1

#convert to seconds
seconds = timediff.total_seconds()

print(seconds)

n = seconds 

def convert(seconds): 
    return time.strftime("%H-hours %M-minutes and %S-seconds", time.gmtime(n)) 
      
#print(convert(n)) 

if ((datetime2 <= datetime1) or (seconds <= 120)):
    latev = ''
    print("You are on time")
	#lateornot= "OnTime"
else:
    latev = 'on'
    print("You are late by " + convert(n)) 
	#lateornot = ("Late by " + convert(n))
#print(lateornot)

"""

#date_string = "10/04/2020 01:30AM"
data_string1 = imput("Enter class time in form (10/04/2020 01:30AM)")
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%m/%d/%Y %I:%M%p")
print("date_object =", date_object)
"""





def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded


def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im):
    """
    will find all of the faces in a given image and label
    them if it knows what they are


    """
    """
    coruse4 = input("Course id ?")
    print(coruse4)
    print(now.strftime("%H -%M -%S ))
    time_entry = input('Enter the time class starts in  H-M-S format')
    hour, minute, seconds = map(int, time_entry.split('-'))
    time1 = datetime.time(hour, minute, seconds)
    print(time1)
    """


    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
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

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Draw a box around the face
            cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)
           # f= open("data.txt","w+")
           #f.write ("Current date and time : \n")
           #f.write (now.strftime("%Y-%m-%d %H:%M:%S \n"))
           # f.write (name)
           
            print(name)
            result = name.find('(') 
            #print ("Substring '(' found at index:", result )
            #print(name[:result])
            fullname = (name[:result])
            c34 = fullname.find(' ')
            firstname = (fullname[:c34])
            #print(firstname)
            lastname =  (fullname[c34:])
            #print(lastname)

            #print("Current date : \n")
            #print(now.strftime("%m/%d/%Y \n"))
            date4 = (now.strftime("%y-%m-%d"))
            #print("Current time : \n")
            #print(now.strftime("%Hh -%Mm -%Ss \n"))
            #print(fullname)
            if(fullname == "Unknow"):
            	print("I dont know you")
            elif (not fullname):
                print("i didnt get that")
            else:
            	login_data = {
	                'Course': courseid,
	                'FirstName': firstname,
	                'LastName': lastname,
	                'Date': datetime1,
	                'Attendance': 'on',
	                'Late': latev,
	                'submitbutton': 'Submit'

                }
            if(fullname == "Unknow"):
                print("I dont know you")
            else:

                with requests.Session() as s:


	                url = "https://rbattendance.000webhostapp.com/update.php"
	                r = s.get(url)
	                soup = BeautifulSoup(r.content, 'html5lib')
	                r = s.post(url, data = login_data)
	                print(r.content)
            	
            	




    # Display the resulting image
    
    while True:

        #cv2.imshow('Video', img)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
            return face_names

            
    
print(classify_face("test.png"))