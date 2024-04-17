# web1.py
from bs4 import BeautifulSoup

#파일 로딩(함수체인, 메서드체인)
page = open("Chap09_test.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#전체 보기
#print(soup.prettify())

#<p> 태그 전체 검색 : ResultSet리턴 -> List 비슷한 파생형식
#print(soup.find_all("p"))

#print(soup.find_all("p", class_="outer-text"))

#print(soup.find_all("p", attrs={"class":"outer-text"}))

for tag in soup.find_all("p"):
    title=tag.text.strip()
    #줄바꿈 문자 변환
    title=title.replace("\n","")
    print(title)