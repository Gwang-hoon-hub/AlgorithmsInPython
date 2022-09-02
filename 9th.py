from itertools import combinations
def solution(orders, course):
    answer = []
    # 1. 각 order 정렬
    for i in range(len(orders)):
        orders[i] = "".join(sorted(orders[i]))
        print(orders[i])

    # 2. course_len 마다 조합 생성
    for course_len in course:
        hash = {}
        max = 0
        for order in orders:
            # 각 Order를 기준으로 courseLength 만큼의 조합 만들기
            for comb in combinations(order, course_len):
                key="".join(comb)
                new_value = hash.get(key,0) + 1
                hash[key] = new_value
                if max < new_value:
                    max = new_value

        # 3. 가장 많은 조합 저장
        if max > 1:
            for type in hash:
                if max == hash[type]:
                    answer.append(type)

    answer.sort()
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
출처: https://coding-grandpa.tistory.com/103?category=981506 [개발자로 취직하기:티스토리]
