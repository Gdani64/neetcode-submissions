from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i,point in enumerate(points):
            
            heapq.heappush(minHeap, (sqrt(point[0]**2 + point[1]**2), i))
            print(minHeap)
        
        print(minHeap)
        res = []
        for i in range(k):
            pointIndex = heapq.heappop(minHeap)[1]
            res.append(points[pointIndex])
        return res
        



