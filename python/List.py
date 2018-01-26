# 파이썬 자료구조
# 리스트 : sequence 자료구조를 이용
# sequence : 순서가 있는 데이터 구조를 의미
# 리스트[], 튜플(), 레인지, 문자열 등이 sequence 구조 사용

msg = 'Hello, World!!'

list1_list = []                              # 빈 리스트
list2_list = [1, 2, 3, 4, 5, 6]                 # 숫자
list3_list = ['a', 'b', 'c']                 # 문자
list4_list = ['a', 'b', 'c', 1, 2, 3, True]  # 혼합

print(list1_list)

# 간단한 연산
# 요소 존재 여부 파악 : in/not in 연산자
print(1 in list1_list)
print('a' in list1_list)
print(3 in list2_list)
# 길이 연산 : len()
print( len(list1_list))
print( len(list2_list))

# 연결 연산 : +
print( list2_list + list3_list)

# 반복 연산 : *
print( list2_list*2)

# 요소의 특정값 참조 : index 사용
print( msg[5], msg[8])
print( list2_list[2])
print( list3_list[2])
print( list4_list[5])
list2_list[2] = -3
print( list2_list[2])

# 주민코드에서 성별 여부 판별
jumin = [9, 2, 0, 7, 0, 5, 1, 1, 5, 8, 6, 1, 2]
if jumin[6] == 1:
    print('남성입니다')
elif jumin[6] == 2:
    print('여성입니다')
else :
    print('잘못 입력하셨습니다')

# 주민코드에서 생년월일 추출
for i in range(0, 6):
    print(jumin[i], end = '')
    # 줄바꿈 없이 출력시 종결문자를 지정
# 특정범위내 요소들을 추출할 때는 슬라이스를 사용 [i:j]
print( jumin[0:6])  # 앞자리
print( jumin[:6])   # 앞에부터 6개
print( jumin[6:])   # 뒷자리
print( jumin[:])    # 모두

print( jumin[0: 6: 2])  # 2자리씩 점프
print( jumin[::-1])     # 역순 출력

# print( jumin[100])      # 인덱스 초과 - 오류?
# print( jumin[0:100:2])  # 인덱스 초과 - 오류?

# # 리스트 관련 통계함수
print( sum(list2_list))
print( min(list2_list))
print( max(list2_list))

# 리스트가 주어지면 이것의 가운데에 있는 요소값을 출력
print(list2_list)

def centernum(list):
    if len(list)/2 == 0:
        print(list[(int)(len(list) / 2) - 1])
        print(list[len(list) / 2])
    elif len(list)/2 != 0:
        print(list[(int)(len(list) / 2)])

centernum(list2_list)

list = [1, 2, 3, 4, 5]
list.append(9)
list.append(8)
print(list)

# 요소추가 : insert(위치, 값)
list.insert(6, 7)
print(list)

# 요소 제거 :remove(값)
list.remove(9)
print(list)

# 요소 제거 : pop(), pop(위치)
list.pop(5)
print(list)
list.pop()  # 마지막 요소 제거
print(list)

# 모두 제거 : clear()
list.clear()
print(list)

# 튜플 tuple
# 리스트 자료구조와 유사하지만 한번 입력한 자료는 변경 불가
# 즉, 요소 추가 가능, 수정/삭제 불가
# 튜플은 ()을 이용함
# 튜플 생성시 단일 요소는 요소 뒤에 ,를 추가

t = [1, 2, 3]       # 리스트
t = (1, 2, 3)       # 튜플
t = (1, 'a', True)  # 튜플
t = (1)             # 숫자(연산우선순위에 의해)
t = (1,)            # 튜플(단일요소로 구성할 때는 ,를 붙여서 사용)

days = ('일', '월', '화', '수', '목', '금', '토')
print(days)     # 요일을 튜플로 정의하고 출력
print(days[3])      # 수요일 출력
print(len(days))
print(days[3:])

# days[3] = '水'   # 튜플 요소에 값 변경 - 불가!
print(days[3])

t = [1, 1, 1, 1]
print(t)
t = (1, 1, 1, 1)
print(t)
t = {1, 1, 1, 1}    # 중복 제거
print(t)

t = [1, 1, 1, 2, 3, 5, 6, 7, 8, 6, 4, 3, 2, 3, 2, 2, 2, 6, 9]
print(t)
# 집합(set)
# 저장된 데이터를 순서에 따라 관리하지 않고 중복을 허용하지 않는 (unique) 자료구조
# 집합은 {}을 이용
# 집합의 개념에 따라 합/교/차집합이 지원
t = set(t)  # 리스트를 집합(set)으로 변환 - 중복제거, 오름차순
print(t)

