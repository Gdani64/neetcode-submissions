import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                return -stones.pop()
            elif len(stones) == 0:
                return 0
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            if s1 == s2:
                continue
            heapq.heappush(stones, s1 - s2)
        return 0
