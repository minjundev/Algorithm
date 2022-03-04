def solution(n, costs):
    connected = list()
    costs.sort(key = lambda x : (x[2],x[0],x[1]))
    connected.append([costs[0][0], costs[0][1]])
    idx = 1
    answer = costs[0][2]

    if len(costs) == 1 :
        return answer
    
    while len(connected[0]) != n :
        zero = -1
        one = -2
        
        for i in range(len(connected)) :
            if costs[idx][0] in connected[i] :
                zero = i
            if costs[idx][1] in connected[i] :
                one = i

        if zero == one :
            pass

        elif zero >= 0 and one >= 0 :
            connected[zero] += connected[one]
            connected.pop(one)
            answer += costs[idx][2]

        elif zero < 0 and one < 0 :
            connected.append([costs[idx][0], costs[idx][1]])
            answer += costs[idx][2]
        
        elif zero >= 0 :
            connected[zero].append(costs[idx][1])
            answer += costs[idx][2]
        
        elif one >= 0 :
            connected[one].append(costs[idx][0])
            answer += costs[idx][2]
            
        idx += 1
        if idx > len(costs)-1 :
            break

    return answer

