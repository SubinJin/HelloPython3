# 이름 짓기
# 파스칼 표기법 : 첫 단어를 대문자로 시작하여 이름을 지음 Employees, Depart
# 카멜 표기법 : 천 단어를 소문자로 시작하여 이름을 지음 registerEmployee
# 스네이크 표기법 : 소문자와 _ 기호를 사용해서 이름을 지음 register_employee
# 헝가리언 표기법 : 자료형을 의미하는 접두사를 이용해 이름을 지음(strName, isMarried, boolMarried)

    # 함수로 재작성하기
    # Q8. 자취방 구하기
def compareRoom(width, height, price):
    return (width * height) / price

roomA = compareRoom(2.5, 3, 27)
roomB = compareRoom(4, 2, 30)

if (roomA < roomB):
    print('방 A가 낫네요')
else:
    print('방 B가 낫네요')



    # Q10.
    def computeProfit():
        s = input('불변자본을 입력하세요')
        v = input('가변자본을 입력하세요')
        c = input('잉여가치액을 입력하세요')
     # constatnt capital, variable capital, surplus value
        return (c + v) / s

        print(computeProfit())


    # Q11.
    def getExchangeRate(country):
        rate = 0
        if country == 'us':
            rate=1071
        elif country == 'euro':
            rate = 1309
        return rate

    buyUS = 780 * getExchangeRate('us')
    buyEuro = 650 * getExchangeRate('euro')

    print(buyEuro, buyUS)

    if buyUS > buyEuro:
        print('유로화로 구입하는게 더 비싸요')
    else :
        print('달러로 구입하는게 더 비싸요')


    # 12
    def howManyRun(radius):
        pi = 3.14
        return radius * pi

        studentA = howManyRun(100)
        studentB = howManyRun(90)

        print('학생A는 학생B보다 %d m만큼 더 뜀' \
             %(studentA - studentB))

    # 17 계산기 (제곱연산 추가)
    def intCalu():
        num1 = int(input('좌변값을 하나 입력하세요'))
        num2 = int(input('우변값을 하나 입력하세요'))
        fmt = "%d + %d = %d \n %d - %d = %d \n"
        fmt += "%d * %d = %d \n %d / %d = %d \n"
        fmt += "%d ** %d = %d"
        print(fmt %(num1, num2, num1+num2, \
                    num1, num2, num1-num2, \
                    num1, num2, num1*num2, \
                    num1, num2, num1/num2, \
                    num1, num2, num1**num2))

    intCalu()

    # 세금 계산 (어제꺼 보고 따라해)
    # computax 관련

    # 18, 19 ,20 복권발행행
def lotto():
    import random
    lucky = int(input('세자리 정수를 입력하세요'))
    match = 0
    lotto = random.randrange(100, 1000)
    prize = '다음 기회에'

    for i in[0, 1, 2]:
        for j in[0, 1, 2]:
            if(lucky[i] == lotto[j]):
               match += 1

    if match ==3 :
        prize = '1등 당첨! 상금 백만원'
    elif match == 2 :
        prize = '2등 당첨! 상금 십만원'
    elif match == 1 :
        prize = '3등 당첨 ! 상금 만원'

    print(lucky, lotto, prize)
lotto()





