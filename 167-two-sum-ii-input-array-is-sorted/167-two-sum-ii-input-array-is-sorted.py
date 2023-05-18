class Solution:
   
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            t1 = target - numbers[i]
            
            left, right = i+1, len(numbers)-1      
            while(left <= right):
                mid = (left + right)//2
                if(t1 == numbers[mid]):
                    return(i+1,mid+1)
                elif (t1 < numbers[mid]):
                    right = mid - 1
                else :
                    left = mid + 1

        return []