dateandtime = input("Please enter date and time in this format  ex:(04/11/2020 02:06AM) : \n")   # asks user to input the date and time in 04/11/2020 02:06AM format
courseID = input("Please enter courseID ex:(csc212):  \n")       # asks user to input name of the class
with open('test2.txt','w+') as f:          # opens a text file. If it does'nt exists, it will create one


	f.write(dateandtime )
	f.write(courseID )            #save the information in the text file.
	
