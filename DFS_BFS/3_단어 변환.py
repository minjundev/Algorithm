from collections import deque

def solution(begin, target, words) :
    if target not in words :
        return 0
    return bfs(begin, target, words)

def bfs(begin, target, words) :
    answerList = list()
    queue = deque()
    queue.append((begin,0,[])) # (begin,answer,visited)

    while queue :
        curr, answer, visited = queue.popleft()
        if curr == target :
            answerList.append(answer)
            continue
        for word in words :
            if word in visited :
                continue
            if transistable(curr,word) :
                queue.append((word,answer+1,visited+[curr]))

    if not answerList :
        return 0
    else :
        return min(answerList)
    
def transistable(a,b):
    return sum((1 if x!=y else 0) for x,y in zip(a,b)) == 1
