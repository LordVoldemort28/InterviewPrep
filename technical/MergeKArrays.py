from heapq import heapify, heappush, heappop

heap = []

heapify(heap)

heappush(heap, [1])
heappush(heap, [0, 2])
heappush(heap, [3, 4])

merge_list = []

while heap:

    current = heappop(heap)

    merge_list.append(current.pop(0))

    if len(current) > 0:

        heappush(heap, current)

print(merge_list)
