def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    while routes :
        if len(routes) == 1 :
            answer += 1
            break

        domain = routes[0][1]
        routes.pop(0)

        candidates = list(filter(lambda x : x[0] <= domain and x[1] >= domain, routes))
        routes = list(filter(lambda x : x not in candidates, routes))
        answer += 1
    return answer
        
