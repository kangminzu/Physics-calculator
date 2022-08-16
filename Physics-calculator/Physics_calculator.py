from cmath import tan
import sys
from wsgiref.handlers import format_date_time
from PyQt5.QtWidgets import *
import math 

#메인 화면
class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()
        
        
        #선택버튼 만들기
        self.samev = QPushButton("등속도 운동") 
        self.samea = QPushButton("등가속도 운동")
        self.parabolic = QPushButton("포물선 운동")
        self.recent = QPushButton("최근 계산 결과")
        
        #버튼 기능 연결
        self.samev.clicked.connect(self.samev_clicked)
        self.samea.clicked.connect(self.samea_clicked)
        self.parabolic.clicked.connect(self.parabolic_clicked)
        self.recent.clicked.connect(self.recent_clicked)
        
        #버튼 크기 조절
        self.samev.setMaximumHeight(500)
        self.samea.setMaximumHeight(500)
        self.parabolic.setMaximumHeight(500)
        self.recent.setMaximumHeight(500)
        
        #레이아웃에 위젯 추가
        grid_layout.addWidget(self.samev,0,0)
        grid_layout.addWidget(self.samea,0,1)
        grid_layout.addWidget(self.parabolic,1,0)
        grid_layout.addWidget(self.recent,1,1)
        main_layout.addLayout(grid_layout,stretch=1)
    
        self.setLayout(main_layout)
        self.setWindowTitle("역학적 상황")
        self.resize(200, 200)
        self.show()
        
    #다른 화면으로 넘어가게 만들기
    
    #등속 운동 화면
    def samev_clicked(self):
        self.hide() # 현재 창 숨기기
        self.samevpage = samev_page()
        self.samevpage.show() # 창 보이기
        
    #등가속도 운동 화면
    def samea_clicked(self):
        self.hide()
        self.sameapage = samea_page()
        self.sameapage.show()
    
    #포물선 운동 화면
    def parabolic_clicked(self):
        self.hide()
        self.parabolicpage = parabolic_page()
        self.parabolicpage.show()
        
    #최근 결과값 화면
    def recent_clicked(self) :
        self.hide()
        self.recentpage = recent_page()
        self.recentpage.show()
        
