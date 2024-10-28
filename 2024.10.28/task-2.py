import datetime
import requests, re
from datetime import date

url = 'https://date.nager.at/api/v3/NextPublicHolidays/Ru' # создал и инициировал переменную url

res = requests.get(url)
data = res.text
a = data.split('},')
today_date = datetime.datetime.now()


for i in range(3):
    print(a[i])
    a1 = re.split("\"", a[i])
    y = a1[3].split('-')
    x = datetime.datetime(int(y[0]), int(y[1]), int(y[2]))

    delta = x - today_date
    print(delta)



