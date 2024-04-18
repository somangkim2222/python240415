# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup

#디자인한 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

#윈도우 클래스 정의
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__() 
        self.setupUi(self)        
    def firstClick(self):

        url = "https://www.daangn.com/fleamarket/"

        #페이지 실행 요청
        response = requests.get(url)

        #검색이 용이한 객체
        soup = BeautifulSoup(response.text, "html.parser")
        f=open("daangn.txt","a+",encoding="utf-8")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            titleElem = post.find("h2", attrs={"class":"card-title"})
            title = titleElem.text.strip()
            priceElem = post.find("div", attrs={"class":"card-price"})
            price = titleElem.text.strip()
            addrElem = post.find("div", attrs={"class":"card-region-nam"})
            addr = titleElem.text.strip()
            #화면에 출력
            print(f"{title},{price},{addr}")
            f.write(f"{title},{price},{addr}\n")
        #파일 닫기
        f.close()
        self.label.setText("당근마켓 크롤링 완료")

    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭")

#직접 모듈을 실행햇는지 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()