
# 클래스

class User:
    username = "ssar"
    password = "1234"


u = User()

print(u.username)
print("="*50)


class Person:
    def __init__(self, username, password):  # __init__ 생성자 키워드
        self.username = username  # self를 사용하여 전역변수 선언
        self.password = password


p = Person("ssar", "1234")
print(p.username)
