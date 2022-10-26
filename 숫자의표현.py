def solution(n):
    answer = 0
    start_num = 1
    while start_num <= n:
        sum_num = 0
        for i in range(start_num,n+1):
            sum_num += i
            if sum_num == n:
                start_num += 1
                answer += 1
            elif sum_num > n:
                start_num += 1
                break

    return answer
