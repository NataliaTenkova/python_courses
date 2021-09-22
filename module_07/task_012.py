import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from datetime import datetime, date, time

page = requests.get('http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')

table_cur = soup.find('table', {'class':'mfd-table mfd-currency-table'})
td = table_cur.find_all('td')

data_list = []
value_list = []

index = 1
for t in td:
	t = str(t)
	if index % 3 == 1 :
		t = t.replace('</td>', '')
		t = t.replace('<td>с ', '')
		data_list.append(datetime.strptime(t, "%d.%m.%Y"))

	if index % 3 == 2 :
		t = t.replace('</td>', '')
		t = t.replace('<td>', '')
		value_list.append(float(t))
	index += 1

plt.plot(data_list, value_list)
plt.show()