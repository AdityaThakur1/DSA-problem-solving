class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        
        left, right = 0, len(height)-1
        
        while(left < right):
            vol = min(height[left], height[right]) * (right-left)
            max_vol = max(max_vol , vol)
            
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
            
        return max_vol