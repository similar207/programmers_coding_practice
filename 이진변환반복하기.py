def solution(s):
    count_0 = 0 # 제거된 0의 갯수
    count = 0   # 이진변환 횟수
    while len(s) > 1:
        length = 0   # 제거후 길이
        for i in s:
            if i == "1":
                length += 1
            else:
                count_0 += 1
        s = bin(length)[2:]
        count += 1
    return [count, count_0]
