class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h1, h2 = 0,0
        
        while(1):
            h1 = nums[h1]
            h2 = nums[nums[h2]]
            
            if h1 == h2:
                break
        h2 = 0
        
        while(1):
            h1 = nums[h1]
            h2 = nums[h2]
            
            if h1 == h2:
                break
                
        return h1
        