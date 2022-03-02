from collections import Counter

def solution(progresses, speeds):
    dayList = list(map(executeDay, list(zip(progresses, speeds))))
    for i in range(1,len(dayList)) :
        if dayList[i] < dayList[i-1] :
            dayList[i] = dayList[i-1]
    return list(map(lambda x : x[1], sorted(list(Counter(dayList).items()), key = lambda x : x[0])))  

def executeDay(atuple) :
    progress = 100 - atuple[0]
    speed = atuple[1]
    if not (progress%speed) :
        return progress // speed
    return (progress//speed)+1

    
        
