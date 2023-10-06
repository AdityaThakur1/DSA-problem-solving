class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while( left < right):
            sum2 = numbers[left] + numbers[right]
            if ( sum2 == target):
                return ([left+1, right+1])
            elif ( sum2 < target):
                left += 1
                continue
            else:
                right -= 1
                continue
        
        return([0,0])

    
"""        for i in range(len(numbers)):
            find = target - numbers[i]
            j = i+1
            k = len(numbers) - 1
            
            while(j <= k):
                mid = (j+k)//2
                if find == numbers[mid]:
                    return [i+1, mid+1]
                elif find < numbers[mid]:
                    k = mid - 1
                else:
                    j = mid + 1
        
        return [0,0]"""