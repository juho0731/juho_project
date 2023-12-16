import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtGui import QPixmap,QFont

# 불러올 UI
form_class = uic.loadUiType("DigestiveSystem_UI2.ui")[0]

class WindowClass(QMainWindow,form_class):
    def __init__(self):
        # 부모 클래스들의 init 활성화
        super().__init__()
        # 불러온 ui form_class를 적용시킨다
        self.setupUi(self)
        self.setWindowTitle("Digetive System")
        self.loadImageFromFile()
        self.Labelinit()




    def Labelinit(self):
        # 탄, 단, 지 textLabel
        self.labelNutrients = QLabel(self)
        self.labelNutrients.setAlignment(QtCore.Qt.AlignCenter)  # 가로 정렬
        self.labelNutrients.setGeometry(50, 200, 0, 0)
        self.labelNutrients.setStyleSheet("background:#99e5e5;"
                                          "border-style: solid;"
                                          "border-width: 1px;"
                                          "border-color: black;"
                                          "border-radius: 10px;")
                                            # "backgound: transparent;" - 배경 투명하게
        self.labelNutrients.setFont(QtGui.QFont('초롱바탕', 28))

        #소화 기관 text label
        self.labelOrgan = QLabel(self)
        self.labelOrgan.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOrgan.setGeometry(730, 153, 200, 70)
        self.labelOrgan.setStyleSheet("background: white;"
                                      "border-style: solid;"
                                      "border-width: 3px;"
                                      "border-color: black;")
        self.labelOrgan.setFont(QFont('초롱바탕', 25, QFont.Bold))

        # 소화 효소 textlabel
        self.labelEnzyme = QLabel(self)
        self.labelEnzyme.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEnzyme.setGeometry(730, 303, 200, 70)
        self.labelEnzyme.setStyleSheet("background: white;"
                                      "border-style: solid;"
                                      "border-width: 3px;"
                                      "border-color: black;")
        self.labelEnzyme.setFont(QFont('초롱바탕', 23, QFont.Bold))


        # 현재 보고 있는 영양소 정보
        self.nutrient = ''
        # 영양소 변화과정 {영양소: [(효소,변화된 영양소),(),()], }
        self.nutrients = {
            '탄수화물': [('','','탄수화물'),('아밀레이스','구강', '엿당'), ('아밀레이스','소장', '엿당'), ('말테이스','소장', '포도당')],
            '단백질': [('','','단백질'),('펩신','위','폴리팹티드'), ('트립신','소장', '디펩티드'), ('펩티데이스','소장', '아미노산')],
            '지방': [('','','지방'),("쓸개즙", '소장','지방 유화'), ('라이페이스', '소장','지방산과 모노글리셀리드')]
        }

        # 영양소 별 위치 값
        self.nutrients_geometry = {
            "탄수화물": [(50, 200, 200, 60),(250,180,200,60),(150,650,200,60),(210,800,200,60)],
            "단백질": [(50, 200, 200, 60),(380,600,240,60),(150,650,200,60),(210,800,200,60)],
            "지방":  [(50, 200, 200, 60),(140,630,200,60),(140,680,340,60)]
        }

        # 버튼 별 기능 할당
        self.btn_carbs.clicked.connect(self.func_carbs)
        self.btn_protein.clicked.connect(self.func_protein)
        self.btn_fat.clicked.connect(self.func_fat)

        self.btn_prev.clicked.connect(self.func_prev)
        self.btn_next.clicked.connect(self.func_next)


    # 메인 이미지 불러오기
    def loadImageFromFile(self):
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("digestive_organ.png")
        self.qPixmapVar = self.qPixmapVar.scaledToWidth(640)
        self.mainLabel.setPixmap(self.qPixmapVar)

    # 탄수화물 버튼 기능
    def func_carbs(self):
        # 영양소 위치
        self.idx = 0
        self.labelOrgan.setText("")
        self.labelEnzyme.setText("")
        self.labelNutrients.setGeometry(50, 200, 200, 60)
        self.labelNutrients.setText("탄수화물")
        self.nutrient = "탄수화물"
        self.labelNutrients.setFont(QtGui.QFont("초롱바탕", 23))


    # 단백질 버튼 기능
    def func_protein(self):
        # 영양소 위치
        self.idx = 0
        self.labelOrgan.setText("")
        self.labelEnzyme.setText("")
        self.labelNutrients.setGeometry(50, 200, 200, 60)
        self.labelNutrients.setText("단백질")
        self.nutrient = "단백질"
        self.labelNutrients.setFont(QtGui.QFont("초롱바탕", 23))

    # 지방 버튼 기능
    def func_fat(self):
        # 영양소 위치
        self.idx = 0
        self.labelOrgan.setText("")
        self.labelEnzyme.setText("")
        self.labelNutrients.setGeometry(50, 200, 200, 60)
        self.labelNutrients.setText("지 방")
        self.nutrient = "지방"
        self.labelNutrients.setFont(QtGui.QFont("초롱바탕", 23))

    # prev 버튼 내용
    def func_prev(self):
        # 영양소가 정해졌을 때에만 실행
        if self.nutrient:
            # 이전단계로 돌아가는 기능이므로 idx -1
            if self.idx > 0:
                self.idx -= 1
            # ENzyme_name:소화효소 이름, Nutrient_name: 영양소 이름
            Enzyme_name, Organ_name, Nurients_name = self.nutrients[self.nutrient][self.idx]
            self.labelNutrients.setText(Nurients_name)
            self.labelOrgan.setText(Organ_name)
            self.labelEnzyme.setText(Enzyme_name)
            # 지방산과 모노글리세리드 같이 긴 글자는 포트를 줄임
            if len(Enzyme_name) >= 5:
                self.labelNutrients.setFont(QtGui.QFont("초롱바탕", 17))
            x, y, w, h = self.nutrients_geometry[self.nutrient][self.idx]
            self.labelNutrients.setGeometry(x, y, w, h)

    def func_next(self):
        # prev와 idx 증가를 제외하곤 동일
        if self.nutrient:
            if self.idx < len(self.nutrients[self.nutrient])-1:
                self.idx += 1
            print(self.idx ,len(self.nutrients[self.nutrient])-1)
            Enzyme_name, Organ_name, Nurients_name = self.nutrients[self.nutrient][self.idx]
            print(1)
            self.labelNutrients.setText(Nurients_name)
            print(2)
            self.labelOrgan.setText(Organ_name)
            print(3)
            self.labelEnzyme.setText(Enzyme_name)
            print(4)
            x, y, w, h = self.nutrients_geometry[self.nutrient][self.idx]
            print(5)
            self.labelNutrients.setGeometry(x, y, w, h)
            if len(Enzyme_name) >= 5:
                self.labelNutrients.setFont(QtGui.QFont("초롱바탕", 15))

if __name__ == "__main__":
    app = QApplication(sys.argv)    # app = QApplication(): 프로그램을 만드는 객체생성      sys.argv: [현재 실행파일 경로]
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()