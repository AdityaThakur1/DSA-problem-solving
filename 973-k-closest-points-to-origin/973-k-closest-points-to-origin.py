class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        result = []

        for x in points:
            dist.append(  [ math.sqrt(x[0]**2 + x[1]**2), x]   )
            
        heapq.heapify(dist)
        
        while(k>0):
            d, x = heapq.heappop(dist)
            result.append(x)
            k -= 1
        
        return result