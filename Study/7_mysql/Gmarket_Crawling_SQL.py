import requests
from bs4 import BeautifulSoup
import pymysql

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000', db='gmarket', charset='utf8')

cursor = db.cursor()

def save_data(item_info):
    print (item_info)
    sql = """SELECT COUNT(*) FROM items WHERE item_code = '""" + item_info['item_code'] + """';"""
    cursor.execute(sql)
    result = cursor.fetchone()
    #print (result[0])
    if result[0] == 0:
        sql = """INSERT INTO items VALUES('""" + item_info['item_code'] + """',
        '""" + item_info['title'] + """', 
        """ + str(item_info['ori_price']) + """, 
        """ + str(item_info['dis_price']) + """, 
        """ + str(item_info['discount_percent']) + """, 
        '""" + item_info['provider'] + """')"""
        #print (sql)
        cursor.execute(sql)
    
    sql = """INSERT INTO ranking (main_category, sub_category, item_ranking, item_code) VALUES('""" + item_info['category_name'] + """',
    '""" + item_info['sub_category_name'] + """', 
    '""" + str(item_info['ranking']) + """', 
    '""" + item_info['item_code'] + """')"""     
    #print (sql)    
    cursor.execute(sql)

def get_items(html, category_name, sub_category_name):
    # 일부 서브 카테고리의 경우, 이벤트 페이지와 같이 표시될 수 있으므로, 해당 케이스들은 skip 함 (2020.09.30)
    best_item = html.select('div.best-list')
    
    if len(best_item[1].select('li')) > 0:
        for index, item in enumerate(best_item[1].select('li')):
            data_dict = dict()

            ranking = index + 1
            title = item.select_one('a.itemname')
            ori_price = item.select_one('div.o-price')
            dis_price = item.select_one('div.s-price strong span')
            discount_percent = item.select_one('div.s-price em')

            if ori_price == None or ori_price.get_text() == '':
                ori_price = dis_price

            if dis_price == None:
                ori_price, dis_price = 0, 0
            else:
                ori_price = ori_price.get_text().replace(',', '').replace('원', '')
                dis_price = dis_price.get_text().replace(',', '').replace('원', '')

            if discount_percent == None or discount_percent.get_text() == '':
                discount_percent = 0
            else:
                discount_percent = discount_percent.get_text().replace('%', '')

            product_link = item.select_one('div.thumb > a')
            item_code = product_link.attrs['href'].split('=')[1]

            res = requests.get(product_link.attrs['href'])
            soup = BeautifulSoup(res.content, 'html.parser')
            provider = soup.select_one('div.item-topinfo_headline > p > span > a')
            if provider == None:
                provider = ''
            else:
                provider = provider.get_text()

            data_dict['category_name'] = category_name
            data_dict['sub_category_name'] = sub_category_name
            data_dict['ranking'] = ranking
            data_dict['title'] = title.get_text()
            data_dict['ori_price'] = ori_price
            data_dict['dis_price'] = dis_price
            data_dict['discount_percent'] = discount_percent
            data_dict['item_code'] = item_code.replace('&ver','')
            data_dict['provider'] = provider

            save_data(data_dict)

def get_category(category_link, category_name):
    print(category_link, category_name)
    res = requests.get(category_link)
    soup = BeautifulSoup(res.content, 'html.parser')

    get_items(soup, category_name, "ALL") # 메인 카테고리 아이템 가져오기

    sub_categories = soup.select('div.navi.group ul li > a')
    for sub_category in sub_categories:
        res = requests.get('http://corners.gmarket.co.kr/' + sub_category['href'])
        soup = BeautifulSoup(res.content, 'html.parser')
        print(category_name, sub_category.get_text())
        get_items(soup, category_name, sub_category.get_text()) # 서브 카테고리 아이템 가져오기



res = requests.get('http://corners.gmarket.co.kr/Bestsellers', headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.content, 'html.parser')

categories = soup.select('div.gbest-cate ul.by-group li a')
for category in categories:
    get_category('http://corners.gmarket.co.kr/' + category['href'], category.get_text())

db.commit()
db.close()        