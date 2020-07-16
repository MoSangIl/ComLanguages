## theater_price  모듈 사용하기

## 일반적 모듈 삽입
import theater_price

theater_price.price(3)
theater_price.price_morning(4)
theater_price.price_soldier(5)

## 모듈 네이밍 사용(Alias)
import theater_price as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

## 모듈이름 필요 없이 메소드 사용
from theater_price import price 
price(3)
# price_morning(3) # price만 불러왔기 때문에 오류

from theater_price import price_soldier as price
# 군 할인 가격을 price로 네이밍하여 사용 가능
price(5)
from theater_price import *

price(3)
price_morning(4)
price_soldier(5)
