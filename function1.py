# function1.py 

#1)함수 정의
def setValue(newValue):
    #지역변수 초기화
    x = newValue
    print("지역변수:", x)

#2)호출
retValue = setValue(5)
print(retValue)

#튜플로 리턴
def swap(x,y):
    return y, x 

#호출
print(swap(3,4))

#지역변수와 전역변수
#전역변수
x = 5 
def func1(a):
    return a+x 

#호출
print(func1(1))

def func2(a):
    #지역변수
    x = 10 
    return a+x 

#호출
print(func2(1))

#디버깅
#교집합 리턴 함수
def intersect(prelist, postlist):
    #지역변수 
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
print(intersect("HAM","SPAM"))

#기본값 셋팅
def times(a=10, b=20):
    return a*b 
#호출
print(times())
print(times(b=5))
print(times(5,6))

#키워드 인자(매개변수명 기술)
def connectURI(server, port):
    strURL = "https://" + server + ":" + port 
    return strURL 
#호출
print(connectURI("multi.com", "80"))
print(connectURI(port="80", server="test.com"))
