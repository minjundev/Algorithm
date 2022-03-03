import heapq

def solution(operations):
    heap = []
    for operation in operations :
        heap = execute(heap, operation)
        heapq.heapify(heap)
    return output(heap)


def execute(heap, operation) :
    operation = operation.split(' ')
    operator = operation[0]
    operand = operation[1]
    if operator == 'I' :
        heapq.heappush(heap, int(operand))
    elif operator == 'D' :
        if not heap :
            return []
        if operand == '-1' :
            heapq.heappop(heap)
        elif operand == '1' :
            heap = heap[:-1]
    return heap
    

def output(heap) :
    if not heap :
        return [0,0]
    minValue = heap[0]
    heap.sort(reverse = True)
    maxValue = heap[0]
    return [maxValue, minValue]
        
