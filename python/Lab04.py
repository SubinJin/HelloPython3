# 30 ~ 41

# 30
print("# 30")
def five():
    number = 100
    sum = 0
    while number < 1000:
      if number % 5 == 0:
          sum = sum + number
          number = number + 1
      else:
          number = number + 1
    print(number, sum)
#five()
# 34
print("# 34")
def ftoc():
    f = float(input('화씨온도를 입력하세요'))
    c= (100/180)*(f-32)
    print("화씨", f, "도는 섭씨", c, "도 입니다")
# ftoc()
# 35
print("# 35")
def change():
    change = int(input("거스름돈을 입력하세요"))
    if (change / 50000) != 0:
        print("5만원권", (change/50000), "장")
    change = change % 50000
    # elif(change / 10000) != 0:
    #     print("1만원권", (change / 10000), "장")