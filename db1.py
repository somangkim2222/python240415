# db1.py 
import sqlite3

#일단 메모리에서 임시 저장
con = sqlite3.connect(":memory:")
#커서 객체 
cur = con.cursor() 

#테이블(자료구조) 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook values ('홍길동','010-222');")

#외부에서 입력 파라메터 처리
name = "전우치"
phoneNum = "010-333"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNum))

#다중행을 입력
datalist = (("김길동","010-123"), ("박문수","010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)
#검색
cur.execute("select * from PhoneBook;")
#선택행 주석: ctrl + / 
# for row in cur: 
#     print(row[0], row[1])
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

