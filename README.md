# Implementing The Face Detection Authentication in the Nao Robot

Kristi Prifti

Krutarth G. Patel

Hue Do

Hao Loi (Faculty Sponsor)

Department of Computer Science, Quinsigamond Community College

# Implementing The Face Detection Authentication in the NAO Robot

The NAO robot has a wide range of applications to automate many of our daily tasks. These robots for many different purposes. Shortly, they will become an essential education element. The NAO robot has a built-in camera that can be used to recognize faces. Our project is to use the NAO robot to take the attendance of students of any class using the NAO robot. This project will have two different methods including several steps. First, we will make the NAO robot learn different faces. These faces will be saved in its memory. Using python script, we will create programs that will compare the faces from the memory with the faces of the students present in the class. This can be done also by using Choregraphe software. The second method is to compare pictures to recognize faces. The NAO robot will capture a picture of a person and compare it with the pictures existing in our machine. After training NAO, a webpage will be build based on the Blackboard interface. The main purpose of this webpage is to keep the attendance report of all students. These two different methods will take attendance and will store the data on one common webpage. This project will be based on the Python programming language and Choregraphe software. The application of this project will have potential beyond the classroom. Eventually, it could be programmed to use in hotels, hospitals, airports, at work, etc.

# Weekly Progress Report

# Week 1 of 01/19/20:

• Krutarth and I developed the main idea for implementing face recognition in the NAO robot. We started doing some research on Softbank robotics.

• We signed off the robot from college and started performing the basic steps on it.

PLAN FOR NEXT WEEK:

• To write the abstract of our project.

# Week 2 of 01/26/20:

We are starting our project by researching different algorithms and documentation from Softbank Robotics and Aldebaran documentation.

Report from Krutarth:

• Started Learning Python programming language.

• I am performing some research on how to do facial recognition using Choregraphe. 

Report from Kristi:

•  Pictures can be captured by using Choregraphe software as well as using a box from box libraries. I am working on doing face recognition using pictures.

PLAN FOR NEXT WEEK:

• Planning to function the NAO robot to learn many faces.

# Week 3 of 02/02/20:

Report from Kristi:

• Trying to make a program that can recognize faces by comparing pictures.

