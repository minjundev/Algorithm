def solution(N, number):
    answer = -1
    dp = list()
    
    for i in range(1,9):
        alls = set()
        check_number = int(str(N)*i)
        alls.add(check_number)
        
        for j in range(0,i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1] :
                    alls.add(op1 + op2)
                    alls.add(op1 - op2)
                    alls.add(op1 * op2)
                    if op2 != 0:
                        alls.add(op1 // op2)
                        
        if number in alls:
            answer = i
            break
            
        dp.append(alls) 
    return answer
