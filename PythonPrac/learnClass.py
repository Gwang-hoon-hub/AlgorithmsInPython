# 클래스 강의 1

# 클래스 선언
class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

user1 = UserInfo("kim")

print(user1.__dict__)

#
# 클래스 메소드, 인스턴스 메소드 따로 있음
# 클래스, 인스턴스
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접사용 가능, 객체보다 먼저 생성 --> JAVA 에서 static
# 인스턴스 변수 : 객체마다 별도로 생성되서 존재한다. 인스턴스 생성 후 사용한다.

class SelfTest:
    def function1(self):
        print('function1 is called!!!')

    def function2(self):
        print(id(self)) # 인스턴스화 된 객체인 self 의 id 를 알려줄것이다.
        print("function2 is called!!!")

selfTest1 = SelfTest()
# selfTest1.function1() --> 해당 메소드는 self를 갖고 있지 않기 때문에 클래스 메소드이다.
selfTest1.function2()
SelfTest.function1()

# self 인스턴스화
print(id(selfTest1))
SelfTest.function2(selfTest1) # 클래스 메소드로 사용을 하려는 경우 self에 인스턴스를 넣어준다.



# 클래스 변수
class VariableClass:
    stock_num = 0 # 클래스 변수 --> 모든 인스턴스가 공유한다.
    def __init__(self, name):
        self.name = name
        VariableClass.stock_num += 1
    def __del__(self):
        VariableClass.stock_num -= 1

user1 = VariableClass("kim")
user2 = VariableClass("lee")
user3 = VariableClass("soo")

print(VariableClass.__dict__) # 클래스 네임스페이스 클래스 변수 공유

del user1 # 인스턴스 삭제

print(user2.stock_num)



