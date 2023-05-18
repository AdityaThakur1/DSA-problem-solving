class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        for n in (num_set):
            if (n-1 in num_set):
                continue
            else:
                #find the maximum length starting with this number
                k = n+1
                seq = 1
                while(k in num_set):
                    seq += 1
                    k += 1
                result = max(result, seq)
                
        return result