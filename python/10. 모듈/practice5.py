# Beautiful Soup Excercise
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

## pip list => 설치된 모듈
## pip show 'module name' -> 모듈 정보
## pip install --upgrade 'module name' -> 모듈 업그레이드
## pip uninstall 'module name' -> 모듈 삭제