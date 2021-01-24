import requests
from bs4 import BeautifulSoup

url = 'https://fred.stlouisfed.org/series/BAMLH0A0HYM2'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

find = soup.find('a', attrs={'id':'export-png'})
print(find)