# 딕셔너리
# key, value 로 되어 있다.
# for문 을 돌릴 때에는 딕셔너리 .item() 을 사용한다.


def mul_func(*args):
    return args

def kwarg_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

kwarg_func(name1="qwe")
print(mul_func(1,2,3))

# 중첩함수 (클로저) --> 데코레이터

def nested_func(num):
    def nested_in_func(num):
        print(num)
    print("in function")
    nested_in_func(num + 100)

nested_func(100)

# 함수 파라미터 타입 명시 / 리턴값 타입 명시
def func_type(x : int) -> list:
    y1 = x + 1
    y2 = x + 2
    y3 = x + 3
    return [y1, y2, y3]

print(func_type(12))

# 람다식
# 함수는 객체를 생성한 후 실행한다. -> 메모리 할당
# 람다식은 메모리 할당을 하지 않고 바로 실행한다. -> Heap 메모리 초기화

# 일반적 함수 -> 람다식
def original_func(x : int) -> int:
    return x + 10

var_func = original_func
print(var_func)
print(type(var_func))

print(var_func(10))

lambda_mul_10 = lambda x : x * 10

print(lambda_mul_10)
print(lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)
print(func_final(10, 10, lambda x : x * 1000))






