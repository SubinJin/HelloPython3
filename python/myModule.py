# 모듈 사용하기
# 프로그램을 구성하는 독립적인 단위를 각각 정의하고 관리하는 방법
# 자주 사용하는 일반적인 기능은 모듈로 한번 만들어 두면 필요할 때마다 도입해서 활용
# 모듈 : 관련성 있는 데이터들, 함수, 클래스

# 모듈을 사용하려면 import 명령으로 인터프리터에게 사용여부를 알려야 한다
import random
import Lab03    # 우리가 만든 함수가 있는 파일
import math
print(random.randint(1, 10))

# 모듈을 호출할 때는 모듈명(파일명).함수명
# ex) Lab03.isLeapYear
print(math.pi)
print(math.sqrt(9))

# 모듈 호출시 이름을 별칭으로 바꾸어 정의
# import 모듈이름 as 별칭
import random as r
print(r.randint(1, 10))

# 함수 호출시 모듈명까지 기술하는 것은 왠지 불편
# from 모듈명 import 함수명
from math import *  # 쓰기 편하지만 비추
from math import pi 
print(pi)