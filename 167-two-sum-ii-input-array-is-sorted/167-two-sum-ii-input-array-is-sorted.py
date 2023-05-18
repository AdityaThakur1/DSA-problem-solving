class Solution:
    def bin_search(self, nums: List[int], target: int):
        left, right = 0, len(nums)-1      
        while(left <= right):
            mid = (left + right)//2
            if(target == nums[mid]):
                return mid
            elif (target < nums[mid]):
                right = mid - 1
            else :
                left = mid + 1
        return None
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            t1 = target - numbers[i]
            t2 = self.bin_search(numbers[i+1:],t1)
            
            if(t2 is not None):
                return(i+1,i+t2+2)
            
        return []