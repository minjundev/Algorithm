from collections import deque

def solution(numbers, target):
    return bfs(numbers, target)

def bfs(numbers, target) :
    answer = 0
    maxIndex = len(numbers)-1
    queue = deque()
    queue.append((numbers[0],0))
    queue.append((-numbers[0],0))

    while queue :
        number, index = queue.popleft()
        if number == target and index == maxIndex :
            answer += 1
        elif index >= maxIndex :
            continue
        else :
            queue.append((number+numbers[index+1],index+1))
            queue.append((number-numbers[index+1],index+1))
    return answer
    
