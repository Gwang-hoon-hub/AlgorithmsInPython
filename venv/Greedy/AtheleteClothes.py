def solution(n, lost, reserve):
    # 1. student 배열 생성
    student = [0]*(n+2)

    # 2. reserve / lost 정보 반영
    for r in reserve:
        student[r] += 1
    for l in lost:
        student[l] -= 1

    # 3. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
    for i in range(1, n+1):
        if student[i] > 0:
            if student[i-1] < 0:
                student[i] -= 1
                student[i-1] += 1
            elif student[i+1] < 0:
                student[i] -= 1
                student[i+1] += 1

    # 4. 체육복을 갖고 있는 학생 수를 계산한다.
    answer = 0
    for i in range(1, n+1):
        if student[i] > -1:
            answer += 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
