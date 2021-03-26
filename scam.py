import requests
import os
import random
import string
import json

url = 'https://hwacloginpage.weebly.com/ajax/apps/formSubmitAjax.php'

names = json.loads(open('names.json').read())
random.seed = (os.urandom(1024))
letters = string.ascii_lowercase
chars = string.ascii_letters +string.digits +"!.*"


while(True):
	for name in names:
		name_extra = ''.join(random.choice(string.digits))
		text_extra =''.join(random.choice(letters) for i in range(4))
		password = ''.join(random.choice(chars) for i in range(8))
		email = name[:2].lower() + name_extra + '@hw.ac.uk'

		requests.post(url, allow_redirects=False, data=
		{

            "_u866263841293040574": email,
            "_u895875494222807507": password

		})
		print ('Pushing email to site: %s ' % (email))
		
		
