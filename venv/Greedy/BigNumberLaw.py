import sys

def solution():
    # n, m, k 를 공백으로 구분하여 입력받기
    n, m, k  = map(int, input().split())
    # N개의 수를 공백으로 구분하여 입력받기
    data = list(map(int, input().split()))

    # 주어진 숫자배열 정렬
    data.sort(reverse = True) # 데이터 역정렬
    data.sort()
    first = data[n-1]
    second = data[n-2]

    # 제일 큰 수가 사용되는 횟수
    re = m // (k+1) # 반복되는 횟수
    namuzi = m % (k+1) # 나머지 횟수

    # 두 번째 큰 수가 사용되는 횟수
    # 총합
    result = first * re * k + second * re + first * namuzi
    print(result)

def solution1():
    # n, m, k 를 공백으로 구분하여 입력받기
    n, m, k  = map(int, input().split())
    # N개의 수를 공백으로 구분하여 입력받기
    data = list(map(int, input().split()))

    # 주어진 숫자배열 정렬
    # data.sort()
    first = data[n-1]
    second = data[n-2]

    result = 0

    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1


if __name__ == '__main__':
    solution()