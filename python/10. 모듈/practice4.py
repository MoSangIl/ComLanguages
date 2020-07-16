# 패키지, 모듈 위치 확인

import inspect
import random
from travel import *
print(inspect.getfile(random))
# -> lib 디렉토리에 모듈을 넣고 사용할 수 있다.
print(inspect.getfile(thailand))