def solution(n):
    answer = 0
    count_1 = 0 # 1의 갯수
    for i in bin(n)[2:]: # n을 2진수로 변환후 1의 갯수를 체크
        if i == "1":
            count_1 += 1

    while True:
        n += 1
        count = 0
        for i in bin(n)[2:]:
            if i == "1":
                count += 1
        if count == count_1:
            return n

    return answer
