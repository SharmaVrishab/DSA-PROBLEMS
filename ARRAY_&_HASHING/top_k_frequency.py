from collections import Counter
import heapq
def top_k_frequency(arr):
    counter = Counter(arr)
    heap = []
    for k,v in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (v, k))  # Push (frequency, element)
        else:
            heapq.heappushpop(heap, (v, k))  # Push and pop smallest frequency
    return [h[1] for h in heap]
arr = [1,1,2,2,2,3,3,3,3,3]
top_k_frequency(arr)

"""
Why Use heapq?
Heaps are efficient for:

Finding the smallest or largest elements.
Implementing priority queues.
Solving problems like "Top K elements" or "Kth smallest/largest element."
"""