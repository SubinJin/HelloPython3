# 파이썬 자료구조
# 리스트 : sequence 자료구조를 이용
# sequence : 순서가 있는 데이터 구조를 의미
# 리스트, 튜플, 레인지, 문자열 등이 sequence 구조 사용

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