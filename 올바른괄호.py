def solution(s):
    answer = True
    count = 0
    if s[0] == ")":
        return False
    
    for i in s:
        if count < 0 and i == "(":
            return False
        if i == "(":
            count += 1
        else:
            count -= 1
            
    if count != 0:
        return False

    return True
