import math
def solution(brown, yellow):
    tile = brown + yellow
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow%i > 0:
            continue
        yellow_x = int(yellow/i)
        if brown == (yellow_x+2)*2 + i*2:
            return [yellow_x+2, i+2]
