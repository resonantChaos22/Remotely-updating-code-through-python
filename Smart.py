import requests
import os 
from bs4 import BeautifulSoup

import time


f = open('<text_file_on_local_device_to_check_the_current_version_of_update>')
f.seek(0)
j = int(f.read())
f.close()

try:
	login_data = {
        'uname': '<username_of_a_particular_machine>',
        'pwd': '<password>',
        'op': 'Login'
    }
	with requests.Session() as s:
	    url = '<site-to-check-whether-update-is-required-or-not>(Check.php)'
	    r = s.get(url)
	    time.sleep(2)
	    soup = BeautifulSoup(r.text, 'lxml')
	    time.sleep(2)
	    r = s.post(url, data=login_data)

	#print stuff
	soup=BeautifulSoup(r.text)
	h1_tag=soup.select('p')
	time.sleep(5)
	i = int(h1_tag[0].string[0])
	print(i)

	if i>j:                       #To check if there is a new update
		try:
			r2 = requests.get('<site-with-the-new-code-written>')
			#print(r2.content.decode('utf-8'))
			open('P{}.py'.format(i), 'w+').write(r2.content.decode('utf-8'))#to create the python file
			j = i
		except:
			#code to send email to notify about problem with Text.txt
			print('Error1')
			pass

except:
	#Email sent probably something wrong with Check.html or Text.txt
	print('Error2')
	pass
try:
	os.system('python P{}.py'.format(j))

	f = open('<text_file_on_local_device_to_check_the_current_version_of_update>', 'w')
	f.write('{}'.format(j))
	f.close()
	if j>1:
		os.system('rm P{}.py'.format(j-2))#Dont input any code after this, that may lead to those code not being executed

except:
	os.system('python P{}.py'.format(j-1))
	print('Error3')
	#send email that new update has error