import datetime     # 날짜, 시간 다루는 패키지

class SungJuk:
    # 생성자
    def __init__(self, name, kor, eng, mat):
        self.sjno = 0
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = 0
        self.avg = 0.0
        self.grd = '가'
        self.regdate = str(datetime.datetime.now())

    def to_str(self):
        fmt = '[번호 : %s, 이름 : %s, 국어 : %d, 영어 : %d, 수학 : %d, 총점 : %d, 평균 : %.2f, 학점 : %s, 등록일 : %s]'
        return fmt % (self.sjno, self.name, self.kor, self.eng, self.mat, self.tot, self.avg, self.grd, self.regdate[:19])

    # 부분정보 출력 - 번호, 이름, 국어, 영어, 수학, 등록일(년월일)
    def to_str_list(self):
        fmt = '[번호 : %s, 이름 : %s, 국어 : %d, 영어 : %d, 수학 : %d, 등록일 : %s]'
        return fmt % (self.sjno, self.name, self.kor, self.eng, self.mat, self.regdate[:19])