• Here, I am using face_recognition_Module.py to recognize the person in the picture taken by NAO robot. Storing the data from face_recognition_Module.py to a text file (Student's name and date and time when picture was taken).

Report from Krutarth:

• Using Choregraphe, I am making the NAO robot learn different faces. NAO robot can recognize different faces using the "learn face" box from box libraries in Choregraphe.

PLAN FOR NEXT WEEK:

• We want an output of names and time information when the NAO recognises the face of student.

# Week 4 of 02/09/20:

Report from Kristi:

• Working on algorithim of face_recognition_module.py

Report from Krutarth:

• Working on algorithim of face_recognition_Using_Choregraphe.py

Report From KRISTI & KRUTARTH:

• Learn how to use the face_recognition libary in python. File face_rec.py uses mulitiple pyhton libarys do perform facial recogntition.

• Researching some better ways to do real-time face recognition.

PLAN FOR NEXT WEEK:

• To learn Python programming language, mostly how to open and close text files, how to modify them and save them with the output of programs

# Week 5 of 02/16/20:

Report from KRUTARTH & KRISTI:

• Learning Python File Handling: Create, Open, Append, Read, Write

• Researching ways to do facial recognition using Amazon Rekognition and PyQt4

• Experimenting with ways to make face recognition faster and more accurate.

• Working on modifying both algorithms.

PLAN FOR NEXT WEEK:

Plan of Hue:

• Planning to start working on creating a website. In this webpage, one will able to upload text files, and also can take class attendance through that webpage. All the data will be stored and can be reviewed after.

• For this task I will use Webhost app.

# Week 6 of 02/23/20::

Report from Hue:

• Creating a website using 000webhost. The phpMyAdmin in MySQL is used to create the database.

• Working on HTML and PHP files.

Report from Kristi:

• Modifying the face_recognition_module.py. Now it can generate the text file in a more organized way. All information of any person with date and time will be stored in this text file by this algorithm.

Report from Krutarth:

• Working on the algorithm of face_recognition_Using_Choregraphe.py. 

• NAO robot has learned the face using Choregraphe. This algorithm takes the face information from NAO's memory. If the student's face matches then it outputs the result through a text file.

PLAN FOR NEXT WEEK:

• Editing and making small changes to the website. Planning to make a table of names of students, class names, date and time, and attendance.
 
# Week 7 of 03/01/20:

Report from Hue:

• Working on Index.html.

• Modified the webpage algorithm. Now, it includes a table so that the course name, student's name, date, and time in an organized manner. The website can show the attendance report of all the students for any date.

KRISTI & KRUTARTH:

• Started creating an algorithm, named as modify_the_start_attendence-time.py.

• The program of face_recognition_module.py and face_recognition_Using_Choregraphe.py can generate a text file with all information of the face in the picture with date and time.

• Trying to use Amazon libraries for facial recognition and to make our programs better and less time-consuming.

PLAN FOR NEXT WEEK:

• Planning to learn and use Amazon libraries. 
• Planning to make our algorithms less time-consuming. 

# Week 8 of 03/08/20

KRISTI & KRUTARTH:

• We worked on Amazon libraries for face recognition. We conclude that they are not be beneficial for our project.

• We finished implemantation of the algorithm of face_recognition_module.py and face_recognition_Using_Choregraphe.py

PLAN FOR NEXT WEEK:

• Planning to make the program of face recognition using pictures more efficient and better. 

# Week 9 of 03/15/20:

Spring Break.

# Week 10 of 03/22/20:

Spring Break.

# Week 11 of 03/29/20:

Report from Hue:

• Using requests and beautifulsoup4 python libraries to post data to the website directly from python programs.

• Finished with working on Update.PHP and Report.PHP.

Report from Kristi:

• Completed the algorithm of modify_the_start_attendence_time.py. With the help of this program, the user can input the date, time, and course information if they do not want to use real-time.

• Creating an algorithm that posts the data of attendance directly to the website's database after we run it.

Report from Krutarth:

• Testing the face_recognition_Using_Choregraphe.py by adding diferent faces. It is working properly for all faces stored in the memory of the NAO. 

• We conclude that the program of face recognition using pictures is more efficient than the one using Cheorographe tools.

PLAN FOR NEXT WEEK:

• Planning to automate all the python scripts to run continuously. (Take a pic ==>  recognize  student ==>  post data to the website)

# Week 12 of 04/05/20:

Report from Krutarth:

• Created an algorithm named: Uses_NAO_Camera_To_take_Pic.py. This program takes a picture by using NAO's built-in camera and saves it in our machine. We do not need to use Choregraphe for capturing pictures anymore.

• Automated the Facerecognition_using_chregraphe.py. It can take multiple faces while running and only stops when user wants to.

Report from Kristi:

• Created a function in the file named as Starts_attendence_with_back_click_of_head.py, that detects the touch on NAO's head with the help of touch sensors. When it detects the touch, the program starts running and takes attendance. When touched again, it stops running and outputs the report.

Report from Hue:

• Finished the implemation of MySQL database.

• Webpage sorts the information from the file and displays all names of students present in the class, with the class name and date.

PLAN FOR NEXT WEEK:

• Creating a program that can directly upload the data to the webpage automatically, after running the program of face recognition.

# Week 13 of 04/12/20:

REPORT FROM KRISTI & KRUTARTH:

• Automated all the pythons code and modified the python scripts. Now, we don't need to upload the text file manually. When we run the program, the text file is uploaded on the webpage when it completes compiling.

• Take a pic ==>  recognize  student ==>  post data to the website, and runs again automatically.

• This program also outputs the students who came late in class. Website shows these late comers.

PLAN FOR NEXT WEEK:

• We will start writing the Documentation and Research Paper of our project.

# Week 14 of 04/19/20:

REPORT FROM ALL GROUP MEMBERS:

• We completed and implemented all our python programs. 

• Performed a virtual meeting and took decisions on writing Documentation and Research paper of our project.

• Also performed tests on all programs and make sure they are working as expected and without generating any bugs and errors.

PLAN FOR NEXT WEEK:

• Planning to add test cases to our codes and count hits amd misses.

# Week 15 of 04/26/20:

Report from Krutarth:

• Started writing the Research paper of our project and modifying GitHub weekely reports.

• Testing the code of face_recognition_Using_Choregraphe.py by adding different test cases to it.

Report from Kristi:

• Started learning Doxygen online. I will use Doxygen to write Documentation of our project.

• Performing tests with different pictures to face_recognition_module.py.

Report from Hue:

• Adding comments and testing all my HTML and PHP files. Started writing the research paper for my part of project

PLAN FOR NEXT WEEK:

• Planning to do a virtual meeting and present the projects and testing all programs with test cases. 

# Week 16 of 05/03/20

REPORT FROM ALL GROUP MEMBERS:

• All the programs are running fine without generating any bugs or errors. NAO is learning faces through Choregraphe, and stores in its memory. NAO is taking pictures and saves them in our machine.

• When the program is running, NAO takes pictures and compares it with the pictures saved in the machine. If they matched, the information of students with class names and time is saved in a text file. 

• This text file is sent to the webpage's database and the attendance report is shown on that webpage. This report can be accessed anytime after.

• We completed Research Paper and Documentation of our project.

Worked Completed by KRISTI:

• Completed and organized the Face_Recognition_Module.py and Starts_Attendence_with_back_click_of_NAO.py

• Performed the face recognition by comparing pictures taken from NAO's built-in camera with the pictures stored on the machine.

Worked Completed by KRUTARTH:

• Completed and organized the Face_Recognition_Using_Choregraphe.py and Uses_Nao_Camera_To_Take_pic.py

• Performed face recognition by using the faces from the memory of the NAO robot.

Worked Completed by HUE:

• Designed and worked on the webpage that keeps the records of all attendance taken.

• Created a table which includes the basic attendance information of students.

