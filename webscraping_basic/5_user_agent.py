import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = 'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101'
res = requests.get(url, headers=headers)
res.raise_for_status()
with open('navernews.html', 'w', encoding='utf-8') as f:
    f.write(res.text)