# pip install --upgrade beautifulsoup4 업그레이드

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())