# function2.py 
#가변인자 처리 
def union(*ar):
    #지역변수 초기화
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#여러가지 경우
print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))
