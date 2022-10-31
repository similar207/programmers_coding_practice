def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5

    city = []
    answer = 0
    for i in cities:
        if i.upper() in city:
            city.pop(city.index(i.upper()))
            city.append(i.upper())
            answer += 1
        else:
            city.append(i.upper())
            if len(city) > cacheSize:
                city.pop(0)                
            answer += 5


    return answer
