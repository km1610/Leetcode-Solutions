import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [-1]
        mini = []
        visited = set()
        heapq.heapify(heap)
        heapq.heapify(mini)
        while len(heap)!=n:
            m = heapq.heappop(heap)
            if (m*2) not in visited:
                heapq.heappush(mini,-(m*2))
                visited.add(m*2)
            if (m*3) not in visited:
                heapq.heappush(mini,-(m*3))
                visited.add(m*3)
            if (m*5) not in visited:
                heapq.heappush(mini,-(m*5))
                visited.add(m*5)
            heapq.heappush(heap,m)
            minimum = -heapq.heappop(mini)
            heapq.heappush(heap,minimum)

        return -heapq.heappop(heap)
