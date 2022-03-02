import heapq

def solution(heap, K):
    heap.sort()
    heapq.heapify(heap)
    answer = 0
    while heap[0] < K
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, first + second*2)
        answer += 1
    return answer
