# 모듈:변수, 함수, 클래스를 모아둔 파일
# 패키지:여러모듈을 하나의 디렉토리로 모아둔 것

# built-in 된 모듈 - print함수 같은 것(import하지 않아도 쓸수 있는 것)

import sys
import hello  # 같은경로에 있는 파일을 찾아감
import hello as h
from hello import say_hello
# from(패키지 또는 모듈) import(모듈(from 뒤가 패키지일때),변수나 함수나 클래스(from 뒤가 모듈일때))
from hello import *

# __init__.py 파이썬 버전 2점대 일때 해당파일이 있어야 패키지라고 인식이 됨 3점 버전에서는 생략 가능


print(sys.modules)  # 기본적으로 설치되어있는 모듈

print("="*50)

print(sys.path)  # 새로 설치한 모듈


hello.say_hello()
h.say_hello()
say_hello()
