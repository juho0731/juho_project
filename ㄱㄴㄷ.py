class HangulNumber:
    def __init__(self, hangul_num="영"):
        self.hangul_num = hangul_num
    def __int__(self):
        num = ""
        for hnum in self.hangul_num:
            if hnum == "영":
                num += "0"
            elif hnum == "일":
                num += "1"
            elif hnum == "이":
                num += "2"
            elif hnum == "삼":
                num += "3"
            elif hnum == "사":
                num += "4"
            elif hnum == "오":
                num += "5"
            elif hnum == "육":
                num += "6"
            elif hnum == "칠":
                num += "7"
            elif hnum == "팔":
                num += "8"
            elif hnum == "구":
                num += "9"
            else:
                raise ValueError(self.hangul_num + "은 정수로 변환할 수 없습니다.")
        return int(num)

    def __float__(self):
        num = map(HangulNumber, self.hangul_num.split("점"))
        num = '.'.join(list(map(lambda x: str(int(x)), num)))
        return float(num)
kor_num = HangulNumber("칠팔구사오육일이삼영")
normal_num = float(kor_num)
print(normal_num)
