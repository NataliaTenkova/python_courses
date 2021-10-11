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
    cols = row.find_all('td')
    if len(cols) > 0:
        data_list.append(datetime.strptime(cols[0].text[2:], "%d.%m.%Y"))
        value_list.append(float(cols[1].text))

plt.plot(data_list, value_list)
plt.show()