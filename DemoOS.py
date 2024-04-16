# DemoOS.py 
import random

print(random.random())
print(random.random())
print( [random.randrange(20) for i in range(10)] )
print( [random.randrange(20) for i in range(10)] )
print( random.sample(range(20), 10) )
print( random.sample(range(20), 10) )
print("---로또번호---")
print( random.sample(range(1,46), 5) )

from os.path import * 
print( abspath("python.exe") )
print( basename("c:\\work\\python.exe") )
print( getsize("c:\\python310\\python.exe") )

if exists("c:\\python310\\python.exe"):
    print("파일 있음")
else:
    print("파일 없음")

from os import * 

print("운영체제이름:", name)
print("환경변수", environ)
#외부 실행파일 실행 
#system("notepad.exe")

import glob 

result = glob.glob("c:\\work\\*.py")
print(result)

