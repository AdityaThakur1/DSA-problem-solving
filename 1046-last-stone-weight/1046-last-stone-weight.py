class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while(len(stones) > 1):
            s1 = -1*heapq.heappop(stones)
            s2 = -1*heapq.heappop(stones)

            if s1-s2 > 0:
                heapq.heappush(stones, -1*(s1-s2))
        
        if len(stones) == 0:
            return 0
        else:
            return -1*stones[0]