class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*n for n in stones]
        
        heapq.heapify(stones)
        
        while(len(stones) > 1):
            s1 = -1 * heapq.heappop(stones)
            s2 = -1 * heapq.heappop(stones)
            
            if s1 - s2 > 0:
                heapq.heappush(stones, s2-s1)
        
        heapq.heappush(stones, 0)
        
        return -1*stones[0]