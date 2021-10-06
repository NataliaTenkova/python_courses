import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from datetime import datetime, date, time

page = requests.get('http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')

table_cur = soup.find('table', {'class':'mfd-table mfd-currency-table'})
tr = table_cur.find_all('tr')

data_list = []
value_list = []

for row in tr:
    cols = str(row.find_all('td'))

    if cols != "[]":
	    value_list.append(float(cols[28:35]))
	    data_list.append(datetime.strptime(cols[7:17], "%d.%m.%Y"))

plt.plot(data_list, value_list)
plt.show()