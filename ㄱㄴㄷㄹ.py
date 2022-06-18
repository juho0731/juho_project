class IntegerTohangul:
    def __init__(self, int_num=0):
        self.int_num = int_num

    def __str__(self):
        num = ""
        for hnum in str(self.int_num):
            if hnum == "0":
                num += "영"
            elif hnum == "1":
                num += "일"
            elif hnum == "2":
                num += "이"
            elif hnum == "3":
                num += "삼"
            elif hnum == "4":
                num += "사"
            elif hnum == "5":
                num += "오"
            elif hnum == "6":
                num += "육"
            elif hnum == "7":
                num += "칠"
            elif hnum == "8":
                num += "팔"
            elif hnum == "9":
                num += "구"
        return str(num)

normal_num = IntegerTohangul(12345)
kor_num = str(normal_num)
print(kor_num)

