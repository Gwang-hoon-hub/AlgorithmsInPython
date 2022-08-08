#List



class Six_th:
    list1 = [1, 4, 5, 6, 7, '문자열']
    print(list1[-3:]) #[6, 7, '문자열']

    list[:] # 레퍼런스를 참조하는 복사본

    list1 + [23,54,12, '붙이기']

    list1[3] = 'fixDATA'

    list1.append('addData') # 데이터 추가하기

    letters = ['a', 'b', 'c', 'd']
    letters[1:3]
    letters[1:3] = ['B', 'C']
    letters[1:3] = ['B', 'C', 0]
    letters[1:2] = []
    letters[:] = []


    a = [1,2,3]
    b = [4,5,6]
    c = [a, b] # 2차원 배열

    a, b = 0, 1 # 한꺼번에 여러개 변수 선언 가능

    while b<10:
        print(b)
        a, b = b, a  # -> multiple assignment 가 가능하다.
        # 다른 언어들은 temporary  변수를 사용하지만 파이썬은 그렇지 않다.


