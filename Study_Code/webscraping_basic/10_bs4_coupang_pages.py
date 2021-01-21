import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

for i in range(1, 6):
    #print('페이지 : ', i)
    url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor='.format(i)
    
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    items = soup.find_all('li', attrs={'class':re.compile('^search-product')})
    for item in items:
        
        #광고제품 제외
        ad = item.find('span', attrs={'class':'ad-badge-text'})
        if ad:
            #print(' < ad exception > ')
            continue
        
        #제품명
        name = item.find('div', attrs={'class':'name'}).get_text()
        #애플제품 제외
        if 'Apple' in name:
            #print(' <Apple product exception> ')
            continue
        
        #가격
        price = item.find('strong', attrs={'class':'price-value'}).get_text()
        
        #평점
        rate = item.find('em', attrs={'class':'rating'})
        if rate:
            rate = rate.get_text()
        else:
            print(' < no rate exception > ')
            continue
        
        #평점수
        rate_cnt = item.find('span', attrs={'class':'rating-total-count'})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1] # 예 (26)
        else:
            # print(' < no rate_cnt exception > ')
            continue
        
        link = item.find('a', attrs={'class':'search-product-link'})['href']

        #리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        if float(rate) >= 4.5 and int(rate_cnt) >= 100 and 300000 <= int(price.replace(',', '')) <= 1500000:
            #print(name, price, rate, rate_cnt)
            print('제품명 : {}'.format(name))
            print(f'가격 : {price}')
            print(f'평점 : {rate}점 ({rate_cnt}개)')
            print('바로가기: {}'.format('https://www.coupang.com' + link))
            print('-'*100) #줄긋기