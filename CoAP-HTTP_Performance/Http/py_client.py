import requests
from time import sleep


while(1):
	r = requests.get("http://127.0.0.1/index.html")

	#print r.status_code
	#print r.headers
	print r.content
	sleep(0.02)

