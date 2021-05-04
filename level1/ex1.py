#HelloWorld 파스칼표기법
#helloWorld 낙타표기법
#hello_world 언더스코어(파이썬)

#타입추론
#모든 것이 오브젝트
#인터프리터

#1.숫자
a = 1
b = 1.2
c = 4e5

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#연산자 +,-,*,/,%
e = 3
f = 4

print(e**f) # ** 제곱
print(e//f) # // 몫
print(4%3) # % 나머지


#2. 문자열

# " ", ' ' 둘다 구분 안함 둘중 하나 아무거나 써도 됨
# ''' ''' 
s1 = "안녕하세요"
s2 = '안녕하세요'
s3 = '''
안녕하세요
'''
print(s1)
print(s2)
print(s3)

s4 = s1 + s2
print(s4)

s5 = '홍길동'

print(s5+'님 안녕하세요')
print(f"{s5}님 안녕하세요")
print('='*50)

#3. 슬라이싱:

str1 = '가나다라마'

print(str1[0:3]) #슬라이싱 연산자는 마지막 인덱스 번호 직전까지 뽑아요
print(str1[-1])
print(str1[1:]) #마직막 인덱스 번호가 없으면 끝까지 뽑아요



