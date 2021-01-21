import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all('a', attrs={'class':'title'})
# find_all : class 속성이 title 인 모든 'a' element를 반환, find : 첫 번째로 만나는 부분을 찾음
for cartoon in cartoons:
    print(cartoon.get_text())

