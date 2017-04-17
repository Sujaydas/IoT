import requests
from time import sleep


while(1):
	r = requests.get("http://10.0.0.73/index.html")

	#print r.status_code
	#print r.headers
	print r.content
	sleep(0.02)

