import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as tm
tm.price(3)
tm.price_morning(4)
tm.price_soldier(10)

from theater_module import *
price(3)
price_soldier(5)
price_morning(10)

from theater_module import price, price_morning
price(5)
price_morning(7)

from theater_module import price_soldier as ps
ps(5)