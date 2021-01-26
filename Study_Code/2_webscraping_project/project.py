import requests
from bs4 import BeautifulSoup
import re

def create_soup(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def print_news(idx, title, link):
    print('{}. {}'.format(idx + 1, title))
    print('  (링크 : {})'.format(link))
    print()

def scrape_weather():
    print('[오늘의 날씨]')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%B2%9C+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=U%2FkLhlp0Jy0ssF%2BSTuZssssssi8-487453'
    soup = create_soup(url)
    # 흐림, 어제보다 00 높아요
    cast = soup.find('p', attrs ={'class':'cast_txt'}).get_text()
    # 현재 00 (최저00 / 최고00)
    curr_tem = soup.find('p', attrs = {'class':'info_temperature'}).get_text().replace('도씨', '')
    min_tem = soup.find('span', attrs = {'class':'min'}).get_text() # 최저온도
    max_tem = soup.find('span', attrs = {'class':'max'}).get_text() # 최고온도
    # 오전 오후 강수확률
    morning_rain_rate = soup.find('span', attrs ={'class':'point_time morning'}).get_text().strip() # 오전 강수 확률
    afternoon_rain_rate = soup.find('span', attrs ={'class':'point_time afternoon'}).get_text().strip()

    # 미세먼지 정보
    dust = soup.find('dl', attrs ={'class':'indicator'})
    # dust = soup.find('dl', attrs ={'class':'indicator', 'id':'iddd'} 딕셔너리 형태, text = ['미세먼지', '초미세먼지])
    pm10 = dust.find_all('dd')[0].get_text() # 미세먼지
    pm25 = dust.find_all('dd')[1].get_text() # 초미세먼지
    # 출력
    print(cast)
    print('현재 {} (최저 {} / 최고 {})'.format(curr_tem, min_tem, max_tem))
    print('오전 {} / 오후 {}'.format(morning_rain_rate, afternoon_rain_rate))
    print()
    print('미세먼지 {}'.format(pm10))
    print('초미세먼지 {}'.format(pm25))


def scrape_headline_news():
    print()
    print('[헤드라인 뉴스]')
    url = 'https://news.naver.com'
    soup = create_soup(url)
    news_list = soup.find('ul', attrs = {'class':'hdline_article_list'}).find_all('li', limit = 5)
    for idx, news in enumerate(news_list):
        title = news.find('a').get_text().strip()
        link = url + news.find('a')['href']
        print_news(idx, title, link)


def scrape_it_news():
    print('[IT 뉴스]')
    url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'
    soup = create_soup(url)
    news_list = soup.find('ul', attrs = {'class':'type06_headline'}).find_all('li', limit = 5)
    for idx, news in enumerate(news_list):
        a_idx = 0
        img = news.find('img')
        if img:
            a_idx = 1 # img 태그가 있으면 [1]번째 img 태그의 정보를 사용

        a_tag = news.find_all('a')[a_idx]

        title = a_tag.get_text().strip()
        link = a_tag['href']
        print_news(idx, title, link)

def scrape_eng():
    print('[오늘의 영어 회화]')
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'
    soup = create_soup(url)
    sentences = soup.find_all('div', attrs = {'id':re.compile('^conv_kor_t')})
    print('(영어 지문)')
    for sentence in sentences[len(sentences)//2:]: # 8 문장이 있다고 가정할 때, 5~8 까지 잘라서 가져옴 index 기준 4~7 까지
        print(sentence.get_text().strip())
    
    print()
    print('(한글 지문)')
    for sentence in sentences[:len(sentences)//2]: # 8 문장이 있다고 가정할 때, 1~4 까지 잘라서 가져옴 index 기준 0~3 까지
        print(sentence.get_text().strip())    


if __name__ == '__main__':
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스
    scrape_it_news() # it뉴스 가져오기
    scrape_eng() # 오늘의 영어 회화 가져오기