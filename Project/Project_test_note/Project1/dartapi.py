import requests
from bs4 import BeautifulSoup
import json
import re

key = '31718c7bf232574ee78e6f3f81c922043baad322'
corp_code = '00126380' #input('회사 코드를 입력해주세요.\n\n 삼성증권 : ') 
year = '2018' #input('원하는 연도를 입력해주세요. 2015년 이후 부터 정보를 제공합니다.')
reprt_code = '11011'#input('보고서 코드를 입력해주세요.\n\n1분기 : 11013, 반기 : 11012, 3분기 : 11014, 사업보고서 : 11011')

url = 'https://opendart.fss.or.kr/api/fnlttSinglAcnt.json?crtfc_key={}&corp_code={}&bsns_year={}&reprt_code={}'.format(key,corp_code,year,reprt_code)

res = requests.get(url)

print(res.text)
