def solution(bridge_length, weight, truck_weights):
    time = 0
    crossing = [0 for i in range(bridge_length)]
    while truck_weights :
        crossing.pop(0)
        if sum(crossing) + truck_weights[0] <= weight :
            crossing.append(truck_weights.pop(0))
        else :
            crossing.append(0)
        time += 1      
    return time+bridge_length
        
        
