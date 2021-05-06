# 오버로딩 없음

def add(a, b):
    return a+b


print(add(1, 2))
print("="*50)


def minus(a, b=5):  # 선택적 매개변수 사용 가능
    return a-b


print(minus(10))  # b 매개변수 안넣으면 기본 값
print("="*50)

print(minus(10, 7))  # b 매개변수 넣으면 넣은 값 사용
print("="*50)


def many(*data):  # 튜플로 받음
    print(data)


many(1, 2, 3, 4, 5)


def keyword(**data):  # 딕셔너리 데이터 받기
    print(data)


keyword(id=1, username='ssar')


n1 = 1


def var_test():
    global n1  # 전역변수를 함수 내에서 사용 시 global 사용
    n1 = 2


var_test()
print(n1)
