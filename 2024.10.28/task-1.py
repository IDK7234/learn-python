import requests  # импорт библиотеки requests

url = 'https://date.nager.at/PublicHoliday/Country/RU/2024/CSV' # создал и инициировал переменную url
payload = {
    'Date': '',
    'LocalName': '',
    'Name': ''
}

res = requests.get(url, params=payload)
data = res.text

print(data)

