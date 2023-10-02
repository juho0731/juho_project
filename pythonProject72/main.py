import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtGui import QPixmap

# 불러올 UI
form_class = uic.loadUiType("DigestiveSystem_UI.ui")[0]

class WindowClass(QMainWindow,form_class):
    def __init__(self):
        # 부모 클래스들의 init 활성화
        super().__init__()
        # 불러온 ui form_class를 적용시킨다
        self.setupUi(self)
        self.setWindowTitle("Digetive System")
        self.loadImageFromFile()


        # 소화효소 textLabel:
        self.digestive_enzymes = QLabel(self)
        self.digestive_enzymes.setAlignment(QtCore.Qt.AlignCenter)  # 가로 정렬
        self.digestive_enzymes.setStyleSheet("background:transparent;")
        self.digestive_enzymes.setFont(QtGui.QFont('초롱바탕', 18))
        self.digestive_enzymes.setGeometry(700,150,300,90)

        # 영양소 textLabel
        self.labelNutrients = QLabel(self)
        self.labelNutrients.setAlignment(QtCore.Qt.AlignCenter) # 가로 정렬
        self.labelNutrients.setStyleSheet("background:transparent;")  # "backgound: transparent;" - 배경 투명하게
        self.labelNutrients.setFont(QtGui.QFont('초롱바탕', 28))

        # 현재 보고 있는 영양소 정보
        self.nutrient = ''
        # 영양소 변화과정 {영양소: [(효소,변화된 영양소),(),()], }
        self.nutrients = {
            '탄수화물': [('아밀레이스', '엿당'), ('아밀레이스', '엿당'), ('말테이스', '포도당')],
            '단백질': [('펩신', '폴리팹티드'), ('트립신', '디펩티드'), ('펩티데이스', '아미노산')],
            '지방': [("쓸개즙", '지방 유화'), ('라이페이스', '지방산과 모노글리셀리드')]
        }
        # 영양소 별 위치 값
        self.carbs_geometry = [(250,180,200,60),(150,650,200,60),(210,800,200,60)]
        self.protein_geometry = [(380,600,240,60),(150,650,200,60),(210,800,200,60)]
        self.fat_geometry = [(140,630,200,60),(140,680,340,60)]

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
        self.idx = -1
        self.labelNutrients.setStyleSheet("background:#6897FC;"   #  "backgound: transparent;" - 배경 투명하게
                                          "border-style: solid;"
                                          "border-width: 1px;"
                                          "border-color: black;"
                                          "border-radius: 10px;"
                                          )
        self.digestive_enzymes.setText("소화효소:                ")
        self.digestive_enzymes.setStyleSheet("background:#6897FC;"  # "backgound: transparent;" - 배경 투명하게
                                             "border-style: solid;"
                                             "border-width: 1px;"
                                             "border-color: black;"
                                             "border-radius: 10px;"
                                             )
        self.labelNutrients.setGeometry(50,200,200,60)      # 기본 위치
        self.labelNutrients.setText("탄수화물")
        self.nutrient = '탄수화물'


    # 단백질 버튼 기능
    def func_protein(self):
        # 영양소 위치
        self.idx = -1
        self.labelNutrients.setStyleSheet("background:#6897FC;"   #  "backgound: transparent;" - 배경 투명하게
                                          "border-style: solid;"
                                          "border-width: 1px;"
                                          "border-color: black;"
                                          "border-radius: 10px;"
                                          )
        self.digestive_enzymes.setText("소화효소:                ")
        self.digestive_enzymes.setStyleSheet("background:#6897FC;"  # "backgound: transparent;" - 배경 투명하게
                                             "border-style: solid;"
                                             "border-width: 1px;"
                                             "border-color: black;"
                                             "border-radius: 10px;"
                                             )
        self.labelNutrients.setGeometry(50,200,200,60)
        self.labelNutrients.setText("단백질")
        self.nutrient = '단백질'


    # 지방 버튼 기능
    def func_fat(self):
        # 영양소 위치
        self.idx = -1
        self.labelNutrients.setStyleSheet("background:#6897FC;"   #  "backgound: transparent;" - 배경 투명하게
                                          "border-style: solid;"
                                          "border-width: 1px;"
                                          "border-color: black;"
                                          "border-radius: 10px;"
                                          )
        self.digestive_enzymes.setText("소화효소:                ")
        self.digestive_enzymes.setStyleSheet("background:#6897FC;"  # "backgound: transparent;" - 배경 투명하게
                                             "border-style: solid;"
                                             "border-width: 1px;"
                                             "border-color: black;"
                                             "border-radius: 10px;"
                                             )
        self.labelNutrients.setGeometry(50,200,200,60)
        self.labelNutrients.setText("지 방")
        self.nutrient = '지방'


    # prev 버튼 내용
    def func_prev(self):
        # 영양소가 정해졌을 때에만 실행
        if self.nutrient:
            # 이전단계로 돌아가는 기능이므로 idx -1
            if self.idx > 0:
                self.idx -= 1
            # 소화효소 변화 된 이름으로 text설정
            self.digestive_enzymes.setText("소화효소: " +self.nutrients[self.nutrient][self.idx][0])
            # 영양소가 변화 된 이름으로 text설정
            self.labelNutrients.setText(self.nutrients[self.nutrient][self.idx][1])
            # 지방의 경우 지방산과 모노글리셀리드로 긴 문장이 나오므로 폰트 크기 줄이기
            if len(self.nutrients[self.nutrient][self.idx][1]) > 6:
                self.labelNutrients.setFont(QtGui.QFont('초롱바탕', 18,))
            # 영양소별 위치값 불러와서 적용
            if self.nutrient == '탄수화물':
                x,y,w,h = self.carbs_geometry[self.idx]
            elif self.nutrient == '단백질':
                x,y,w,h = self.protein_geometry[self.idx]
            else:
                x,y,w,h = self.fat_geometry[self.idx]
            self.labelNutrients.setGeometry(x,y,w,h)

    # next 버튼 내용
    def func_next(self):
        # prev와 idx 증가를 제외하곤 동일
        if self.nutrient:
            if self.idx < len(self.nutrients[self.nutrient])-1:
                self.idx += 1
            if len(self.nutrients[self.nutrient][self.idx][1]) > 6:
                self.labelNutrients.setFont(QtGui.QFont('초롱바탕', 18))
            self.digestive_enzymes.setText("소화효소: " +self.nutrients[self.nutrient][self.idx][0])
            self.labelNutrients.setText(self.nutrients[self.nutrient][self.idx][1])
            if self.nutrient == '탄수화물':
                x, y, w, h = self.carbs_geometry[self.idx]
            elif self.nutrient == '단백질':
                x, y, w, h = self.protein_geometry[self.idx]
            else:
                x, y, w, h = self.fat_geometry[self.idx]
            self.labelNutrients.setGeometry(x, y, w, h)


if __name__ == "__main__":
    app = QApplication(sys.argv)    # app = QApplication(): 프로그램을 만드는 객체생성      sys.argv: [현재 실행파일 경로]
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()