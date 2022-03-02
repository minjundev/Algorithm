import heapq

def solution(jobs):
    jobs.sort()
    time = 0
    answer = list()

    while jobs :
        candidates = list()
        for job in jobs :
            if job[0] <= time :
                candidates.append(job)
            else :
                break

        if not candidates :
            answer.append(jobs[0][1])
            time = time + jobs[0][1] + abs(jobs[0][0] - time)
            jobs.pop(0)
            continue
            
        elif len(candidates) == 1 :
            answer.append(abs(time - jobs[0][0]) + jobs[0][1])
            time = time + jobs[0][1]           
            jobs.pop(0)
            continue
                
        else :
            candidates = sorted(candidates, key = lambda x : x[1])
            answer.append(abs(time - candidates[0][0]) + candidates[0][1])
            time = time + candidates[0][1]
            jobs.remove(candidates[0])
    return int(sum(answer) // len(answer)) 
