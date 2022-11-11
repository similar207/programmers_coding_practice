def solution(n,a,b):
    answer = 1
    if abs(a-b) == 1:
        if a%2 == 0:
            if a < b:
                b += 1
        else:
            if b < a:
                a += 1
    while abs(a-b) != 1:
        n = int(n/2)
        if a%2 == 0:
            a = int(a/2)
        else:
            a = int(a/2)+1
        if b%2 == 0:
            b = int(b/2)
        else:
            b = int(b/2)+1
        answer += 1
        if abs(a-b) == 1:
            if a%2 == 0:
                if a < b:
                    b += 1
            else:
                if b < a:
                    a += 1

    return answer
