def solution(n, words):
    answer = [0,0]
    a = 1 #순서
    w = words[0][0] #끝 단어
    w1 = [] #말한 단어
    c = 1
    for i in words:

        if w != i[0]:
            return [a, c]
        w = i[-1]
        if i in w1:
            return [a, c]
        else:
            w1.append(i)
        a += 1
        if a > n:
            a -= n
            c += 1


    return answer
