from collections import deque

def solution(tickets):
    return bfs(tickets)

def bfs(tickets) :
    answerList = list()
    queue= deque()
    queue.append((tickets, ["ICN"])) # (남은티켓, 경유한 나라)

    while queue :
        togoList, visited = queue.popleft()
        if not togoList :
            answerList.append(visited)
            continue
        curr = visited[len(visited)-1]
        for togo in togoList :
            if togo[0] == curr :
                removed_togoList = togoList.copy()
                removed_togoList.remove(togo)
                queue.append((removed_togoList,visited+[togo[1]]))

    return sorted(answerList)[0]
