import requests
import time
from datetime import datetime
from threading import Thread

def get_html(link):
	res = requests.get(link)
	return res.text

urls = ['https://yandex.ru/', 'https://yandex.ru/images/', 'https://auto.ru/', 'https://yandex.ru/pogoda/', 'https://www.python.org/']
threads = [Thread(target = get_html, args=(n, )) for n in urls]

t1 = datetime.now()
for n in urls:
	get_html(n)

print('time 1: ', (datetime.now() - t1).seconds)

t1 = datetime.now()
for t in threads:
	t.start()

for t in threads:
	t.join()

print('time 2: ', (datetime.now() - t1).seconds)