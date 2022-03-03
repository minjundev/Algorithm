def solution(number, k):
    length = len(number)-k
    answer = ''
    while length >= 1 :
        maxValue = '0'
        for i in range(len(number)-length+1) :
            if number[i] == '9' :
                maxValue = '9'
                break
            maxValue = max(maxValue, number[i])
        answer += maxValue
        number = number[number.index(maxValue)+1:]
        length -= 1
    return answer
