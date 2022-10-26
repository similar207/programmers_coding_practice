def solution(n):
    answer = 0
    start_num = 1   #시작 숫자
    while start_num <= n:
        sum_num = 0     #연속된 숫자를 합한 숫자
        for i in range(start_num,n+1):
            sum_num += i    #연속된 숫자를 더함
            if sum_num == n:    #숫자의 합이 n과 같으면 정답 카운트 1 시작 숫자를 다음으로 옮김
                start_num += 1  
                answer += 1
            elif sum_num > n:
                start_num += 1
                break

    return answer