# 집합 정의
# 1월중 교육받은 날을 집합으로 정의
edu = {1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26}
# 집합의 기본적인 연산산
동물 = {'사자', '늑대', '토끼', '고양이', '돼지', '뱀', '너구리', '다람쥐'}
육상동물 = {'기린', '여우', '사슴'}
해상동물 = {'고래', '상어', '고등어'}
조류 = {'독수리', '참새', '비둘기'}

print(len(동물))          # 길이
print('여우' in 육상동물)
print('여우' in 조류)
#print(동물[2])           # 인덱스 연산 : 3번째 동물은?

# 합집합
print(육상동물.union(해상동물))
print(육상동물 | 해상동물)
# 교집합
새로운동물 = 육상동물|해상동물
print(새로운동물.intersection(육상동물))
print(새로운동물 & 해상동물)
# 차집합
print(새로운동물.difference(육상동물))
#print(새로운동물.해상동물)
# 대칭차집합
print(새로운동물.symmetric_difference(육상동물))
print(새로운동물^해상동물)

# 집합에서 제공하는 메서드
동물.add('인간')        # 데이터 추가
print(동물)
동물.discard('인간')    # 데이터 삭제
print(동물)
해상동물.remove('고등어')  # 데이터 제거
print(해상동물)
#print(육상동물.pop())   # 데이터 확인 후 제거
print(육상동물)
동물.clear()              # 데이터 모두 제거
print(동물)

# 패킹, 언패킹
# 패킹packing : 여러 데이터를 변수 하나에 묶어 담기
# 언패킹unpacking : 변수에 담긴 데이터를 여러 변수에 풀어 놓기

numbers = (1, 2, 3, 4, 5)       # 튜플 생성(packing)
a, b, c, d, e = numbers         # 튜플에 저장된 데이터를 언패킹
print(c)
numbers = 1, 2, 3, 4, 5         # 패킹시 () 생략 가능
# x, y, z = numbers             # 언패킹시 데이터 갯수와 변수 갯수가 일치
x, y, *z = numbers              # 언패킹시 변수 갯수 불일치할 경우 해결 방법(z에 나머지가 다들어감)
print(z)

# n, k, e, m = input().split()
a, b, c = 1, 2, 3               # 변수 초기화에 패킹, 언패킹 동시에 사용된 경우

# 연습문제 풀이
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x)
x.append(10)    # 요소 하나를 추가할 때
print(x)
x.extend([11, 12, 13])  # 요소 여러개를 추가할 때
print(x)

x.remove(11)
x.remove(12)
print(x)

x.reverse()     # 요소를 역순으로 배치
print(x)

print(x.pop())  # 빈칸으로 두면 맨 뒤가 pop인가? ㅇㅇ
print(x)

x = [10, 5, 4, 1]
print(x)
x.sort()
print(x)

x.insert(3, 7)  # 3번 자리에 7을 넣기(원래 3 이후에 있던 것들은 뒤로 한칸씩 밀림)
print(x)

print(x.count(4))    # 요소 수(4가 몇개?)
print(x.index(5))    # 요소의 위치값 출력(5가 몇 번째 위치?)

z = {1, 1, 1, 2, 2, 3, 3, 3}
print(z)    # 요소 3개
z.add(1)    # 이미 있는 요소 추가
print(z)    # 결국 그대로 3개

def myRange(start, end, hop = 1):
    retVal = start

    while retVal <= end:
        yield retVal
        retVal += hop

hap = 0
# for i in myRange(1, 5, 2): 맨 끝(5) 까지 나오게 하고싶다 왜냐면
for i in range(1, 5, 2):    # i : 1, 3 이렇게 나오니까
                            # 결국 list 형태의 값이 출력되는 것
# for i in [1, 3] :      # 사실 이것과 같음(1 + 3)
    hap += i
print(hap)

def myRange2(start, end, hop = 1):
    retVal = start

    while retVal <= end:
        # return retVal     # 중간 계산결과를 출력 또는 처리
        yield retVal      # 실행중에 계산된 값은 generator 타입에 저장
        print(retVal)
        retVal += hop

myRange2(1, 5, 2)
a = myRange2(1, 5, 2)       # yield로 넘긴 데이터는 순환형식의 generator 타입 생성
print(a)
print(next(a))      # generator 타입에 저장된 값은 iterator형식으로 다룰 수 있음
                    # iterator는 리스트에 저장된 객체를 순환하며 하나씩 꺼내 사용하는 자료구조
print(next(a))
print(next(a))

for i in a:
    print(i)