#선택한 블럭을 주석처리: ctrl + / 
# score = int(input('점수를 입력:'))
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# elif 60 <= score < 70:
#     grade = "D"
# else:
#     grace = "F"
    
# print("Grade is " + grade)

value = 5 
while value > 0:
    print(value)
    value -= 1 

d = {"apple":5, "kiwi":10}
for item in d.items():
    print(item)

print("---key, value 별로 처리---")
for k,v in d.items():
    print(k, v)

print("---수열함수---")
print( list(range(10)) )
print( list(range(2000, 2025)) )
print( list(range(1, 32)) )

print("---리스트 임베딩---")
lst = list(range(1,11))
print( [i**2 for i in lst if i > 5] )

d = {100:"apple", 200:"orange", 300:"kiwi"}
print( [v.upper() for v in d.values()] )

print("---필터링함수---")
l = [10, 25, 30]
iterL = filter(None, l)
for i in iterL:
    print("Item:{0}".format(i))

print("---필터링 함수 있는 경우---")
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, l)
for i in iterL:
    print("Item:{0}".format(i))

print("---람다함수---")
iterL = filter(lambda x:x>20, l)
for i in iterL:
    print("Item:{0}".format(i))

