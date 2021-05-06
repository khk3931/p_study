# 딕셔너리{"key":"value"}  ex>  {1:"홍길동"}  {자료형 : 자료형} => 파이썬에서 몽고DB에 값 넣을 때 사용
# 자바스크립트{key:value}  ex> {username : "홍길동"}  {변수 : 자료형}  => 몽고DB(자바스크립트 오브젝트를 넣어야 함)
# JSON {"key":value} {변수 : 오브젝트}


dic1 = {"username": "ssar"}
print(dic1)
print("="*50)

print(dic1["username"])
print("="*50)

# 딕셔너리 값 추가
dic1["password"] = "12345"  # 키값이 없으면 추가 있으면 덮어 씌운다
print(dic1)
print("="*50)


#del 삭제

# key값 추출하기
dic2 = {"username": "ssar", "password": "1234"}

print(dic2.keys())  # 키값만 표시
print("="*50)
print(dic2.values())  # value값만 표시
print("="*50)


# key값과 value값 동시에 추출하기
for i in dic2:
    print(i)

print("="*50)

list1 = []
for k, v in dic2.items():  # items() 함수가 중요
    print(k, v)
    list1.append(v)  # 들여쓰기 끝나는 곳에서 for문이 종료 됨

print(list1)
print("="*50)

for i in range(1, 6):
    print(i)