#등속 운동
class samev_page(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        #메인 레이아웃
        main_layout = QVBoxLayout()
        
        #설명창
        self.explain_label = QLabel("구하려는 값을 체크 후, 요구하는 값을 입력해주세요")
        
        #요구하는 값의 레이아웃
        t_layout = QHBoxLayout()
        v_layout = QHBoxLayout()
        s_layout = QHBoxLayout()
        
        #결과값 레이아웃
        answer_layout = QHBoxLayout()
        
        #구하고자 하는 값 선택 버튼
        self.t_radiobtn = QRadioButton("시간")
        self.v_radiobtn = QRadioButton("속도")
        self.s_radiobtn = QRadioButton("거리")
        
        #요구하는 값 입력창
        self.t_value = QLineEdit()
        self.v_value = QLineEdit()
        self.s_value = QLineEdit()
        
        #결과값 창
        answer_name = QLabel("계산 결과 : ")
        self.answer= QLabel()
        
        #각 레이아웃에 위젯 추가
        t_layout.addWidget(self.t_radiobtn)
        t_layout.addWidget(self.t_value)
        
        v_layout.addWidget(self.v_radiobtn)
        v_layout.addWidget(self.v_value)
        
        s_layout.addWidget(self.s_radiobtn)
        s_layout.addWidget(self.s_value)
        
        answer_layout.addWidget(answer_name)
        answer_layout.addWidget(self.answer)
        
        #값 구하기와 돌아가기 버튼
        self.equal_btn = QPushButton("값 구하기")
        self.back_btn = QPushButton("역학적 상황으로 돌아가기")
        
        main_layout.addWidget(self.explain_label)
        main_layout.addLayout(t_layout)
        main_layout.addLayout(v_layout)
        main_layout.addLayout(s_layout)
        main_layout.addLayout(answer_layout)
        main_layout.addWidget(self.equal_btn)
        main_layout.addWidget(self.back_btn)
        
        #버튼 기능 연결
        self.equal_btn.clicked.connect(self.equal_btn_clicked)
        self.back_btn.clicked.connect(self.back_btn_clicked)
        
        #라디오 버튼 연결
        self.t_radiobtn.clicked.connect(self.t_radiobtn_clicked)
        self.v_radiobtn.clicked.connect(self.v_radiobtn_clicked)
        self.s_radiobtn.clicked.connect(self.s_radiobtn_clicked)
        
        self.setLayout(main_layout)
        self.setWindowTitle("등속도")
        self.resize(300,300)
        self.show()
    
    #값 구하기 버튼 연결
    def equal_btn_clicked(self):
        #시간을 구할 때
        if self.t_radiobtn.isChecked(): #시간 라디오 버튼이 클릭되어있는지 확인
            #변수 설정
            v = float(self.v_value.text())
            s = float(self.s_value.text())
            t = str(round(float(s/v),2)) #식 계산하기
            f = open("calculation.txt", mode = 'a', encoding = 'utf-8') #파일 열기
            f.write(f"{s} / {v} = {t}" + "\n") #식과 결과값을 파일에 저장
            f.close() #파일 닫기
            self.answer.setText(t) #결과값 출력
        #속도를 구할 때
        elif self.v_radiobtn.isChecked(): #속도 라디오 버튼이 클릭되어있는지 확인
            #변수 설정
            t = float(self.t_value.text())
            s = float(self.s_value.text())
            v = str(round(float(s/t),2)) #식 계산하기
            f = open("calculation.txt", mode = 'a', encoding = 'utf-8') #파일 열기
            f.write(f"{s} / {t} = {v}" + "\n") #식과 결과값을 파일에 저장
            f.close() #파일 닫기
            self.answer.setText(v) #결과값 출력
        #거리를 구할 때
        elif self.s_radiobtn.isChecked(): #거리 라디오 버튼이 클릭되어있는지 확인
            #변수 설정
            t = float(self.t_value.text())
            v = float(self.v_value.text())
            s = str(round(float(v*t),2)) #식 계산하기
            f = open("calculation.txt", mode = 'a', encoding = 'utf-8') #파일 열기
            f.write(f"{v} * {t} = {s}" + "\n") #식과 결과값을 파일에 저장
            f.close() #파일 닫기
            self.answer.setText(s) #결과값 출력
            
    #시간을 구할 때 안내문구        
    def t_radiobtn_clicked(self):
        self.explain_label.setText("속도와 거리를 입력해주세요.")
    
    #속도를 구할 때 안내문구
    def v_radiobtn_clicked(self):
        self.explain_label.setText("거리와 시간을 입력해주세요.")
        
    #거리를 구할 때 안내문구
    def s_radiobtn_clicked(self):
        self.explain_label.setText("속도와 시간을 입력해주세요.")
        
    #역학적 상황으로 돌아가기 버튼
    def back_btn_clicked(self):
        self.close()
        self.main = Main()
        self.main.show()
        
#등가속도 운동
class samea_page(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        #메인 레이아웃
        main_layout = QVBoxLayout()
        
        #설명창
        self.explain_label = QLabel("구하려는 값을 체크 후, 요구하는 값을 입력해주세요")
        
        #요구하는 값의 레이아웃
        t_layout = QHBoxLayout()
        vi_layout = QHBoxLayout()
        vf_layout = QHBoxLayout()
        s_layout = QHBoxLayout()
        a_layout = QHBoxLayout()
        
        #결과값 레이아웃
        answer_layout = QHBoxLayout()
        
        #구하고자 하는 값 선택 버튼
        self.t_radiobtn = QRadioButton("시간")
        self.vi_radiobtn = QRadioButton("처음 속도")
        self.vf_radiobtn = QRadioButton("나중 속도")
        self.s_radiobtn = QRadioButton("거리")
        self.a_radiobtn = QRadioButton("가속도")
        
        #요구하는 값 입력창
        self.t_value = QLineEdit()
        self.vi_value = QLineEdit()
        self.vf_value = QLineEdit()
        self.s_value = QLineEdit()
        self.a_value = QLineEdit()
        
        #결과값 창
        answer_name = QLabel("계산 결과 :")
        self.answer = QLabel()
        
        #각 레이아웃에 위젯 추가
        t_layout.addWidget(self.t_radiobtn)
        t_layout.addWidget(self.t_value)
        
        vi_layout.addWidget(self.vi_radiobtn)
        vi_layout.addWidget(self.vi_value)
        
        vf_layout.addWidget(self.vf_radiobtn)
        vf_layout.addWidget(self.vf_value)
        
        s_layout.addWidget(self.s_radiobtn)
        s_layout.addWidget(self.s_value)
        
        a_layout.addWidget(self.a_radiobtn)
        a_layout.addWidget(self.a_value)
        
        answer_layout.addWidget(answer_name)
        answer_layout.addWidget(self.answer)
        
        #값 구하기와 돌아가기 버튼
        self.equal_btn = QPushButton("값 구하기")
        self.back_btn = QPushButton("역학적 상황으로 돌아가기")
        
        main_layout.addWidget(self.explain_label)
        main_layout.addLayout(t_layout)
        main_layout.addLayout(vi_layout)
        main_layout.addLayout(vf_layout)
        main_layout.addLayout(s_layout)
        main_layout.addLayout(a_layout)
        main_layout.addLayout(answer_layout)
        main_layout.addWidget(self.equal_btn)
        main_layout.addWidget(self.back_btn)
        
        #버튼 기능 연결
        self.equal_btn.clicked.connect(self.equal_btn_clicked)
        self.back_btn.clicked.connect(self.back_btn_clicked)
        
        #라디오 버튼 기능 연결
        self.t_radiobtn.clicked.connect(self.t_radiobtn_clicked)
        self.vi_radiobtn.clicked.connect(self.vi_radiobtn_clicked)
        self.vf_radiobtn.clicked.connect(self.vf_radiobtn_clicked)
        self.s_radiobtn.clicked.connect(self.s_radiobtn_clicked)
        self.a_radiobtn.clicked.connect(self.a_radiobtn_clicked)
        
        self.setLayout(main_layout)
        self.setWindowTitle("등가속도")
        self.resize(300,300)
        self.show()
    
    #값 구하기 기능 연결
    def equal_btn_clicked(self): 
        if self.t_radiobtn.isChecked(): #시간 라디오 버튼 클릭되어있는지 확인
            f = open("calculation.txt", mode = 'a', encoding = 'utf-8') #파일 열기
            if self.a_value.text() == "": #가속도 값이 없을 때
                #변수 설정
                vi = float(self.vi_value.text())
                vf = float(self.vf_value.text())
                s = float(self.s_value.text())
                t = str(round(float(2*s/(vi+vf)),2)) #식 계산하기
                f.write(f"2*{s} / ({vi} + {vf}) = {t}" + "\n") #식과 결과값을 파일에 저장
            else:
                #변수 설정
                vi = float(self.vi_value.text())
                vf = float(self.vf_value.text())
                a = float(self.a_value.text())
                t = str(round(float((vf-vi)/a),2)) #식 계산하기
                f.write(f'({vf} - {vi}) / {a} = t' + "\n") #식과 결과값을 파일에 저장
            f.close() #파일 닫기
            self.answer.setText(t) #결과값 출력
        
        elif self.vi_radiobtn.isChecked(): #처음 속도 라디오 버튼 클릭되어있는지 확인
            f = open("calculation.txt", mode = 'a', encoding = 'utf-8') #파일 열기
            if self.s_value.text() == "": #거리 값이 없을 때
                #변수 설정
                t = float(self.t_value.text())
                vf = float(self.vf_value.text())
                a = float(self.a_value.text())
                vi = str(round(float(vf-(a*t)),2)) #식 계산하기
                f.write(f"({vf} - ({a} * {t}) = {vi}" + "\n") #식과 결과값을 파일에 저장
            else:
                #변수 설정
                t = float(self.t_value.text())
                vf = float(self.vf_value.text())
                s = float(self.s_value.text())
                vi = str(round(float(2*s/t - vf),2)) #식 계산하기
                f.write(f'(2*{s} / {t} - {vf}) = {vi}' + "\n") #식과 결과값을 파일에 저장
            f.close() #파일 닫기
            self.answer.setText(vi) #결과값 출력
            
        elif self.vf_radiobtn.isChecked(): #나중 속도 라디오 버튼 클릭되어있는지 확인
            f = open("calculation.txt", mode = 'a', encoding = 'utf-8') #파일 열기
            if self.s_value.text() =="": #거리 값이 없을 때
                #변수 설정
                t = float(self.t_value.text())
                vi = float(self.vi_value.text())
                a = float(self.a_value.text())
                vf = str(round(float(vi + a*t),2)) #식 계산하기
                f.write(f'{vi} + {a} * {t} = {vf}' + "\n") #식과 결과값을 파일에 저장
            else:
                #변수 설정
                t = float(self.t_value.text())
                vi = float(self.vi_value.text())
                s = float(self.s_value.text())
                vf = str(round(float(2*s/t - vi),2)) #식 계산하기
                f.write(f'2*{s} / {t} - {vi} = {vf}' + "\n") #식과 결과값을 파일에 저장
            f.close() #파일 닫기
            self.answer.setText(vf) #결과값 출력
            
        elif self.s_radiobtn.isChecked(): #거리 라디오 버튼 클릭되어있는지 확인
            f = open("calculation.txt", mode = 'a', encoding = 'utf-8') #파일 열기
            if self.vf_value.text() =="": #나중 속도 값이 없을 때
                #변수 설정
                t = float(self.t_value.text())
                vi = float(self.vi_value.text())
                a = float(self.a_value.text())
                s = str(round(float((vi*t)+(a*(t**2)/2)),2)) #식 계산하기
                f.write(f'({vi} * {t}) + ({a} * ({t}^2) / 2) = {s}' + "\n") #식과 결과값을 파일에 저장
            else:
                #변수 설정
                t = float(self.t_value.text())
                vi = float(self.vi_value.text())
                vf = float(self.vf_value.text())
                s = str(round(float((vi+vf)*t/2),2)) #식 계산하기
                f.write(f'({vi} + {vf}) * {t}/2 = {s}' + "\n") #식과 결과값을 파일에 저장
            f.close() #파일 닫기
            self.answer.setText(s) #결과값 출력
            
        elif self.a_radiobtn.isChecked():#가속도 라디오 버튼클릭되어있는지 확인
            f = open("calculation.txt", mode = 'a', encoding = 'utf-8') #파일 열기
            if self.s_value.text() == "": #거리 값이 없을 때 
                #변수 설정
                t = float(self.t_value.text())
                vi =float(self.vi_value.text())
                vf = float(self.vf_value.text())
                a = str(round(float((vf-vi)/t),2)) #식 계산하기
                f.write(f'({vf} - {vi}) / {t} = {a}' + "\n") #식과 결과값을 파일에 저장
            else:
                #변수 설정
                vi =float(self.vi_value.text())
                vf = float(self.vf_value.text())
                s = float(self.s_value.text())
                a = str(round(float((vf**2 - vi**2)/(2*s)),2)) #식 계산하기
                f.write(f'({vf}^2 - {vi}^2) / (2*{s}) = {a}' + "\n") #식과 결과값을 파일에 저장
            f.close() #파일 닫기
            self.answer.setText(a) #결과값 출력
        
    #시간을 구할 때 안내문구        
    def t_radiobtn_clicked(self):
        self.explain_label.setText("처음속도, 나중속도, 거리 혹은 가속도를 입력해주세요.")
        
    #처음속도를 구할 때 안내문구
    def vi_radiobtn_clicked(self):
        self.explain_label.setText("시간, 나중속도, 거리 혹은 가속도를 입력해주세요.")
    
    #나중속도를 구할 때 안내문구
    def vf_radiobtn_clicked(self):
        self.explain_label.setText("처음속도, 시간, 거리 혹은 가속도를 입력해주세요.")
    
    #거리를 구할 때 안내문구
    def s_radiobtn_clicked(self):
        self.explain_label.setText("처음속도, 시간, 나중속도 혹은 가속도를 입력해주세요.")
        
    #가속도를 구할 때 안내문구
    def a_radiobtn_clicked(self):
        self.explain_label.setText("처음속도, 나중속도, 시간 혹은 거리를 입력해주세요.")
        
    def back_btn_clicked(self):
        self.close()
        self.main = Main()
        self.main.show()
 
 #포물선 운동
class parabolic_page(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        #메인 레이아웃
        main_layout = QVBoxLayout()
        
        #설명창
        self.explain_label = QLabel("구하려는 값을 체크 후, 요구하는 값을 입력해주세요")
        
        #요구하는 값의 레이아웃
        x_layout = QHBoxLayout()
        v_layout = QHBoxLayout()
        d_layout = QHBoxLayout()
        y_layout = QHBoxLayout()
        h_layout = QHBoxLayout()
        r_layout = QHBoxLayout()
        
        #결과값 레이아웃
        answer_layout = QHBoxLayout()
        
        #구하고자 하는 값 선택 버튼
        self.x_radiobtn = QLabel("x좌표")
        self.v_radiobtn = QLabel("처음 속도")
        self.d_radiobtn = QLabel("각도")
        self.y_radiobtn = QRadioButton("y축 좌표")
        self.h_radiobtn = QRadioButton("최고 높이")
        self.r_radiobtn = QRadioButton("수평 도달 거리")
        
        #요구하는 값 입력창
        self.x_value = QLineEdit()
        self.v_value = QLineEdit()
        self.d_value = QLineEdit()
        self.y_value = QLabel()
        self.h_value = QLabel()
        self.r_value = QLabel()
        
        #결과값 창
        answer_name = QLabel("계산 결과 :")
        self.answer = QLabel()
        
        #각 레이아웃에 위젯 추가
        x_layout.addWidget(self.x_radiobtn)
        x_layout.addWidget(self.x_value)
        
        v_layout.addWidget(self.v_radiobtn)
        v_layout.addWidget(self.v_value)
        
        d_layout.addWidget(self.d_radiobtn)
        d_layout.addWidget(self.d_value)
        
        y_layout.addWidget(self.y_radiobtn)
        y_layout.addWidget(self.y_value)
        
        h_layout.addWidget(self.h_radiobtn)
        h_layout.addWidget(self.h_value)
        
        r_layout.addWidget(self.r_radiobtn)
        r_layout.addWidget(self.r_value)
        
        answer_layout.addWidget(answer_name)
        answer_layout.addWidget(self.answer)
        
        #값 구하기와 돌아가기 버튼
        self.equal_btn = QPushButton("값 구하기")
        self.back_btn = QPushButton("역학적 상황으로 돌아가기")
        
        main_layout.addWidget(self.explain_label)
        main_layout.addLayout(x_layout)
        main_layout.addLayout(v_layout)
        main_layout.addLayout(d_layout)
        main_layout.addLayout(y_layout)
        main_layout.addLayout(h_layout)
        main_layout.addLayout(r_layout)
        main_layout.addLayout(answer_layout)
        main_layout.addWidget(self.equal_btn)
        main_layout.addWidget(self.back_btn)
        
        #버튼 기능 연결
        self.equal_btn.clicked.connect(self.equal_btn_clicked)
        self.back_btn.clicked.connect(self.back_btn_clicked)
        
        #라디오 버튼 기능 연결
        self.y_radiobtn.clicked.connect(self.y_radiobtn_clicked)
        self.h_radiobtn.clicked.connect(self.h_radiobtn_clicked)
        self.r_radiobtn.clicked.connect(self.r_radiobtn_clicked)
        
        self.setLayout(main_layout)
        self.setWindowTitle("포물선 운동")
        self.resize(300,300)
        self.show()
      
    #값 구하기 버튼 기능 연결  
    def equal_btn_clicked(self):
        if self.y_radiobtn.isChecked(): #y좌표 라디오 버튼이 클릭되어있는지 확인
            #변수 설정
            x = float(self.x_value.text())
            v = float(self.v_value.text())
            d = float(self.d_value.text())
            y = str(round((math.tan(math.pi*(d/180))*x) - (((x**2)*10) / (2*(v**2)*math.cos(math.pi*(d/180)))),2)) #식 계산하기
            f = open("calculation.txt", mode = 'a', encoding = 'utf-8') #파일 열기
            f.write(f"(tan{d}*{x}) - ({x}^2 * 10 / 2{v}^2cos{d}) = {y}" + "\n") #식과 결과값을 파일에 저장
            f.close() #파일 닫기
            self.answer.setText(y) #결과값 출력
            
        elif self.h_radiobtn.isChecked(): #최고 높이 라디오 버튼이 클릭되어있는지 확인
            #변수 설정
            v = float(self.v_value.text())
            d = float(self.d_value.text())
            h = str(round(((v * (math.sin(math.pi *(d/180))))**2) / 20,2)) #식 계산하기
            f = open("calculation.txt", mode = 'a', encoding = 'utf-8') #파일 열기
            f.write(f'{v} * sin{d}^2 / 20 = {h}' + "\n") #식과 결과값을 파일에 저장
            f.close() #파일 닫기
            self.answer.setText(h) #결과값 출력
            
        elif self.r_radiobtn.isChecked(): #최고 도달 거리 라디오 버튼이 클릭되어있는지 확인
            #변수 설정
            v = float(self.v_value.text())
            d = float(self.d_value.text()) 
            r = str(round((v**2) * (math.sin(math.pi*(2*d / 180))) / 10,2)) #식 계산하기
            f = open("calculation.txt", mode = 'a', encoding = 'utf-8') #파일 열기
            dd = 2 * d
            f.write(f'{v}^2 * sin{dd}/ 10 = {r}' + "\n") #식과 결과값을 파일에 저장
            f.close() #파일 닫기
            self.answer.setText(r) #결과값 출력
        
    #y좌표를 구할 때 안내문구        
    def y_radiobtn_clicked(self):
        self.explain_label.setText("x좌표, 속도, 각도를 입력해주세요.")
        
    #최고 높이를 구할 때 안내문구
    def h_radiobtn_clicked(self):
        self.explain_label.setText("속도와 각도를 입력해주세요.")
    
    #최대 도달 거리를 구할 때 안내문구
    def r_radiobtn_clicked(self):
        self.explain_label.setText("속도와 각도를 입력해주세요.")
        
    def back_btn_clicked(self):
        self.close()
        self.main = Main()
        self.main.show()
 
 #최근 결과 확인
class recent_page(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        #메인 레이아웃
        main_layout = QVBoxLayout()
        
        self.recent_value = QLabel("[최근 결과 값]" + "\n")
        back_btn = QPushButton("역학적 상황 돌아가기")
        
        main_layout.addWidget(self.recent_value)
        main_layout.addWidget(back_btn)

        f = open("calculation.txt", mode = 'r', encoding = 'utf-8') #파일 열기
        
        lines = f.readlines() #문자열로 파일의 값 받기
        leng = len(lines) #문자열의 길이 저장
        
        num = 0
        
        for i in reversed(range(leng)): #문자열이 길이에서부터 거꾸로 i를 진행
            exist = self.recent_value.text() #현재 입력된 값을 변수로 저장
            value = str(exist) + str(lines[i]) #문자열 뒤에서부터 현재 입력된 값과 더함
            self.recent_value.setText(str(value)) #출력
            num += 1
            if num == 10 : #10번 반복
                break #종료
            
        f.close() #파일 닫기
        
        #버튼 기능 연결
        back_btn.clicked.connect(self.back_btn_clicked)
        
        self.setLayout(main_layout)
        self.setWindowTitle("최근 결과") #윈도우 창 이름 변환
        self.resize(300,300)
        self.show()
        
    #역학적 상황으로 돌아가기 기능 연결
    def back_btn_clicked(self):
        self.close()
        self.mainpage = Main()
        self.mainpage.show()
                 
if __name__=="__main__":
    app=QApplication(sys.argv)
    main=Main()
    sys.exit(app.exec_())