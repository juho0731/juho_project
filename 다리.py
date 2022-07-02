class HangulStudy:
    def __init__(self, hangul_num="영",  int_num=0):
        self.int_num = int_num
        self.hangul_num = hangul_num


    def __int__(self):
        num = ""
        for hnum in self.hangul_num:
            if hnum == "영":
                num += "0"
            elif hnum == "일" or hnum == "이백":
                num += "1"
            elif hnum == "이" or hnum == "이십" or hnum == "이백":
                num += "2"
            elif hnum == "삼" or hnum == "삼십" or hnum == "삼백":
                num += "3"
            elif hnum == "사" or hnum == "사십" or hnum == "사백":
                num += "4"
            elif hnum == "오" or hnum == "오십" or hnum == "오백":
                num += "5"
            elif hnum == "육" or hnum == "육십" or hnum == "육백":
                num += "6"
            elif hnum == "칠" or hnum == "칠십" or hnum == "칠백":
                num += "7"
            elif hnum == "팔" or hnum == "팔십" or hnum == "팔백":
                num += "8"
            elif hnum == "구" or hnum == "구십" or hnum == "구백":
                num += "9"
            elif hnum == "백":
                num += "1"
            elif hnum == "십":
                num += ""

            else:
                raise ValueError(self.hangul_num + "은 정수로 변환할 수 없습니다.")
        return int(num)

    def __float__(self):
        num = map(HangulStudy, self.hangul_num.split("점"))
        num = '.'.join(list(map(lambda x: str(int(x)), num)))
        return float(num)


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


a = HangulStudy("백이십삼")

print(int(a))


a = HangulStudy(123)
kor_num = str(a)
print(kor_num)