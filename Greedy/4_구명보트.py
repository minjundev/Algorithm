from collections import deque

def solution(people, limit):
    people.sort()
    queue = deque(people)
    answer = 0
    while queue :
        if len(queue) == 1 :
            return answer+1
        if queue[0] + queue[-1] <= limit :
            queue.pop()
            queue.popleft()
        else :
            queue.pop()
        answer += 1
    return answer
            
        
