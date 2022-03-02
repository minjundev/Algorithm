def solution(priorities, location):
    iList = [i for i in range(len(priorities))]
    answer = []

    while iList :
        curr_i = iList.pop(0)
        priority = priorities.pop(0)
        if isMax(priority, priorities) :
            answer.append(curr_i)
        else :
            iList.append(curr_i)
            priorities.append(priority)
    return answer.index(location)+1


def isMax(x, aList) :
    for a in aList :
        if a > x :
            return False
    return True
