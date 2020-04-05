import requests
from bs4 import BeautifulSoup


headers = {
	
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

login_data = {
	'Course': 'pythontest1',
	'FirstName': 'pythontest2',
	'LastName': 'pythontest3',
	'Date': '2020-12-21',
	'Attendance': 'on',
	'submitbutton': 'Submit'

}
with requests.Session() as s:
	url = "https://rbattendance.000webhostapp.com/insert.php"
	r = s.get(url, headers = headers)
	soup = BeautifulSoup(r.content, 'html5lib')
	r = s.post(url, data = login_data, headers = headers)
	print(r.content)
