def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    copy_reserve = reserve.copy()
    for res in copy_reserve :
        if res in lost :
            lost.remove(res)
            reserve.remove(res)
    copy_lost = lost.copy()
    for lst in copy_lost :
        if lst-1 in reserve :
            lost.remove(lst)
            reserve.remove(lst-1)
        elif lst+1 in reserve :
            lost.remove(lst)
            reserve.remove(lst+1)
    
    return n-len(lost)
