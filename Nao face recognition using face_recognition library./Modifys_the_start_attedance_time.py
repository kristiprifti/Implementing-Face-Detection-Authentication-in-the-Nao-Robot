dateandtime = input("Please enter date and time in this format  ex:(04/11/2020 02:06AM) : \n")
courseID = input("Please enter courseID ex:(csc212):  \n")
with open('class_starts_time.txt','w+') as f:


	f.write(dateandtime )
	f.write(courseID )
	
	
"""
This program wirtes a .text file with the date and time class starts and the course id 




There is 5-minute tolerance. Considering My program takes 1 minute for 50 test cases 
"""