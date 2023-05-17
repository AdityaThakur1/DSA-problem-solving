class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)

        for n in nums:
            count[n] += 1
        
        arr = []
        for key in count.keys():
            arr.append(tuple([count[key],key]))
        
        arr.sort()

        result = []

        for i in range(k):
            x,y = arr[-1-i]
            result.append(y)
        
        return result
        
            
