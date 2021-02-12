import requests
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# with open('quiz.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())

data_rows = soup.find('table', attrs = {'class':'tbl'}).find('tbody').find_all('tr')
for idx, row in enumerate(data_rows):
    columns = row.find_all('td')

    print('='*10, f'매물 {idx + 1}','='*10)
    print('거래 : ', columns[0].get_text().strip())
    print('면적 : ', columns[1].get_text().strip(), "(공급/전용)")
    print('가격 : ', columns[2].get_text().strip(), '(만원)')
    print('동 : ', columns[3].get_text().strip())
    print('층 : ', columns[4].get_text().strip())