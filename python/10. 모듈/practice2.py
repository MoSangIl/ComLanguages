# 패키지 -> 모듈을 묶어 놓음
## travel 패키지 사용

# 바로 import 시에 파일만 가능 
## 클래스, 메소드는 import 할 수 없다.
import travel.thailand

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# from import 시에는 클래스, 메소드 import 할 수 있다.

from travel.thailand import ThailandPackage
trip_to1 = ThailandPackage()
trip_to1.detail()

from travel import vietnam

trip_to2 = vietnam.VietnamPackage()
trip_to2.detail()