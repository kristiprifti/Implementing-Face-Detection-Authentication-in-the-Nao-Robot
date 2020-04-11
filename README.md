# Implementing The Face Detection Authentication in the Nao Robot

Kristi Prifti

Krutarth G. Patel

Hue Do

Hao Loi (Faculty Sponsor)

Department of Computer Science, Quinsigamond Community College

# Implementing The Face Detection Authentication in the NAO Robot

The NAO Robot a wide range of applications to automate many of our daily tasks. The NAO robot has a built-in camera that can be used to recognize faces. Our project is to use NAO robot to take the attendance for our classes. First, we will train NAO to learn the faces of the students and save it in its memory. After the training, we will build a Blackboard interface to take attendance using the NAO robot. This work will be based on the Python programming language and Choregraphe software. Our application has the potential beyond the classroom. Eventually, it could be programmed to use for check-in and check-out in hospitals, hotels, airports, work, etc.

# Weekly Progress Report

# Week 1 of 01/19/20:

We are starting our project by doing research for different programs and documentation.

KRUTARTH:

• Performed some research and found some code that could be useful in making NAO to take pictures.

KRISTI:

•	Pictures can be captured by using Choregraphe as well. Here, we found that images from the code are better than the one from Choregraphe.

•	The algorithm, that is used here to take pictures from NAO robot is TakePicUsingNao.py

PLAN FOR NEXT WEEK:

Will function NAO robot to learn faces.

# Week 2 of 01/26/20:

KRISTI:

• Using face_rec.py to recognize the person in the picture taken by NAO robot

• Storing the data from face_rec.py to a .txt file ( Persons name and date and time of pic taken )

KRUTARTH:

• NAO robot can recognize different faces using the "learn face" module in Choregraphe.

PLAN FOR NEXT WEEK:

We want NAO to print the names as an output after recognizing the face. 

# Week 3 of 02/02/20:

KRISTI & KRUTARTH:

• Learn how to use the face_recognition libary in python. File face_rec.py uses mulitiple pyhton libarys do perform facial recogntition.

• Learning Python online.

• Reaseaching some better ways to do real-time face recognition.

PLAN FOR NEXT WEEK:

To learn Python programming language.

# Week 4 of 02/09/20:

KRUTARTH:

• Learning Python File Handling: Create, Open, Append, Read, Write

• Researching ways to do facial recognition using Amazon Rekognition and PyQt4

KRISTI:

• Experimenting with ways to make face recognition faster and more accurate.

PLAN FOR NEXT WEEK:

HUE:

• Creating a website that can store and display the data from .txt file generated by NAO after running the program.

# Week 5 of 02/16/20:

HUE:

• Creating a website using 000webhost

• Using  PHPMyAdmin to manage the database of the webpage.

KRISTI:

• Made some changes to code that can generate the .txt file in more organized way. Now, this .txt file will also display the course name and date.

KRUTARTH:

• Working on the program which take picture by NAO's built-in camera and compare that picture with other picture existing in the machine. If it finds any match then it outputs the result.

PLAN FOR NEXT WEEK:

• Editing and making small chqanges to the website to make a table of all students, class and attendence and input the required data.
 
# Week 6 of 02/23/20:

HUE:

Edited the webpage to have a input boxes to take Course Name, First Name, Last Name, date from user. The website can show the attendance report of all the students

KRISTI & KRUTARTH:

• The program of face recognitation by using pictures can generate a .txt file with all information of the face in picture with date and time.

• Using Amazon libraries for facial recognition and to make our programs better

PLAN FOR NEXT WEEK:

• Adding the option to take data from a .txt file and display it on the attendance report 

# Week 7 of 03/01/20:

HUE:

• Added the option to take data from a .txt file and display it on the attendance report.

KRISTI & KRUTARTH:

• We found that the Amazon libraries for face recognition will not be useful for our project ofcfacial recognition.

• Started learning how PyQt4 works with python programming.

PLAN FOR NEXT WEEK:

• Planning to make the program of face recognition using pictures more efficient and better.


# Week 8 of 03/08/20

HUE:

• Using requests and beautifulsoup4 python libraries to post data to the website directly from python

KRISTI:

• Creating a program that posts the data of attendence directly to website's database.

KRUTARTH:

• Testing all programs working proprly for all kinds of faces. 
• We found that the program of face recognition using pictures is more efficient that the one using Cheorographe tools.

PLAN FOR NEXT WEEK:

• Planning to add a time option to the website. 

• Automating the python scripts to run continually  ( Take a pic ==>  recognize  student ==>  post data to the website ) 

# Week 9 of 03/15/20:

  Spring Break.

# Week 10 of 03/22/20:

  Spring Break.

# Week 11 of 03/29/20:

REPORT FROM ALL GROUP MEMBERS:

• The website is taking the data from the .txt file created by NAO.

• It sorts the information fromthe file and displays all names of students present in the class, with the class name and date.

PLAN FOR NEXT WEEK:

• Creating program that can directly uploads the data to the webpage after running the program of face recognition.

# Week 12 of 04/05/20:

KRISTI & KRUTARTH:

• Using file testrequets.py to do the data posting to the website 

• Another way of doing data posting is by using mechanize pyhton libary  (mechanize.py)

REPORT FROM ALL GROUP MEMBERS:

• Created the program that asks the user to input the date and starting time of class. 

• Now, we don't need to upload the .txt file manually. This program does it automatically.

• This program also outputs the students who came late in class.

PLAN FOR NEXT WEEK:

• We will start writing the Documentation and Research Paper of our project.

# Week 13 of 04/12/20:


# Week 14 of 04/19/20:


# Week 15 of 04/26/20:


# Week 16 of 05/03/20:

