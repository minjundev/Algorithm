from collections import deque

def solution(n, computers):
    visited = [0]*n
    answer = 0
    while 0 in visited :
        bfs(n, computers, visited.index(0), visited)
        answer += 1
    return answer
        

def bfs(n, computers, src, visited) :
    queue = deque()
    queue.append(src)
    visited[src] = 1

    while queue :
        num = queue.popleft()
        for i in range(n) :
            if computers[num][i] == 1 and visited[i] == 0 :
                queue.append(i)
                visited[i] = 1
    
